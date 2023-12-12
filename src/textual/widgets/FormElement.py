from textual.widgets import Static, Label, Input
from textual.app import ComposeResult
from typing import Union
from ..widgets import Row, Col
from ...lib import text_to_var

class FormElement(Static):
    """ An utility class for for bundling labels and inputs within a form. """

    def __init__(
          self,
          label: str,
          type: str, 
          placeholder: str, 
          required: bool = False, 
          classes: Union[str, None] = None,
          element_name: Union[str, None] = None,
          max_length: Union[int, None] = 255
        ) -> None:
        self.label = label
        self.type = type
        self.placeholder = placeholder
        self.required = required
        self.style_classes = classes
        self.max_length = max_length

        if not element_name:
            self.element_name = text_to_var(name)
        else:
            self.element_name = element_name

        
        super().__init__()

    def compose(self) -> ComposeResult:

        if self.style_classes:
            self.add_class(self.style_classes)
            self.add_class(f"form-element form-element-{self.element_name}")

        label =  [Label(self.label, id = f"label-{self.element_name}")] 

        if self.required:
            label.append(Static("*", classes="required"))
        
        label_group = Row(*label)
        
        input = [
            Input(
                type = self.type, 
                placeholder = self.placeholder, 
                id = f"input-{self.element_name}",
                max_length = self.max_length,
                valid_empty = not self.required
            )
        ]
        input_group = Row(*input)

        yield Col(label_group, input_group)
