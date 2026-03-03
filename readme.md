AI-Powered Smart Vision-Based Campus Intrusion Detection System
📌 Project Overview

This project presents a real-time AI-based security system designed to detect unauthorized human presence in restricted areas such as laboratories, server rooms, hostels, or research facilities.

The system uses a pretrained deep learning object detection model (YOLOv8) to detect humans via a camera feed. Based on predefined authorization logic (time-based access control), it classifies detected individuals as either authorized or intruders.

Upon detecting an intrusion, the system:
Saves visual evidence with timestamps
Logs the event in a structured CSV file
Displays alerts on a live monitoring dashboard
The solution demonstrates the integration of Artificial Intelligence and IoT-based security architecture.

🎯 Objectives

Detect and classify human presence using computer vision
Implement time-based authorization logic
Log intrusion events with timestamped image evidence
Provide a live web-based dashboard for monitoring
Design a scalable system architecture suitable for campus deployment

🧠 System Architecture
1. Vision Module

Captures live video using laptop camera
Uses YOLOv8 pretrained model for human detection
Identifies “person” class in real time

2. Authorization Logic

Defines allowed access hours (9 AM – 5 PM)
Flags presence outside allowed time as intrusion

3. Evidence Logging Module

Saves intrusion images inside intruders/ folder
Logs intrusion data into logs.csv with:
Timestamp
Status
Image path

4. Dashboard Module

Built using Flask framework

Displays:
Total intrusions
Timestamped logs
Intruder images
Auto-refreshes every 5 seconds

⚙️ Technologies Used

Python
OpenCV
YOLOv8 (Ultralytics)
Flask
CSV (for structured logging)
Git & GitHub (version control)

📊 System Workflow

Camera captures live frame
YOLOv8 detects objects
If object class = "person":
System checks current time
If outside allowed hours:
Marks as INTRUDER
Saves image
Logs event
Dashboard displays updated intrusion record

📈 Expected Outcomes

Real-time human detection accuracy using pretrained model
Automated intrusion logging
Reduced false alarms through time-based filtering
Visual evidence for each unauthorized entry
Scalable architecture adaptable for multi-camera deployment

🌍 Industry Relevance

This system can be extended and deployed in:

Smart campuses
Corporate offices
Industrial facilities
Data centers
Defense environments
Smart city infrastructure

The architecture supports expansion to:
Multi-camera networks
Edge device deployment (Raspberry Pi / Jetson)
Cloud-based analytics
Person re-identification systems
IoT alarm integration

🔐 Scalability and Future Enhancements

Integration with Arduino-based alert system
Multi-zone camera deployment
Face recognition for authorized personnel
Cloud-based log storage
Mobile notification alerts
Privacy-preserving tracking system

🏁 Conclusion

This project demonstrates the practical implementation of an AI-powered intrusion detection system using real-time computer vision and IoT principles.

It successfully integrates:

Artificial Intelligence (human detection)
Authorization logic
Evidence logging
Web-based monitoring interface
The system serves as a scalable foundation for intelligent security infrastructure in modern smart environments.