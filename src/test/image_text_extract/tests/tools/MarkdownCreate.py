
class MDCreateModule:
    """
    A module that can be used to generate an Markdown file.
    """

    ret: str
    index: int

    def __init__(self, modelName: str):
        """
        Initialize the markdown file with certain module as title.

        Parameters
        -----------------
        `modelName`: name of the model used.
        """
        self.ret = f"# AI Model: {modelName} Usage Report\n"
        self.index = 0
        return
    
    def append(self, output: str) -> None:
        """
        Append the text to the end of this file.
        """
        self.index += 1
        self.ret += f"## Output {self.index}\n"
        self.ret += output
        self.ret += "\n"

    def export(self) -> str:
        """
        Export the string in this module as a string file.
        """
        return self.ret
