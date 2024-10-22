# https://github.com/mushfiq1998/object-detection-using-yolov5-from-scartch-python-opencv?source=post_page-----cfb6b65f540b--------------------------------
# https://medium.com/@KaziMushfiq1234/object-detection-using-yolov5-from-scartch-with-python-computer-vision-cfb6b65f540b

import cv2
import torch

# Download model from GitHub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# model = torch.hub.load('yolov5', 'yolov5n', source= 'local')

cap = cv2.VideoCapture('slow_traffic_small.mp4')

while True:
    img = cap.read()[1]
    if img is None:
        break

    # Perform detection on image
    result = model(img)
    print('result: ', result)

    # Convert detected result to pandas data frame
    data_frame = result.pandas().xyxy[0]
    print('data_frame:')
    print(data_frame)

    # Get indexes of all the rows
    indexes = data_frame.index
    for index in indexes:
        # Find the coordinate of top left corner of bounding box
        x1 = int(data_frame['xmin'][index])
        y1 = int(data_frame['ymin'][index])
        # Find the coordinate of right bottom corner of bounding box
        x2 = int(data_frame['xmax'][index])
        y2 = int(data_frame['ymax'][index])

        # Find label name
        label = data_frame['name'][index]
        # Find confidence score of the model
        conf = data_frame['confidence'][index]
        text = label + ' ' + str(conf.round(decimals=2))

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
        cv2.putText(img, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 255, 0), 2)

    cv2.imshow('IMAGE', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
