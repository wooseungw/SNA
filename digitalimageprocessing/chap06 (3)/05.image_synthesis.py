import cv2
import numpy as np

# 1) 두 그레이스케일 이미지 읽기
img1 = cv2.imread('./images/add1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./images/add2.jpg', cv2.IMREAD_GRAYSCALE)
if img1 is None or img2 is None:
    raise FileNotFoundError('img1.png 또는 img2.png 파일을 찾을 수 없습니다.')
if img1.shape != img2.shape:
    raise ValueError('입력 이미지들의 크기(shape)가 일치해야 합니다.')

# 2) float32로 캐스팅 후 합성
#    → np.float32를 쓰면 오버플로우 없이 정확한 합성값 확보 가능
sum_img = img1.astype(np.float32) + img2.astype(np.float32)

# 3) 선형 노말라이즈
#    sum_img_norm = (sum_img - min) / (max - min) * 255
min_val, max_val = sum_img.min(), sum_img.max()
if max_val == min_val:
    # 두 이미지가 완전히 동일하거나 모두 0이라면 그냥 0 영상으로 처리
    normalized = np.zeros_like(sum_img, dtype=np.uint8)
else:
    normalized = ((sum_img - min_val) / (max_val - min_val) * 255.0).astype(np.uint8)

# ───────────────────────────────────────────────────────────────
# 또는 OpenCV 내장 함수로:
# cv2.normalize(sum_img, normalized, 0, 255, cv2.NORM_MINMAX)
# normalized = normalized.astype(np.uint8)
# ───────────────────────────────────────────────────────────────

# 4) 결과 저장 및 표시
# cv2.imwrite('composite_normalized.png', normalized)
cv2.imshow('Composite (Normalized)', normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()