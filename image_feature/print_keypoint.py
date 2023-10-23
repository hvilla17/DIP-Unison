# File: print_keypoint.py

# prints a keypoint
def print_keypoint(kp):
    print(f'angle: {kp.angle}, class_id: {kp.class_id}, octave: {kp.octave}, \
pt: {kp.pt}, response: {kp.response}, size: {kp.size}')
