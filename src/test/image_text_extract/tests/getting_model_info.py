
import requests
import google.generativeai as genai
from tools.TimeMeasure import TimeMeasureModule

class ModelTester:

    timer: TimeMeasureModule

    def __init__(self):
        self.timer = TimeMeasureModule()
        return
    
    
    def test_model(self, model_name: str, image, img_path=""):
        if model_name == "Sample Model":
            return self.test_sample_model(image)
        
        if model_name.find("Gemini") >= 0 and model_name.upper().find("PRO") >= 0:
            return self.test_gemini_15_pro(image)
        
        if model_name.find("OCR") >= 0 and model_name.find("Space") >= 0:
            return self.test_ocr_space(img_path)
        
        return "Custom Error: Model name not valid or not set up.", 0.0
    

    def test_sample_model(self, image):
        return "Text parsed", 10.2
    
    
    def test_gemini_15_pro(self, image):
        genai.configure(api_key="AIzaSyATjswh7u94DaZzO68WSbLrK2UwHLuTQMQ")

        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = "Parse the text that appears in this image. Don't contain extra text."

        self.timer.begin_record()
        response = model.generate_content([prompt, image])
        return response.text, self.timer.get_time()
    

    def test_ocr_space(self, image_path):
        payload = {
            'isOverlayRequired': False,
            'apikey': 'K88826155288957',
            'language': 'eng',
            'OCREngine': 2
        }
        filename = image_path

        self.timer.begin_record()

        with open(filename, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                            files={filename: f},
                            data=payload,
                            )
            
        result = r.content.decode()
        index_0 = result.find("ParsedText") + 13
        index_1 = result.find("ErrorMessage") - 3
        result = result[index_0:index_1].replace("\\n", "\n")
                
        return result, self.timer.get_time()

