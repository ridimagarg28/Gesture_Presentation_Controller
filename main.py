from gesture_mode import run_gesture_mode
from voice_mode import run_voice_mode

def main():
    print("\n🎮 Control Options:")
    print("1. Gesture Mode")
    print("2. Voice Mode")
    
    mode = input("Choose control mode ('gesture' or 'voice'): ").strip().lower()

    if mode == "gesture":
        run_gesture_mode()
    elif mode == "voice":
        run_voice_mode()
    else:
        print("❌ Invalid input. Please run the program again and enter 'gesture' or 'voice'.")

if __name__ == "__main__":
    main()
