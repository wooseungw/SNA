import numpy as np, cv2
from Common.filters import erode, dilate

def opening(img, mask):                     # 열림 연산
    tmp = erode(img, mask)                  # 침식
    dst = dilate(tmp, mask)                 # 팽창
    return dst

def closing(img, mask):                     # 닫힘 연산
    tmp = dilate(img, mask)
    dst = erode(tmp, mask)
    return dst

image = cv2.imread('images/test_car/11.jpg', cv2.IMREAD_GRAYSCALE)

if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],                 # 마스크 초기화
                 [1, 1, 1], 
                 [0, 1, 0]]).astype("uint8")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]   # 영상 이진화

dst1 = opening(th_img, mask)                            # 사용자 정의 열림 함수 호출
dst2 = closing(th_img, mask)                            # 사용자 정의 닫힘 함수 호출
dst3 = erode(th_img, mask)                            # OpenCV의 열림 함수
dst4 = dilate(th_img, mask)                            # OpenCV의 닫힘 함수


cv2.imshow("original", th_img)
cv2.imshow("opening", dst1)       
cv2.imshow("closing", dst2)
cv2.imshow("erode", dst3)
cv2.imshow("dilate", dst4)

cv2.waitKey(0)