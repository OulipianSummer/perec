from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Input, Label
from ..widgets import Form, FormElement

class CreateProjectScreen(Screen):

    BINDINGS = [
        ('b', 'app.pop_screen', 'Back'),
    ]
    
    def compose(self) -> None:

        form_id = "create_project_form"

        form = [            
            FormElement(
                element_name = 'Project Name',
                type = 'text',
                placeholder = 'My Awesome Project',
                required = True,
            ),
            FormElement(
                element_name = 'Description',
                type = 'text',
                placeholder = 'This project is going to be so cool'
            ),
            FormElement(
                element_name = 'Size',
                type = 'integer',
                placeholder = 'Enter a number between 5 and 10, excluding 6',
                required = True,
                max_length =  2
            )
        ]

        yield Header()
        
        yield Form(
            form_id = "create_project_form",
            *form
        )

        yield Footer()