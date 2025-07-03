import cv2
import mediapipe as mp
import pyautogui
import time

from gesture_utils import get_landmark_positions, fingers_up
from draw_utils import init_canvas, draw_on_canvas

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

canvas = None
draw_color = (0, 0, 255)
brush_thickness = 5
drawing = False
prev_point = None

prev_gesture = None
last_trigger_time = 0
cooldown_duration = 1.5

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if canvas is None:
        canvas = init_canvas(frame.shape)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = get_landmark_positions(hand_landmarks, frame.shape)
            if landmarks:
                finger_status = fingers_up(landmarks)
                current_time = time.time()
                gesture = None
    
                if finger_status == [1,1,1,1,1]:
                    gesture = "Start Presentation"
                elif finger_status == [0, 0, 0, 0, 0]:
                    gesture = "End Presentation"
                elif finger_status == [0, 1, 1, 0, 0]:
                    gesture = "Next Slide"
                elif finger_status == [0, 0, 1, 1, 0]:
                    gesture = "Previous Slide"

                if finger_status == [0, 1, 0, 0, 0]:
                    drawing = True
                    x, y = landmarks[8][1], landmarks[8][2]
                    curr_point = (x, y)
                    canvas = draw_on_canvas(canvas, prev_point, curr_point, draw_color, brush_thickness)
                    prev_point = curr_point
                else:
                    drawing = False
                    prev_point = None

                
                if gesture and (gesture != prev_gesture or current_time - last_trigger_time > cooldown_duration):
                    if gesture == "Start Presentation":
                        pyautogui.press("f5")
                    elif gesture == "End Presentation":
                        pyautogui.press("esc")
                    elif gesture == "Next Slide":
                        pyautogui.press("right")
                    elif gesture == "Previous Slide":
                        pyautogui.press("left")

                    print("Gesture Detected:", gesture)
                    prev_gesture = gesture
                    last_trigger_time = current_time

    frame = cv2.addWeighted(frame, 1, canvas, 0.7, 0)
                
    cv2.imshow("Gesture Presentation Controller", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()