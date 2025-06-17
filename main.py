import numpy as np
import cv2
import imutils
import datetime
import os

gun_cascade = cv2.CascadeClassifier('cascade.xml')

url = "http://100.76.129.112:8080/video"
camera = cv2.VideoCapture(url)
first_frame = None

save_dir = "detected_frames"
os.makedirs(save_dir, exist_ok=True)

frame_count = 0
while True:
    ret, frame = camera.read()
    if not ret or frame is None:
        print("Failed to grab frame from IP webcam. Check the IP address and that the app is running.")
        break
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray,
                                       1.3,5,
                                       minSize=(1000, 100))
    gun_exists = False
    if len(gun) > 0:
        gun_exists = True
        for (x, y, w, h) in gun:
            frame = cv2.rectangle(frame,
                                   (x, y), 
                                   (x + w, y + h), 
                                   (255,0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(save_dir, f"gun_detected_{timestamp}_{frame_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Gun detected! Frame saved as {filename}")
    else:
        print("No gun detected")
    frame_count += 1
    
camera.release()
