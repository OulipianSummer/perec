
from widgets import TourCreator, ChessBoard
from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer

class CreateTourScreen(Screen):
    """ A screen used for creating knight's tours. """

    BINDINGS = [
        ('b', 'app.pop_screen', 'Back'),
        ("x", "toggle_exclude_chessboard_mode", "Exclude Mode"),
        ("s", "toggle_select_chessboard_mode", "Select Mode"),
        ("ctrl+z", "undo", "Undo"),
    ]

    def action_toggle_exclude_chessboard_mode(self) -> None:
        """ Toggle the chessboard mode to exclude squares """
        chessboard = self.query_one(ChessBoard)

        if chessboard:
            chessboard.mode = "exclude"

    def action_toggle_select_chessboard_mode(self) -> None:
        """ Toggle the chessboard mode to select squares """
        chessboard = self.query_one(ChessBoard)

        if chessboard:
            chessboard.mode = "select"
    
    def action_undo(self) -> None:
        chessboard = self.query_one(ChessBoard)

        if chessboard:
            chessboard.undo()

    def compose(self) -> ComposeResult:
        yield Header()
        yield TourCreator() 
        yield Footer()