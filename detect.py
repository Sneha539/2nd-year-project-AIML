import cv2
from ultralytics import YOLO
import datetime
import os

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

# create folder for intruder images
if not os.path.exists("intruders"):
    os.makedirs("intruders")

print("Camera started...")

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
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.putText(frame, "INTRUDER", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    if human_detected:
        print("Intruder detected!")

        # Save image with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"intruders/intruder_{timestamp}.jpg"
        cv2.imwrite(filename, frame)

    cv2.imshow("Campus Security Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
