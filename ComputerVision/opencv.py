import cv2 as cv
import numpy as np

img = cv.imread('./ComputerVision/soccer.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Lena', img)
cv.imshow('Gray', gray)

cv.waitKey(0)
cv.destroyAllWindows()