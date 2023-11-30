
from textual.widgets import Static
from textual.app import ComposeResult
from .ChessBoard import ChessBoard

class TourCreator(Static):

    tour = []

    def on_chess_board_move(self, move: ChessBoard.Move):
        """ Respond to chessboard moves. """
        self.tour.append(move.square)

    def compose(self) -> ComposeResult:
        yield ChessBoard(board_size=5)