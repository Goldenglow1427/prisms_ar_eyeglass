
import PIL.Image
from getting_model_info import ModelTester
from tools.MarkdownCreate import MDCreateModule

# Constant declaration
MODEL_NAME = "OCR Space"
STARTING_INDEX = 1
ENDING_INDEX = 8

assert 1 <= STARTING_INDEX <= ENDING_INDEX <= 8, "Invalid sample indexes are provided" # Check if the constant is within range.

md_record = MDCreateModule(MODEL_NAME)
tester = ModelTester()

filename_suffix = f"{STARTING_INDEX}{ENDING_INDEX}"
if STARTING_INDEX == 1 and ENDING_INDEX == 8:
    filename_suffix = "all"

try:
    for i in range(STARTING_INDEX, ENDING_INDEX+1):
        image_path = f"test/image_text_extract/data/sample_images/fig{i}.jpg"
        image_path_comp = f"test/image_text_extract/data/sample_images/fig{i}-compressed.jpg"
        sample_file = PIL.Image.open(image_path)

        response = tester.test_model(MODEL_NAME, sample_file, image_path_comp)

        print(f"Text {i} used {response[1]} seconds to generate")
        md_record.append(response[0])

        
except:
    with open(f"test/image_text_extract/output/{MODEL_NAME}_{filename_suffix}.md", "w", encoding="utf-8") as f:
        f.write(md_record.export())
else:
    with open(f"test/image_text_extract/output/{MODEL_NAME}_{filename_suffix}.md", "w", encoding="utf-8") as f:
        f.write(md_record.export())