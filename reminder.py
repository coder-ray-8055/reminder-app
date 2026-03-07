import pyttsx3
import time
from plyer import notification
import threading

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


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

        speak("After how many seconds?")
        inp2 = int(input("After how many seconds : "))

        print(f"{inp} set for {inp2} seconds...")

        t = threading.Thread(target=reminder_task, args=(inp, inp2))
        t.start()

        again = input("Want to add another reminder(yes/no): ").lower()

        if again != "yes":
            print("Exitting App...")
            break


if __name__ == "__main__":
    speak("Welcome to your reminder app!")
    set_reminder()
