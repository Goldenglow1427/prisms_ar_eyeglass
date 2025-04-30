
from image_read import ImageReader

# Main program.
img_reader = ImageReader("src/image/output.bmp")

img_reader.convert_jpg2bmp("src/image/input.jpg")
