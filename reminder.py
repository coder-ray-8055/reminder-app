import pyttsx3
import time

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
    speak(f"remender! {inp}")
    print(f"remender! {inp}")

if __name__ == "__main__":
    speak("Welcome to your reminder app!")
    set_reminder()

