
import requests;
import time; # Measure the execution time to generate each image.

class TTMModule:
    
    def __init__(self):
        return
    
    def generate_image(self, description: str) -> float:
        image_url = "https://image.pollinations.ai/prompt/" + description;

        start_time = time.time()

        img_data = requests.get(image_url).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)

        end_time = time.time()

        return end_time - start_time
