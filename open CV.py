import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')
cv2.circle(photo,(photo.shape[1] // 2, photo.shape[0] // 2), 200, (255, 255, 255), thickness=5)
cv2.ellipse(photo,(photo.shape[1] // 2, photo.shape[0] // 2), (70, 90), 0, 0, 180, (119, 201, 105), thickness=3)
cv2.ellipse(photo,(photo.shape[1] // 2, photo.shape[0] // 2), (50, 70), 0, 0, 180, (119, 201, 105), thickness=3)
cv2.line(photo,(200,250), (200, 200), (255, 0, 0), thickness=3)
cv2.line(photo,(180,250), (180, 200), (255, 0, 0), thickness=3)
cv2.line(photo,(300,250), (300, 200), (255, 0, 0), thickness=3)
cv2.line(photo,(320,250), (320, 200), (255, 0, 0), thickness=3)
cv2.line(photo,(180,200), (200, 200), (0, 0, 255), thickness=3)
cv2.line(photo,(300,200), (320, 200), (0, 0, 255), thickness=3)

logo_resized = cv2.resize(photo,(0, 0), fx=0.5, fy=0.5)
height, width = logo_resized.shape[:2]
gradient = np.zeros((height, width, 3), dtype='uint8')
for i in range(height):
    gradient[i, :, :] = i + (255 / height)
combined = cv2.addWeighted(gradient, 0.5, logo_resized, 0.5, 0)

cv2.imshow('Photo', photo)
cv2.waitKey(0)

