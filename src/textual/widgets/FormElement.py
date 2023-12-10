from textual.widgets import Static
from textual.app import ComposeResult
from typing import Union

class FormElement(Static):

    def __init__(self, *components, element_id: str, required: bool = False, classes: Union[str, None] = None) -> None:
        self.components = components
        self.style_classes = classes
        self.element_id = element_id
        super().__init__()

    def compose(self) -> ComposeResult:

        if self.style_classes:
            self.add_class(self.style_classes)
            self.add_class("form-element")

        return self.components