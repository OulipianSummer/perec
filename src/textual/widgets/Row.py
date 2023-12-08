
from textual.widgets import Static
from textual.app import ComposeResult

class Row(Static):

    def __init__(self, *components, classes = None):
        self.components = components
        self.style_classes = classes
        super().__init__()

    def compose(self) -> ComposeResult:

        if self.style_classes:
            self.add_class(self.style_classes)

        self.styles.layout = "horizontal"
        return self.components