import cv2
gstr = "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)NV12,framerate=(fraction)30/1 ! nvvi dconv flip-method=2 ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx !videoconvert ! video/x-raw, format=(string)BGR ! appsink"
cam = cv2.VideoCapture(gstr, cv2.CAP_GSTREAMER)

for i in range(1000):
    _, frame = cam.read()
    cv2.imshow("frame", frame)
    
cam.release()