🚨 AI-Powered Campus Intrusion Detection System (AI + IoT)

📌 Overview

This project is a real-time AI-based security system designed to detect unauthorized human presence in restricted areas such as labs, server rooms, or campus facilities.

The system uses a deep learning model (YOLOv8) to detect humans via a camera feed, applies time-based authorization logic, logs intrusions into a database, sends email alerts, and triggers physical hardware alarms using Arduino.

A secure web dashboard allows administrators to monitor activity in real-time.


🎯 Key Features

🧠 AI-Based Human Detection
1. Uses YOLOv8 (Ultralytics) for real-time object detection
2. Detects humans from live camera feed
3. Draws bounding boxes around detected persons

⏱️ Time-Based Authorization
1. Defines allowed access hours (e.g., 9 AM – 5 PM)
2. Flags presence outside allowed time as intrusion

📸 Intruder Evidence Capture
1. Captures and stores intruder images
2. Saves images with timestamp in intruders/ folder

🗄️ Database Integration (SQLite)
1. Replaced CSV logging with SQLite database
2. Stores:
     timestamp
     status
     image path
3. Enables structured and scalable data handling

📧 Email Alert System
1. Sends real-time email alerts when intrusion is detected
2. Includes:
     timestamp
     intruder image attachment
3. Uses secure Gmail App Password authentication

🔐 User Authentication
1. Login system implemented using Flask-Login
2. Only authorized users can access dashboard

👥 Role-Based Access Control
1. Admin → full access
2. Viewer → read-only access
3. Route-level restrictions enforced

📊 Real-Time Dashboard
1. Built using Flask
2. Displays:
     live camera feed
     intrusion logs
     total intrusions
3. Auto-refresh every 5 seconds

🎨 Modern UI/UX
1. Responsive design using Bootstrap
2. Dark-themed professional dashboard
3. Clean layout with cards, navbar, and status indicators

⚠️ Error Handling
1. Handles failures in:
     camera access
     model loading
     database operations
     email sending
2. Prevents system crashes

🔔 IoT Hardware Integration
1. Arduino-based alert system
2. On intrusion:
     buzzer activates
     LED turns ON
3. Communication via serial (Python → Arduino)


🧰 Technologies Used

1. Programming → Python
2. AI/ML → YOLOv8 (Ultralytics)
3. Computer Vision → OpenCV
4. Web Framework → Flask
5. Authentication → Flask-Login
6. Database → SQLite
7. Email → Yagmail (SMTP)
8. IoT → Arduino UNO R4
9. Version Control → Git & GitHub
10. UI → Bootstrap


📂 Project Structure
AI_SECURITY_PROJECT/
│
├── detect.py              # AI detection + intrusion logic + alerts
├── dashboard.py           # Flask dashboard backend
├── database.py            # SQLite database operations
│
├── templates/
│   ├── index.html         # Dashboard UI
│   └── login.html         # Login page
│
├── intruders/             # Saved images (ignored)
├── intrusions.db          # Database (ignored)
│
├── .env                   # Email credentials (ignored)
├── .env.example           # Sample env file
├── .gitignore
├── README.md


▶️ Running the System
1. Start Detection (Backend + IoT)
python detect.py

This will:

start camera
detect humans
log intrusions to database
send email alerts
trigger Arduino buzzer & LED
2. Start Dashboard
python dashboard.py

Open in browser:

http://127.0.0.1:5000
🔑 Login Credentials
Admin:
username: admin
password: admin123

Viewer:
username: viewer
password: viewer123


🔄 System Workflow
1. Camera captures live video
2. YOLOv8 detects humans
3. Authorization logic checks access time
4. If intrusion detected:
     image saved
     database updated
     email alert sent
     Arduino triggered
5. Dashboard updates in real-time


📈 Expected Outcome
1. Real-time intrusion detection system
2. Automated alerting and logging
3. Secure monitoring dashboard
4. AI + IoT integrated solution


🌍 Applications
1. Smart campuses
2. Corporate offices
3. Industrial zones
4. Data centers
5. Smart city surveillance


🔮 Future Enhancements
1. Face recognition for authorized users
2. Multi-camera support
3. Mobile app notifications
4. Cloud deployment
5. Analytics dashboard (graphs)


🏁 Conclusion

This project demonstrates a complete AI-powered surveillance system integrating:

  1. Computer vision
  2. Web technologies
  3. Database systems
  4. IoT hardware

It provides a scalable foundation for intelligent security solutions in real-world environments.


🧠 Development Workflow
1. Feature-based development
2. Regular commits to GitHub
3. Incremental system improvements
4. CI/CD-inspired workflow
