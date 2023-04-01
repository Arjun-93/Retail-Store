import win32com.client as wincom
speak = wincom.Dispatch("SAPI.spVoice")

if __name__ == '__main__':
    print("\nWelcome to RoboSpeaker 1.1 Created by Arjun")
    while True:
        text = input("Enter what you want me to pronounce: ")
        if text == "q":
            speak.Speak("Bye Bye Friend")
            break
        speak.Speak(text)
