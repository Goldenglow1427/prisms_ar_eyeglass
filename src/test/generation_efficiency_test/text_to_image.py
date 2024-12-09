
import requests

image_url = "https://image.pollinations.ai/prompt/A male student is doing physics research.";

img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
