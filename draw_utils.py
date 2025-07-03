import numpy as np
import cv2

def init_canvas(frame_shape):
    return np.zeros(frame_shape, dtype=np.uint8)

def draw_on_canvas(canvas, prev_point, curr_point, color=(0, 0, 255), thickness=5):
    if prev_point is not None and curr_point is not None:
        cv2.line(canvas, prev_point, curr_point, color, thickness)
    return canvas