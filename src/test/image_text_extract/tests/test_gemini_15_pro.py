
import PIL.Image
import os
import google.generativeai as genai
from tools.TimeMeasure import TimeMeasureModule
from tools.MarkdownCreate import MDCreateModule

timer = TimeMeasureModule()
md_record = MDCreateModule("Gemini 1.5 Pro")

# Setup the basics
genai.configure(api_key="AIzaSyATjswh7u94DaZzO68WSbLrK2UwHLuTQMQ")

# Use the model to get responses.
model = genai.GenerativeModel("gemini-1.5-pro")
prompt = "Parse the text that appears in this image. Don't contain extra text."

try:
    for i in range(3, 5):
        image_path = f"test/image_text_extract/data/sample_images/fig{i}.jpg"
        sample_file = PIL.Image.open(image_path)

        timer.begin_record()
        response = model.generate_content([prompt, sample_file])
        print(f"Text {i} used {timer.get_time()} seconds to generate")
        md_record.append(response.text)
except:
    with open("test/image_text_extract/output/gemini_15_pro_34.md", "w") as f:
        f.write(md_record.export())
else:
    with open("test/image_text_extract/output/gemini_15_pro_34.md", "w") as f:
        f.write(md_record.export())
