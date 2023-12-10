from textual.widgets import Static, Button
from textual.app import ComposeResult
from .FormSubmit import *
from typing import Union

class Form(Static):

    def __init__(self, *components, form_id: str, classes: Union[str, None] = None) -> None:
        self.components = (*components, FormSubmit(label="Submit", classes=f"form-submit form-submit-{form_id}", id=f"form-submit-{form_id}"))
        
        self.style_classes = classes
        self.form_id = form_id
        super().__init__()

    def compose(self) -> ComposeResult:

        if self.style_classes:
            self.add_class(self.style_classes)
            self.add_class(f"form form-{self.form_id}")

        self.styles.layout = "vertical"
        return self.components