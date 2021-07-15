import cv2 
ipv4url='http://10.145.145.71:8080'
cam = f'{ipv4url}/video'
cap = cv2.VideoCapture(cam)

while True:
    ret, frame = cap.read()
    farme = cv2.resize(frame, (600,600))
    cv2.imshow("Mobile Camera", farme)
    if cv2.waitKey(1) ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()