
from tools.MarkdownCreate import MDCreateModule

md_file = MDCreateModule("ChatGPT 4.0")

md_file.append("qwe")

md_file.append("asd")

with open("test/image_text_extract/output/test_output.md", "w") as f:
    f.write(md_file.export())
