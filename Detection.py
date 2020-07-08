

import cv2
import numpy as np
import pytesseract
minArea = 500
color = (0, 255, 0)
imgName = "download.jpg"
numberPlateCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")
img = cv2.imread("images/" + imgName)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

licensePlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in licensePlates:
    area = w * h
    if area > minArea:
        imgROI = img[y:y + h, x-5:x + w]

img=cv2.cvtColor(imgROI,cv2.COLOR_BGR2RGB)
pytesseract.pytesseract.tesseract_cmd='D:\\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string(img))
cv2.imshow("image", imgROI)
cv2.waitKey(0)

