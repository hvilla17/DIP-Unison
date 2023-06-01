# File: face_detection_picture.py
import cv2 as cv

image = cv.imread('../images/bad_boys.jpg')
# instantiate a CascadeClassifier object
classifier = cv.CascadeClassifier()
# load the cascade
if not classifier.load('../classifiers/haarcascade_frontalface_alt.xml'):
    print('Error loading face cascade')
    exit(0)
# detect faces
faces = classifier.detectMultiScale(image)
print(faces)
print(f'{len(faces)} faces detected')
# write rectangles around faces
for (x, y, w, h) in faces:
    frame = cv.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), lineType=cv.LINE_AA)
cv.imwrite('bad_boys_faces.jpg', image)
