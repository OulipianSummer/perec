
from textual.widgets import Static, Button
from textual.app import ComposeResult
from textual.message import Message
from .Row import Row
from .Col import Col
from .Square import Square
from ...chess import *

class ChessBoard(Static):
    """ A widget that renders an interactive chessboard for knight's tours. """

    class Move(Message):
        """ Message indicating a move has been made. """

        def __init__(self, square: str) -> None:
            self.square = square
            super().__init__()

    class TourUpdate(Message):
        """A message indicating that the entire tour has been modified, and should be modeled elsewhere."""
        def __init__(self, tour: list) -> None:
            self.tour = tour
            super().__init__()

    def __init__(
        self, 
        board_size: int = 8, 
        show_ranks_and_files=True, 
        tour: None | list = None,
        mode: str = "select"
    ):
        self.board_size = board_size
        self.show_ranks_and_files = show_ranks_and_files
        self.tour = tour
        self.history = []
        self.mode = mode
        super().__init__()

    def on_button_pressed(self, event: Button.Pressed) -> None:     
        """ Respond to button presses."""

        if self.mode == 'select':

            # Ignore error buttons, presumed skipped
            if event.button.variant == 'error':
                return

            selected_move = event.button.id

            # Make the first move if one has not yet been made.
            if not self.tour:
                self.tour = []
                self.tour.append(selected_move)
                self.post_message(self.Move(selected_move))
                event.button.disabled = True
                return

            # Reject duplicate moves.
            if selected_move in self.tour:
                return
            
            last_move = self.tour[-1]

            # Validate the suggested move against the last one.
            if is_valid_move(last_move, selected_move):
                self.tour.append(selected_move)
                self.post_message(self.Move(selected_move))
                event.button.disabled = True

        if self.mode == "exclude":
            
            # Toggle a button to error if it isn't already.
            if event.button.variant!= 'error':
                event.button.variant = "error"

            # Toggle a button back to its original variant.
            else:
                if event.button.has_class('original-variant-primary'):
                    event.button.variant = 'primary'
                if event.button.has_class('original-variant-default'):
                    event.button.variant = 'default'

    def undo(self) -> None:
        """ Remove the last move from the tour, append it to the undo history, alert everyone the tour has changed.s """
        if len(self.tour) > 0:
            move = self.tour.pop()
            self.history.append(move)
            self.post_message(self.TourUpdate(self.tour))
            
            square = self.query_one(f"Square#{move}")
            
            if square:
                if square.disabled:
                    square.disabled = False

    def compose(self) -> ComposeResult:


        chessboard = []

        # Show ranks in a column.
        if self.show_ranks_and_files:
            ranks = []
            for i in range(self.board_size):
                rank = f"{self.board_size - i}"
                ranks.append(Static(rank,  id=f"chessboard-rank-{rank}", classes="chessboard-rank"))
            
            chessboard.append(Col(*ranks, classes="chessboard-ranks-container"))

        # Render the chess board squares.
        grid = []
        for i in range(self.board_size):
            row_buttons = []
            for j in range(self.board_size):
                id = index_to_chess_notation(i, j, self.board_size)
                variant = "primary" if (i + j) % 2 == 0 else "default"
                row_buttons.append(Square(f"", variant=variant, id=id, classes=f"original-variant-{variant}"))
            grid.append(Row(*row_buttons))

        # Show the chessboard files.
        if self.show_ranks_and_files:
            files = []
            for i in range(self.board_size):
                file = chr(ord('a') + i)
                files.append(Static(file, id=f"chessboard-file-{file}", classes=f"chessboard-file"))

            grid.append(Row(*files, classes="chessboard-files-container"))

        chessboard.append(Col(*grid))
        yield Row(*chessboard)
    