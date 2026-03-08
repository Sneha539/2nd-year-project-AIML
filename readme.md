AI-Powered Campus Intrusion Detection System
Project Overview

This project implements an AI-based campus security system that detects unauthorized human presence in restricted areas using computer vision. The system uses a pretrained YOLOv8 object detection model to identify humans from a live camera feed. When an intruder is detected outside allowed hours, the system captures visual evidence, logs the event, sends an email alert to the administrator, and displays the alert on a secure web dashboard.

The goal of this project is to demonstrate how Artificial Intelligence and IoT-style monitoring can be combined to build an intelligent surveillance system for smart campuses.

🧠 Key Features
1. Real-Time Human Detection

The system uses the YOLOv8 deep learning model to detect humans in real time from a camera feed using OpenCV.

2. Time-Based Authorization

The system allows human presence only during predefined hours. If a person is detected outside those hours, the system classifies the event as an intrusion.

3. Intruder Image Capture

When an intrusion occurs, the system captures and saves an image with a timestamp in the intruders folder.

4. Intrusion Logging

Each intrusion event is logged with the following details:

->Timestamp

->Intrusion status

->Image path

The data is stored in a structured CSV file for dashboard display.

5. Email Alert System

When an intrusion is detected, the system automatically sends an email alert to the administrator with the captured intruder image attached.

6. Secure Dashboard

A Flask-based dashboard allows authorized users to monitor intrusion events.

The dashboard displays:

->Total number of intrusions

->Timestamp of each intrusion

->Intruder images

->Intrusion status

7. User Authentication

The dashboard is protected by a login system so that only authorized administrators can access the monitoring interface.

⚙️ Technologies Used

Programming Language
Python

Computer Vision
OpenCV

Deep Learning Model
YOLOv8 (Ultralytics)

Web Framework
Flask

Authentication
Flask-Login

Email Notifications
SMTP / Yagmail

Version Control
Git and GitHub

📊 System Workflow

1. Camera captures live video feed

2. YOLOv8 detects humans in each frame

3. System checks if current time is within allowed hours

4. If unauthorized presence is detected:

->Intruder image is saved

->Event is logged

->Email alert is sent

->Dashboard is updated

5. Administrator monitors events through the web dashboard

📈 Expected Outcomes

The system provides a basic prototype of an intelligent campus surveillance system capable of:

->real-time human detection

->automated intrusion alerts

->secure monitoring dashboard

->evidence logging for security review

🌍 Industry Relevance

This system can be extended and deployed in:

  ->Smart campuses

  ->Corporate offices

  ->Industrial facilities

  ->Data centers

  ->Defense environments

  ->Smart city infrastructure

The architecture supports expansion to:

  ->Multi-camera networks

  ->Edge device deployment (Raspberry Pi / Jetson)

  ->Cloud-based analytics

  ->Person re-identification systems

  ->IoT alarm integration

🔐 Future Improvements

Potential enhancements include:

->Database integration instead of CSV logging

->Multi-camera support for large campuses

->SMS or mobile push notifications

->Face recognition for authorized users

->Edge deployment using Raspberry Pi or Jetson devices

🏁 Conclusion

This project demonstrates how AI-based computer vision and web technologies can be integrated to create a smart security monitoring system. It provides a foundation for building scalable surveillance systems for campuses, offices, and smart city environments.