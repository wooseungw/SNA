import cv2
import numpy as np

INIT_X = 50
INIT_Y = 60

roi_pts = []

def make_view(name, img, x, y, put_text=""):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(name, x, y)
    disp = img.copy()
    if put_text:
        cv2.putText(
            disp, put_text, (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (0, 0, 255), 2, cv2.LINE_AA
        )
    cv2.imshow(name, disp)

def nothing(x):
    pass

def clip_image(image):
    return np.clip(image, 0, 255).astype(np.uint8)

def warp_roi(image, src_pts, dst_size=(480, 360)):
    if len(src_pts) != 4:
        return np.zeros((dst_size[1], dst_size[0], 3), dtype=np.uint8)
    src = np.array(src_pts, dtype=np.float32)
    dst = np.array([
        [0, 0],
        [dst_size[0] - 1, 0],
        [dst_size[0] - 1, dst_size[1] - 1],
        [0, dst_size[1] - 1]
    ], dtype=np.float32)
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, dst_size, flags=cv2.INTER_NEAREST)
    return warped

def get_roi_mask(image_shape, points):
    mask = np.zeros(image_shape[:2], dtype=np.uint8)
    if len(points) == 4:
        pts = np.array(points, dtype=np.int32)
        cv2.fillPoly(mask, [pts], 1)
    return mask

def enhance_roi_contrast(image, mask=None):
    result = image.copy().astype(np.float32)
    if mask is not None and np.any(mask):
        ys, xs = np.where(mask > 0)
        y0, y1 = ys.min(), ys.max()
        x0, x1 = xs.min(), xs.max()
        # ROI 패치 추출
        patch = result[y0:y1+1, x0:x1+1].copy()
        patch_mask = mask[y0:y1+1, x0:x1+1]
        # 노이즈 완화를 위해 미디언 필터 적용
        patch_uint8 = clip_image(patch)
        patch = cv2.medianBlur(patch_uint8, ksize=3).astype(np.float32)
        # 채널별 히스토그램 평활화
        for c in range(3):
            channel = patch[..., c]
            eq = cv2.equalizeHist(channel.astype(np.uint8)).astype(np.float32)
            channel[patch_mask > 0] = eq[patch_mask > 0]
            patch[..., c] = channel
        # 결과 병합
        result_roi = result[y0:y1+1, x0:x1+1]
        result_roi[patch_mask > 0] = patch[patch_mask > 0]
        result[y0:y1+1, x0:x1+1] = result_roi
    # 병합 후 전체 결과 클램핑
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

def on_mouse(event, x, y, flags, param):
    global roi_pts
    if event == cv2.EVENT_LBUTTONDOWN and len(roi_pts) < 4:
        roi_pts.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        roi_pts.clear()

def show(image_path="./a2.jpeg"):
    global roi_pts
    frame = cv2.imread(image_path)
    if frame is None:
        print("이미지를 열 수 없습니다:", image_path)
        return
    W = 480
    H = int(frame.shape[0] * (W / frame.shape[1]))
    frame = cv2.resize(frame, (W, H))
    logf = cv2.log(frame.astype(np.float32) + 1.0)
    logf = cv2.normalize(logf, None, 0, 255, cv2.NORM_MINMAX)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
    l_norm = gray / 255.0
    weight = (1.0 - l_norm)[..., np.newaxis]
    ctrl_win = "Information"
    blank = np.zeros((1, 500, 3), dtype=np.uint8)
    cv2.namedWindow(ctrl_win, cv2.WINDOW_NORMAL)
    init_alpha = 40
    cv2.createTrackbar("alpha", ctrl_win, init_alpha, 100, nothing)
    cv2.imshow(ctrl_win, blank)
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Original", on_mouse)
    while True:
        alpha = cv2.getTrackbarPos("alpha", ctrl_win) / 100.0
        cv2.moveWindow(ctrl_win, INIT_X + int(0.5 * W), 0)
        adaptive = frame.astype(np.float32) + logf * alpha * weight
        adaptive = clip_image(adaptive)
        display_frame = frame.copy()
        for pt in roi_pts:
            cv2.circle(display_frame, pt, 4, (0, 255, 255), -1)
        warped = warp_roi(adaptive, roi_pts, dst_size=(W, H))
        roi_mask = get_roi_mask(adaptive.shape, roi_pts)
        enhanced_roi = enhance_roi_contrast(adaptive, roi_mask)
        original_ms = f"Mean: {frame.mean():.1f} Std: {frame.std():.1f}"
        adap_ms = f"Mean: {adaptive.mean():.1f} Std: {adaptive.std():.1f}"
        enhanced_ms = f"Mean: {enhanced_roi.mean():.1f} Std: {enhanced_roi.std():.1f}"
        warp_ms = f"Warped ROI ({len(roi_pts)} pts)"
        make_view("Original", display_frame, INIT_X, INIT_Y, original_ms)
        make_view("Adaptive Better", adaptive, INIT_X, INIT_Y + H + 10, adap_ms)
        make_view("ROI Enhanced", enhanced_roi, INIT_X + W, INIT_Y + H + 10, enhanced_ms)
        make_view("ROI Region (Warped)", warped, INIT_X + W, INIT_Y, warp_ms)
        key = cv2.waitKey(30) & 0xFF
        if key == 27:
            break
        elif key == ord('r'):
            roi_pts.clear()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img_list = [
        "./a.png",
        "./a2.jpeg",
        "./a3.jpeg",
        "./a4.png"
    ]
    for img in img_list:
        show(img)
