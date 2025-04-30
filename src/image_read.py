
from PIL import Image

class ImageReader:

    output_path: str
    debug_mode: bool

    def __init__(self, output_path: str, debug_mode: bool=False):
        self.output_path = output_path
        self.debug_mode = debug_mode

    
    def convert_jpg2bmp(self, image_path: str) -> int:
        try:
            img = Image.open(image_path).convert("L")

            resized_image = img.resize((128, 64))

            resized_image.save(self.output_path, "BMP")
            if self.debug_mode:
                print(f"Image successfully converted and saved to {image_path}")
        except FileNotFoundError:
            print(f"Error: image not found at {image_path}")
            return 0
        except Exception as e:
            print(f"An error occured: {e}")