!pip install pdf2image
from pdf2image import convert_from_path

!pip install poppler-utils
!sudo apt install poppler-utils poppler-data

pages = convert_from_path('6026810_E14_PRE_X_01_001_001_XX_01_001_X_XXX.pdf', 500)

for page in pages:
    page.save('6026810_E14_PRE_X_01_001_001_XX_01_001_X_XXX.jpg', 'JPEG')

# Python program to illustrate 
# template matching 
import cv2 
import numpy as np 

# Read the main image 
img_rgb = cv2.imread('6026810_E14_PRE_X_01_001_001_XX_01_001_X_XXX.jpg')

# Convert it to grayscale 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 

# Read the template 
template = cv2.imread('template.png',0) 

# Store width and heigth of template in w and h 
w, h = template.shape[::-1] 

# Perform match operations. 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 

# Specify a threshold 
threshold = 0.8

# Store the coordinates of matched area in a numpy array 
loc = np.where( res >= threshold) 

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 

# Show the final image with the matched area. 
cv2.imshow('Detected',img_rgb) 
