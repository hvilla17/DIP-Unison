# File: video_copy.py
import cv2 as cv

videoCapture = cv.VideoCapture('../videos/MyInputVid.avi')
fps = videoCapture.get(cv.CAP_PROP_FPS)
size = (int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
print(fps)  # frames per second
print(size)  # (rows, cols)
videoWriter = cv.VideoWriter('MyOutputVid.avi',
                             cv.VideoWriter_fourcc('I', '4', '2', '0'),
                             fps, size)
success, frame = videoCapture.read()
while success:  # Loop until there are no more frames
    videoWriter.write(frame)
    success, frame = videoCapture.read()
