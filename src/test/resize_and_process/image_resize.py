
# For taking input from camera
import cv2
import numpy as np
from PIL import Image

# For parsing the text from image.
import pytesseract;


def cv2_to_pil(img):
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


# cam = cv2.VideoCapture(0)
# ret, img = cam.read()

# cv2.imshow("Camera", img)
# cv2.waitKey(0)

# pil_image = cv2_to_pil(img);
pil_image = Image.open("image_name.jpg")

pil_image = pil_image.resize((128, 128))
pil_image = pil_image.convert('1')

pil_image.save("image_name.jpg")

# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# text = pytesseract.image_to_string(pil_image)

# print(text)
