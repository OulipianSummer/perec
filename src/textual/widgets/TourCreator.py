
from textual.widgets import Static
from textual.app import ComposeResult
from .ChessBoard import ChessBoard

class TourCreator(Static):

    def __init__(self, board_size: int | None) -> None:

        if board_size:
            self.board_size = board_size
        else:
            self.board_size = 8

        super().__init__()

    tour = []

    def on_chess_board_move(self, move: ChessBoard.Move):
        """ Respond to chessboard moves. """
        self.tour.append(move.square)

    def compose(self) -> ComposeResult:
        yield ChessBoard(board_size=self.board_size)