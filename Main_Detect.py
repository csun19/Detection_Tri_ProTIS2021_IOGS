# Main program of color&shape detection
# Chenyu SUN
# Version 29 Mar. 2021
from shapedetector import ShapeDetector
import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)

while(True):
    # Get the frames of camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Get the width and height of camera display window
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # The coordinates of the vertex of the lower left corner of the selected rectangle
    rect_x = int(1/4*width)
    rect_y = int(1/4*height)
    # The width and height of the selected rectangle
    rect_w = int(1/2*width)
    rect_h = int(1/2*height)

    # Gaussian Filter
    gau = cv2.GaussianBlur(frame, (5, 5), 1.5)

    # Convert image to HSV color space
    hsv = cv2.cvtColor(gau, cv2.COLOR_BGR2HSV)

    # Using the mask to suppress the background area (conveyor belt)
    # The H paramter 10-180 due to the color in the range of RGB and Yellow
    hsvNBl = np.array([10, 43, 46])         # No-Background lower threshold
    hsvNBu = np.array([180, 255, 255])      # No-Background upper threshold
    maskNB = cv2.inRange(hsv, hsvNBl, hsvNBu)
    rect = np.zeros(frame.shape[:2], dtype="uint8")
    rect[rect_y:(rect_y+rect_h),rect_x:(rect_x+rect_w)] = 255
    maskNB = cv2.bitwise_and(maskNB,rect)  
    
    # Binary
    binary = cv2.threshold(maskNB, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)[1]
    
    # Open morphology
    # kernel = np.ones((5,5), np.uint8)
    # morph = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations = 3)

    # Close morphology
    kernel = np.ones((5,5), np.uint8)
    morph = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations = 3)
    
    # searching the contours
    contours, _ = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    try:
        # Calculate the center of the contours
        cnt = contours[0]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        # Shape detect
        sd = ShapeDetector()
        shape = sd.detect(cnt)
        
        # Create a mask for color detecting
        mask = np.zeros(frame.shape[:2], dtype="uint8")
        cv2.drawContours(mask, cnt, -1, 255, -1)
        # Calculate the hsv histogram in the mask
        hist_mask = cv2.calcHist([hsv], [0], mask, [180], [0,180])
        arrayH = np.where(hist_mask == np.max(hist_mask))

        # Find the mean value of H component of hsv in the mask
        H = np.mean(arrayH[0])
        if H > 10 and H < 34: color = "Jaune"
        elif H > 34 and H < 112: color = "Vert"
        elif H > 112 and H < 140: color = "Bleu"
        elif H > 156 and H < 180: color = "Rouge"
        else: color = "Couleur"
        
        text = "{} {}".format(shape, color)
        cv2.putText(frame, text, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    except: pass
    

    # Display the frame with the color and shape
    cv2.rectangle(frame, (rect_x, rect_y), (rect_x+rect_w, rect_y+rect_h), (0, 255, 0), 2)
    cv2.drawContours(frame, contours, -1, (255, 255, 255), 3)
    cv2.imshow('Couleur&Forme', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'echap' to quit
        break

                
cap.release()
cv2.destroyAllWindows()
