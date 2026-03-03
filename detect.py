import cv2
from ultralytics import YOLO
import datetime
import os
import csv

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

# Create folders if not exist
if not os.path.exists("intruders"):
    os.makedirs("intruders")

# Create log file if not exist
log_file = "logs.csv"
if not os.path.exists(log_file):
    with open(log_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "status", "image_path"])

print("Camera started...")

last_intruder_time = None  # Prevent duplicate logs within short time

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    human_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "person":
                human_detected = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if human_detected:
        if 9 <= current_hour < 17:
            cv2.putText(frame, "Authorized Access", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print("Authorized person (allowed time)")
        else:
            cv2.putText(frame, "INTRUDER ALERT!", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Prevent saving multiple images every frame
            if last_intruder_time is None or (current_time - last_intruder_time).seconds > 10:

                timestamp_str = current_time.strftime("%Y%m%d_%H%M%S")
                filename = f"intruders/intruder_{timestamp_str}.jpg"
                cv2.imwrite(filename, frame)

                # Log to CSV
                with open(log_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        current_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "INTRUDER",
                        filename
                    ])

                print("Intruder logged and image saved.")
                last_intruder_time = current_time

    cv2.imshow("Campus Security Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()