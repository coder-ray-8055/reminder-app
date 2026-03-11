import pyttsx3
import time
from plyer import notification
import threading
import json
import os

engine = pyttsx3.init()

reminders= []
FILE = "reminders.json"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def converted_to_sec(inp2 , unit):
    if unit in ["second" , "seconds"]:
        return inp2
    elif  unit in ["minute" , "minutes"]:
        return inp2*60
    elif  unit in ["hour" , "hours"]:
        return inp2*3600
    elif  unit in ["day" , "days"]:
        return inp2*86400
    else:
        return None
    
def save_reminders():
    with open(FILE , "w") as f:
        json.dump(reminders , f)

def load_reminders():
    global reminders
    if os.path.exists(FILE):
        with open(FILE , "r") as f:
            reminders = json.load(f)

def reminder_task(inp, inp2):

    time.sleep(inp2)

    speak(f"Reminder! {inp}")
    print(f"Reminder! {inp}")

    notification.notify(
        title="Reminder",
        message=f"Time's up! {inp}",
        timeout=5
    )


def set_reminder():

    while True:

        speak("what should i remind you about?")
        inp = input("what should i remind you about : ")

        speak("Enter time span")
        try:
            inp2 = int(input("Enter time span: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        unit = input("Enter unit(second/minutes/hours/days): ").lower()

        seconds = converted_to_sec(inp2 , unit)

        if seconds is None:
            print("Invalid unit, using your input by default")
            continue

        print(f"Reminder set: {inp} after {inp2} {unit}")
        speak(f"Reminder set for {inp} after {inp2} {unit}")
        reminders.append(f"Reminder set: {inp} after {inp2} {unit}")

        save_reminders()

        t = threading.Thread(target=reminder_task, args=(inp, seconds))
        t.start()

        again = input("Want to add another reminder(yes/no): ").lower()

        if again != "yes":
            print("Exitting App...")

            print("Reminders added: ")
            for r in reminders:
                print(r)
            break


if __name__ == "__main__":
    load_reminders()

    if reminders:
        print("Previously saved reminders:")
        for r in reminders:
            print(r)

    speak("Welcome to your reminder app!")
    set_reminder()
