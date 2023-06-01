# File: video_10s.py
import cv2 as cv

# differences with previous program are in blue
cameraCapture = cv.VideoCapture(0)
fps = 30  # An assumption
size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv.VideoWriter('MyOutputVid.avi',
                             cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                             fps, size)
success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1  # 10 seconds of frames
while numFramesRemaining > 0:
    if frame is not None:
        videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
