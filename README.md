# ⏰ Python Voice Reminder App

A simple Python reminder application that reminds users about tasks after a specified time. The app uses **text-to-speech** to speak the reminder and also sends a **system notification** so the user never misses important tasks.

---

## 🚀 Features

* 🔊 Text-to-speech reminder using Python
* 🔔 Desktop notification alert
* ⏱ Set reminder time in seconds
* 💬 Voice, notification, and console message alerts
* 🧠 Simple and beginner-friendly Python project

---

## 🛠️ Tech Stack

* Python
* pyttsx3 (Text-to-Speech Library)
* plyer (Desktop Notification)

---

## 📦 Installation

1. Make sure Python is installed on your system.

2. Install the required dependencies:

```bash
pip install pyttsx3 plyer
```

---

## ▶️ Usage

Run the Python script:

```bash
python reminder.py
```

Then follow the instructions:

1. Enter what you want to be reminded about
2. Enter reminder time in seconds
3. After the timer ends, the app will notify you using:

* 🔊 Voice reminder
* 🔔 Desktop notification
* 💬 Console message

---

## 💻 Example

```
Welcome to your reminder app!

What should I remind you about: Drink water
After how many seconds you want to be reminded: 10

Drink water set for 10 seconds...

🔔 Reminder! Drink water
```

---

## 📂 Project Structure

```
reminder-app
│
├── reminder.py
└── README.md
```

---

## 🎯 Purpose

This project was built while learning Python to understand:

* Python functions
* User input handling
* Time delay using `time.sleep()`
* Text-to-speech integration
* Desktop notification integration

---

## 📜 License

This project is open source and free to use.
