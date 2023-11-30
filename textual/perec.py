from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, OptionList, Button
from textual.reactive import reactive
from screens import WelcomeScreen, CreateTourScreen

class Perec(App):
    """A Textual app to manage constrained writing projects."""

    CSS_PATH = "perec.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ('escape', 'quit', 'Quit')
    ]   

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        """ Respond to selected options. """

        match event.option_id:
            case 'new_project':
                pass

            case "create_knights_tour":
                self.push_screen(CreateTourScreen())


    def on_mount(self) -> None:
        self.push_screen(WelcomeScreen())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit(self) -> None:
        """ Exit the app """
        self.exit()


if __name__ == "__main__":
    app = Perec()
    app.run()
