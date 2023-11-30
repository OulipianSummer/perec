LEGAL_MOVES = [
    [1, 2],
    [1, -2],
    [-1 , 2],
    [-1, -2],
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
]

def index_to_chess_notation(row: int, col: int, board_size: int) -> str:
    """ Convert 0 indext coordinates into chess notation."""

    chess_col = chr(ord('a') + col)
    chess_row = str(board_size - row)
    return chess_col + chess_row


def chess_notation_to_index(move: str, mode = "human") -> int:
    """ Convert algabraic chess notation to numeric coordinates. Can return 1 indexed and 0 indexed results. """

    x_offset = 96
    y_offset = 0

    # Check to see if we should be generating a zero index result.
    if mode == 'zero':
        x_offset = x_offset + 1
        y_offset = y_offset + 1

    x = ord(move[0]) - x_offset
    y = int(move[1]) - y_offset
    return x, y

def is_valid_move(last: str, selected: str) -> bool:
    """ Compares two moves to see if they adhere to chess knight movements. """  

    x_last, y_last = chess_notation_to_index(last)
    x_sel, y_sel = chess_notation_to_index(selected)

    for move in range(len(LEGAL_MOVES)):
            
        x_next = x_last + LEGAL_MOVES[move][0]
        y_next = y_last + LEGAL_MOVES[move][1]

        if x_next == x_sel and y_next == y_sel:

            return True

    return False
        