import os 
import cv2
import time
cap = cv2.VideoCapture(0)

num = 0
for i in range(10):
    ret,image = cap.read()
    time.sleep(3)
    path = os.path.join('images', f'image{num}.jpg')
    cv2.imwrite(path,image)
    num += 1
    cv2.imshow('frame',image)
    cv2.waitKey(1)
cv2.destroyAllWindows()