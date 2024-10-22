import cv2
import torch


def process_frame(frame):
    # YOLOv5 inference on the frame
    results = model(frame)

    # Extract results and get bounding boxes
    labels, coordinates = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

    # Loop through detections
    for i in range(len(labels)):
        class_id = int(labels[i])
        class_name = class_names[class_id]

        if class_name == 'car':  # Check if label is 'car'
            x1, y1, x2, y2, conf = coordinates[i]

            # Scale the bounding boxes back to the frame size
            h, w, _ = frame.shape
            x1, y1, x2, y2 = int(x1 * w), int(y1 * h), int(x2 * w), int(y2 * h)

            # Draw rectangle for bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Add label for the car
            cv2.putText(frame, f'Car {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame


# Load the YOLOv5 model (YOLOv5s is a small version, adjust as necessary)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Class labels that YOLOv5 can detect
class_names = model.names

# Video capture from file or camera
video_path = 'slow_traffic_small.mp4'  # Change to your video file or use 0 for webcam
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Video stream ended or error.")
        break

    # Process frame for car detection
    frame = process_frame(frame)

    # Show the result
    cv2.imshow('Car Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
