# ⏰ Python Voice Reminder App

A simple Python reminder application that allows users to set **multiple reminders** for different tasks. The app uses **text-to-speech** to speak the reminder and also sends a **desktop notification**, ensuring you never miss important tasks.

---

## 🚀 Features

* 🔊 Text-to-speech reminder using Python
* 🔔 Desktop notification alert
* ⏱ Set reminder time in seconds
* 📌 Multiple reminders support
* 💬 Voice, notification, and console message alerts
* 🧠 Simple and beginner-friendly Python project

---

## 🛠️ Tech Stack

* Python
* `pyttsx3` – Text-to-Speech Library
* `plyer` – Desktop Notification Library

---

## 📦 Installation

1. Make sure **Python** is installed on your system.

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

1. Enter the task you want to be reminded about
2. Enter the reminder time in seconds
3. You can add **multiple reminders**
4. After the timer ends, the app will notify you using:

* 🔊 Voice reminder
* 🔔 Desktop notification
* 💬 Console message

---

## 💻 Example

```
Welcome to your reminder app!

How many reminders you want to set: 2

Enter reminder 1 task: Drink water
Enter time in seconds: 10

Enter reminder 2 task: Stretch
Enter time in seconds: 20

Reminders set successfully!

🔔 Reminder! Drink water
🔔 Reminder! Stretch
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
* Handling multiple reminders using loops

---

## 📜 License

This project is open source and free to use.
