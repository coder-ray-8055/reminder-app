# ⏰ Python Voice Reminder App

A simple and powerful **Python Reminder Application** that allows users to set **multiple reminders** for different tasks.  
The app gives alerts using **voice (text-to-speech)**, **desktop notifications**, and **console messages** so you never miss important tasks.

---

## 🚀 Features

- 🔊 Voice reminder using Text-to-Speech
- 🔔 Desktop notification alerts
- ⏱ Set reminder time in **seconds, minutes, hours, or days**
- 📌 Support for **multiple reminders**
- 💬 Console message alert
- 🧠 Beginner-friendly Python project

---

## 🛠️ Tech Stack

- **Python**
- `pyttsx3` – Text-to-Speech library
- `plyer` – Desktop notification library
- `time` – For managing reminder delays

---

## 📦 Installation

1. Make sure **Python** is installed on your system.

2. Install the required libraries:

```bash
pip install pyttsx3 plyer
```

---

## ▶️ Usage

Run the Python script:

```bash
python reminder.py
```

Then follow the instructions in the terminal:

1. Enter how many reminders you want to set
2. Enter the **task name**
3. Enter the **time value**
4. Choose the **time format**:
   - Seconds
   - Minutes
   - Hours
   - Days

After the timer ends, the app will alert you using:

- 🔊 Voice reminder
- 🔔 Desktop notification
- 💬 Console message

---

## 💻 Example

```
Welcome to your Reminder App!

How many reminders do you want to set: 2

Reminder 1
Enter task: Drink water
Enter time: 1
Choose format (seconds/minutes/hours/days): minutes

Reminder 2
Enter task: Stretch
Enter time: 30
Choose format (seconds/minutes/hours/days): seconds

Reminders set successfully!

🔔 Reminder! Drink water
🔔 Reminder! Stretch
```

---

## 📂 Project Structure

```
voice-reminder-app
│
├── reminder.py
└── README.md
```

---

## 🎯 Purpose

This project was built while learning Python to understand:

- Python functions
- User input handling
- Time delay using `time.sleep()`
- Text-to-Speech integration
- Desktop notification integration
- Handling **multiple reminders**
- Working with **different time formats (seconds, minutes, hours, days)**

---

## 📜 License

This project is open source and free to use.
