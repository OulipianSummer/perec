from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Input, Label
from ..widgets import Form, FormElement

class CreateProjectScreen(Screen):
    
    def compose(self) -> None:

        form_id = "create_project_form"

        form = [            
            FormElement(
                Label("Project Name"),
                Input(placeholder="My Awesome Project"),
                element_id = "project_name",
            ),
            FormElement(
                Label("Description"),
                Input(placeholder="This project is going to be so cool"),
                element_id = "project_description",
            ),
            FormElement(
                Label("Size"),
                Input(type="integer", placeholder="A number from 5 to 10"),
                element_id = "project_size"
            )
        ]

        yield Header()
        
        yield Form(
            form_id = "create_project_form",
            *form
        )

        yield Footer()