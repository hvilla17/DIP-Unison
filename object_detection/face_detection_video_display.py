# File: face_detection_video_display.py
# Adapted from: https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
from __future__ import print_function
import cv2 as cv


def detect_and_display(picture):
    frame_gray = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    # Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        picture = cv.ellipse(picture, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

        face_roi = frame_gray[y:y + h, x:x + w]
        # In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(face_roi)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            picture = cv.circle(picture, eye_center, radius, (255, 0, 0), 4)

    cv.imshow('Capture - Face detection', picture)


face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

# Load the cascades
if not face_cascade.load('../classifiers/haarcascade_frontalface_alt.xml'):
    print('Error loading face cascade')
    exit(0)
if not eyes_cascade.load('../classifiers/haarcascade_eye_tree_eyeglasses.xml'):
    print('Error loading eyes cascade')
    exit(0)

# Read the video stream
cap = cv.VideoCapture('../videos/people.mp4')
if not cap.isOpened:
    print('Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('Break!')
        break

    detect_and_display(frame)

    if cv.waitKey(1) == 27:
        break
