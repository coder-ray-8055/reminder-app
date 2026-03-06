import pyttsx3
import time
from plyer import notification

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)

def set_reminder():
    speak("what should i remind you about?")
    inp = input("what should i remind you about : ")

    speak("After how many second you want to reminded?")
    inp2 = int(input("After how many seconds you want to reminded : "))

    speak(f"{inp} set for {inp2} seconds")
    print(f"{inp} set for {inp2} seconds...")

    time.sleep(inp2)
    speak(f"reminder! {inp}")
    print(f"reminder! {inp}")

    notification.notify(
        title = "Reminder",
        message = f"Time's up! {inp}...",
        timeout = 5
    )

if __name__ == "__main__":
    speak("Welcome to your reminder app!")
    set_reminder()

