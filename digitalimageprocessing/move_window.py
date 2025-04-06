import numpy as np
import cv2

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)    # 300x500, 흰색 영상 생성

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 50), (150, 100)
pt3, pt4 = (100, 200), (200, 270)


cv2.putText(image, "SIMPLEX", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, brown)
cv2.putText(image, "TRIPLEX", (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 2, olive)
cv2.putText(image, "DUPLEX", (10, 110), cv2.FONT_HERSHEY_DUPLEX, 3, violet)
cv2.putText(image, "COMPLEX_SMALL", (10, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))

fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
cv2.putText(image, "ITALIC", (10, 190), fontFace, 1, (0, 0, 0))

cv2.imshow("Put Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
