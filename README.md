# ⏰ Python Voice Reminder App

A simple and powerful **Python Reminder Application** that allows users to set **multiple reminders interactively**.

The app alerts users using **voice (text-to-speech)**, **desktop notifications**, and **console messages**, ensuring you never miss important tasks.  
It also **saves reminders to a JSON file**, so your reminders can persist even after restarting the app.

---

## 🚀 Features

- 🔊 Voice reminders using **Text-to-Speech**
- 🔔 Desktop notification alerts
- ⏱ Set reminder time in **seconds, minutes, hours, or days**
- 📌 Add **multiple reminders continuously**
- 📋 View all reminders after adding them
- 💾 **Save reminders to a JSON file**
- 🔁 Load previously saved reminders automatically
- 💬 Console message alerts
- 🧠 Beginner-friendly Python project

---

## 🛠️ Tech Stack

- **Python**
- `pyttsx3` → Text-to-Speech library  
- `plyer` → Desktop notification library  
- `time` → For managing reminder delays  
- `threading` → For running multiple reminders simultaneously  
- `json` → For saving and loading reminders  
- `os` → For handling file operations  

---

## 📦 Installation

1. Make sure **Python** is installed on your system.

2. Install required libraries:

```bash
pip install pyttsx3 plyer
```

---

## ▶️ Usage

Run the Python script:

```bash
python reminder.py
```

Follow the instructions in the terminal:

1. Enter the **task you want to be reminded about**
2. Enter the **time value**
3. Choose the **time unit**
   - seconds
   - minutes
   - hours
   - days
4. Choose whether you want to **add another reminder**

You can continue adding reminders until you choose to exit.

All reminders are **automatically saved** and will be **loaded the next time the app runs**.

---

## 💻 Example

```
Welcome to your reminder app!

what should i remind you about : Drink water
Enter time span: 1
Enter unit(second/minutes/hours/days): minutes

Reminder set: Drink water after 1 minutes

Want to add another reminder(yes/no): yes

what should i remind you about : Stretch
Enter time span: 30
Enter unit(second/minutes/hours/days): seconds

Reminder set: Stretch after 30 seconds

Want to add another reminder(yes/no): no

Exitting App...

Reminders added:
Reminder set: Drink water after 1 minutes
Reminder set: Stretch after 30 seconds
```

When the time is completed, the app will alert you using:

- 🔊 Voice reminder
- 🔔 Desktop notification
- 💬 Console message

---

## 📂 Project Structure

```
voice-reminder-app
│
├── reminder.py
├── reminders.json
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
- Using **threads for multiple reminders**
- Working with **different time formats**
- Managing **lists to store reminders**
- Saving and loading data using **JSON**

---

## 📜 License

This project is open source and free to use.

---

⭐ If you like this project, consider giving it a star!
