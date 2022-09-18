import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

previous_time = 0
current_time = 0


while True:
    ret, frame = cap.read()
    img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for idx, lm in enumerate(hand_landmarks.landmark):
                height, width, channel = frame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)

                if idx == 0:
                    cv.circle(frame, (cx, cy), 25, (255, 0, 255), cv.FILLED)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), thickness=3)


    cv.imshow('Image', frame)

    if cv.waitKey(1) == ord('q'):
        break 