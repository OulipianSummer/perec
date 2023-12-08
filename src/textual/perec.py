from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, OptionList, Button
from textual.reactive import reactive
from .screens import WelcomeScreen, CreateTourScreen

class TuiOperations:
    NEW_TOUR = 'tui.new_tour'

class Perec(App):
    """A Textual app to manage constrained writing projects."""

    CSS_PATH = "perec.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ('escape', 'quit', 'Quit')
    ]   

    def __init__(self, operation: str | None, arguments: object | None) -> None:

        self.operation = operation    
        self.arguments = arguments

        super().__init__()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        """ Respond to selected options. """

        match event.option_id:
            case 'new_project':
                pass

            case "create_knights_tour":
                self.push_screen(CreateTourScreen())


    def on_mount(self) -> None:
        
        match(self.operation):

            case TuiOperations.NEW_TOUR:
                board_size = 8;

                if self.arguments['<size>']:
                    board_size = int(self.arguments['<size>'])
                self.push_screen(CreateTourScreen(board_size = board_size))

            case _:
                self.push_screen(WelcomeScreen())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit(self) -> None:
        """ Exit the app """
        self.exit()


def launch_tui(operation: str | None, arguments: object | None):
    """ Launches the TUI with arguments so it can integrate with the larger CLI application. """
    app = Perec(operation, arguments)
    app.run()

if __name__ == "__main__":
    launch_tui()