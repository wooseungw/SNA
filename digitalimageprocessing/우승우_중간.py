import cv2
import numpy as np

INIT_X = 50
INIT_Y = 60

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

def show(image_path="./a2.jpeg"):
    # 1) 이미지 로드 & 리사이즈
    frame = cv2.imread(image_path)
    if frame is None:
        print("이미지를 열 수 없습니다:", image_path)
        return
    W = 480
    H = int(frame.shape[0] * (W / frame.shape[1]))
    frame = cv2.resize(frame, (W, H))

    # 2) 로그 변환 + 정규화
    logf = cv2.log(frame.astype(np.float32) + 1.0)
    logf = cv2.normalize(logf, None, 0, 255, cv2.NORM_MINMAX)

    # 3) 그레이→weight 계산 (adaptive)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)
    # gray = cv2.log(gray + 1.0)
    
    gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
    l_norm = gray / 255.0
    weight = (1.0 - l_norm)[..., np.newaxis]  # shape=(H,W,1)

    # 4) 트랙바 창 생성
    ctrl_win = "Information"
    # 트랙바용 빈 이미지를 그대로 imshow 시켜서 창 크기를 고정
    blank = np.zeros((1, 500, 3), dtype=np.uint8)
    cv2.namedWindow(ctrl_win, cv2.WINDOW_NORMAL)
    # 초기 alpha = 40%
    init_alpha = 40
    cv2.createTrackbar("alpha", ctrl_win, init_alpha, 100, nothing)
    cv2.imshow(ctrl_win, blank)

    while True:
        # 5) 트랙바에서 alpha 읽기
        alpha = cv2.getTrackbarPos("alpha", ctrl_win) / 100.0
        cv2.moveWindow(ctrl_win, INIT_X + int(0.5*W), 0)

        # 6) Better & Adaptive Better 계산
        #    Better: frame + alpha * logf
        better = frame.astype(np.float32) + logf * alpha
        better = cv2.normalize(better, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        #    Adaptive: frame + alpha * logf * weight
        adaptive = frame.astype(np.float32) + logf * alpha * weight
        adaptive = cv2.normalize(adaptive, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        # 7) Mean/Std 문자열
        original_ms = f"Mean: {frame.mean():.1f} Std: {frame.std():.1f}"
        log_ms  = f"Mean: {logf.mean():.1f} Std: {logf.std():.1f}"
        better_ms    = f"Mean: {better.mean():.1f} Std: {better.std():.1f}"
        adaptive_better_ms    = f"Mean: {adaptive.mean():.1f} Std: {adaptive.std():.1f}"

        # 8) 뷰 배치 및 출력
        make_view("Original",        frame,              INIT_X,          INIT_Y,         original_ms)
        make_view("Log Transform",   logf.astype(np.uint8), INIT_X,          INIT_Y + H + 10, log_ms)
        make_view("Better",          better,             INIT_X + W, INIT_Y,         better_ms)
        make_view("Adaptive Better", adaptive,           INIT_X + W, INIT_Y + H + 10, adaptive_better_ms)
        make_view("weight map", cv2.normalize(weight, None,0,255,cv2.NORM_MINMAX).astype(np.uint8), INIT_X + 2*W, INIT_Y + H + 10)
        # 9) 키 이벤트 처리ㅌ
        key = cv2.waitKey(30) & 0xFF
        # print("key:", key)
        if int(key) == 27:      # 종료
            break
        elif int(key)==2:    # ‘<’ 키로 감소
            val = cv2.getTrackbarPos("alpha", ctrl_win)
            cv2.setTrackbarPos("alpha", ctrl_win, max(0, val - 5))
        elif int(key)==3:    # ‘>’ 키로 증가
            val = cv2.getTrackbarPos("alpha", ctrl_win)
            cv2.setTrackbarPos("alpha", ctrl_win, min(100, val + 5))


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
    