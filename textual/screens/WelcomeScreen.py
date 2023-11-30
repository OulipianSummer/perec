from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, OptionList
from textual.widgets.option_list import Option, Separator

class WelcomeScreen(Screen):
    """ The first screen users see when they use perec. """

    def compose(self) -> ComposeResult:
        yield Header()

        welcome_options = [
            Option("New Project", id="new_project"),
            Option("Load Project", id="load_project"),
            Separator(),
            Option("Create Knight's Tour", id="create_knights_tour"), 
            Separator(),
            Option("Create Latin Square", id="create_latin_square"),
            Option("Create Graeco-Latin Square", id="create_graeco_latin_square"),
        ];
        yield OptionList(*welcome_options)

        yield Footer()
