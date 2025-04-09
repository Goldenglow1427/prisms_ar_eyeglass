
# For taking input from camera
import cv2
import numpy as np
from PIL import Image

# For parsing the text from image.
import pytesseract;


def cv2_to_pil(img):
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

camera = cv2.VideoCapture(0)
while True:
    ret, img = camera.read()

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) == ord('Q'):
        break

    if cv2.waitKey(1) == ord('C'):
        print("Text parse request received.")
        
        pil_image = cv2_to_pil(img)
        text = pytesseract.image_to_string(pil_image)
        print(text)

        print("Text parse request done.")


camera.release()
cv2.destroyAllWindows()
