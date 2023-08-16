import cv2

cap = cv2.VideoCapture(0)

while True:
    rt,video = cap.read()

    cv2.imshow('frame',video)
    cv2.waitKey(1)
cv2.destroyAllWindows()
