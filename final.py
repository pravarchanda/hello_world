import cv2
import numpy as np
import imutils
import subprocess
image = cv2.imread("aggregate.png") 
blur = cv2.blur(image,(3,3))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blur, "This one!", (230, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
val = 0
bottom = blur
height,width = blur.shape[:2]
for angle in np.arange(0, height/10, 1):
	cropped = blur[1:height-1,1:width-1]
	resized = cv2.resize(cropped,(width,height))
	blur = resized
	ball = blur[:,:]
	blank = np.zeros((height*2,width,3), np.uint8)
	blank[:height,:] = blur[:,:]
	blank[height:height*2,:] = bottom[:,:]
	cv2.imwrite("/home/pravar/opencvpics/"+str(val).zfill(3)+".jpeg",blank)
	val=val+1