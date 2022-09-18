import numpy as np
import cv2

def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotation_matrix, dimensions)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=.5, fy=.5)  

    image[:height//2,:width//2] = rotate(smaller_frame, 90)
    image[:height//2,width//2:] = rotate(smaller_frame, -90)
    image[height//2:,width//2:] = rotate(smaller_frame, 180)
    image[height//2:,:width//2] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()