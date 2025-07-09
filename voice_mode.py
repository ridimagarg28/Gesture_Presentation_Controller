import pyautogui
import speech_recognition as sr

def run_voice_mode():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Voice mode active.")
    print("Say one of these commands: 'start', 'next', 'previous', 'end', or 'exit'")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                print("\n Listening for command...")
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print("Heard: {command}")

                if "start" in command:
                    pyautogui.press("f5")
                    print("🟢 Presentation started.")
                elif "next" in command:
                    pyautogui.press("right")
                    print("➡️ Moved to next slide.")
                elif "previous" in command:
                    pyautogui.press("left")
                    print("⬅️ Moved to previous slide.")
                elif "end" in command or "stop" in command:
                    pyautogui.press("esc")
                    print("🔴 Presentation ended.")
                elif "exit" in command:
                    print("👋 Exiting voice control mode.")
                    break
                else:
                    print("⚠️ Command not recognized. Try again.")

            except sr.WaitTimeoutError:
                print("Timeout. Please try again.")
            except sr.UnknownValueError:
                print("Couldn't understand. Speak clearly.")
            except Exception as e:
                print(f"Error: {e}")