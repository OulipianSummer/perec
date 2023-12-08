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

def index_to_chess_notation(col: int, row: int, board_size: int) -> str:
    """ Convert 0 indexed coordinates into chess notation."""

    chess_col = chr(ord('a') + col)
    return chess_col + str(row + 1)


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

def generate_tour(size, startx, starty, tries = 0, moveset = LEGAL_MOVES):
    """
    A 

    Usage:
    Produces a knights tour from any given start position using the Warnsdorf huerstic.

    Arguments:
    size : A number
    startx : Starting position x coordinate between 1 and size
    starty : Starting position y coordinate between 1 and size

    """
    
    # Establishes the board size
    board_size = size or 10
    max_moves = board_size * board_size

    # Start Positions
    x = startx or 6
    y = starty or 6

    # Assigns a virtual knight to the start position provided by x and y
    kx = x - 1
    ky = y - 1

    # Creates a virtual chess board as a list of lists (for easy board[x][y] indexing)
    board = []
    for i in range(size):
        board.append([0] * size)

    # Places knight on the chessboard
    board[kx][ky] = 1
    
    # Creates a list of the fist xy coords of the knight, and then appends them to a list to be used for recording subsequent move coords
    first_coords = index_to_chess_notation(x - 1,y - 1,size)

    coords = []
    coords.append(first_coords) 

    for move in range(2, max_moves + 1):
        possible_moves = 0
        next_x = [0] * size
        next_y = [0] * size

        for i in range(0, 8):
            check_x = kx + moveset[i][0]
            temp_y = ky + moveset[i][1]

            if (check_x >= 0 and check_x < size
                and temp_y >=0 and temp_y < size
                and board[check_x][temp_y] == 0):
                next_x[possible_moves] = check_x
                next_y[possible_moves] = temp_y
                possible_moves += 1
        smallest_move = 0

        if possible_moves == 0 and tries > 9:
            tries = tries + 1
            shuffle(moveset)
            return generate_tour(size, startx, starty,tries, moveset)

        if tries == 10:
            print("Unable to create a tour\n")

        elif possible_moves > 1:
            exits = [0] * size

            for i in range(0, possible_moves):
                num_exits = 0

                for j in range(0, 8):
                    check_x = next_x[i] + moveset[j][0]
                    check_y = next_y[i] + moveset[j][1]

                    if (check_x >= 0 and check_x < size
                        and check_y >= 0 and check_y < size
                        and board[check_x][check_y] == 0):
                        num_exits += 1
                
                exits[i] = num_exits
             
            smallest_move = 0
            
            current_num_exit = exits[0]

            for i in range(1, possible_moves):
                if current_num_exit > exits[i]:
                    current_num_exit = exits[i]
                    smallest_move = i

        kx = next_x[smallest_move]
        ky = next_y[smallest_move]
        
        current_coords = index_to_chess_notation(kx, ky, size)
        coords.append(current_coords)

        board[kx][ky] = move  

    return coords, board