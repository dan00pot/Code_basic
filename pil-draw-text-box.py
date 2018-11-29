from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
cap = cv2.VideoCapture('0.png') 
while cap.isOpened(): # True:
    ret, img = cap.read()
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 15)
	# draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0),"con cá",(255,255,255),font=font)
    draw.rectangle(((0, 00), (24, 24)), fill=(0,0,0,127))
    img = np.array(img_pil)
    cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()