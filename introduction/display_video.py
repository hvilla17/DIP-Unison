# File: display_video.py
import cv2 as cv

clicked = False


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv.VideoCapture(0)
cv.namedWindow('MyWindow')
cv.setMouseCallback('MyWindow', onMouse)
print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()
while success and cv.waitKey(1) == -1 and not clicked:
    cv.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv.destroyWindow('MyWindow')
