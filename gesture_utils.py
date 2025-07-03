import math

def get_landmark_positions(hand_landmarks, frame_shape):
    height, width = frame_shape[:2]
    landmarks = []

    for id, lm in enumerate(hand_landmarks.landmark):
        cx, cy = int(lm.x * width), int(lm.y * height) #Mediapipe gives landmarks as relative coordinates (0.0, 1.0)
        landmarks.append((id, cx, cy))
    return landmarks

def fingers_up(landmarks):
    fingers = []

    #Thumb (check x movement instead of y because its sideways)
    if landmarks[4][1] < landmarks[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    for tip_id in [8, 12, 16, 20]:
        fingers.append(1 if landmarks[tip_id][2] < landmarks[tip_id - 2][2] else 0)

    return fingers

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)