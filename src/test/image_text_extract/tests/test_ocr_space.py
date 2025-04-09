
import requests

payload = {
    'isOverlayRequired': False,
    'apikey': 'K88826155288957',
    'language': 'eng',
    'OCREngine': 2
}

filename = "test/image_text_extract/data/sample_images/fig1-compressed.jpg"

with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image',
                      files={filename: f},
                      data=payload,
                      )
    
result = r.content.decode()

index_0 = result.find("ParsedText") + 13
index_1 = result.find("ErrorMessage") - 3
result = result[index_0:index_1].replace("\\n", "\n").replace("\\\"", "\"")

with open("test/image_text_extract/output/test_ocr_space.md", "w") as f:
    f.write(result)
