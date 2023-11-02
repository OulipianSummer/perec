"""
RandomLatinSquares.py

A random latin square generator script

Source: https://rosettacode.org/wiki/Random_Latin_squares#Python
"""

from random import choice, shuffle
from copy import deepcopy


def new_ls(arguments):
    size = int(arguments['<size>'])

    # Assign a default size until we can pull it from project
    if not size:
        size = 5
    
    square = make_latin_square(size)
    while test_square(square) is False:
        square = make_latin_square(size)
    




def manage_latin_square(op):
    pass


def make_latin_square(n):
    if n <= 0:
        return []
    else:
        symbols = list(range(n))
        square = _rls(symbols)
        return _shuffle_transpose_shuffle(square)


def _shuffle_transpose_shuffle(matrix):
    square = deepcopy(matrix)
    shuffle(square)
    trans = list(zip(*square))
    shuffle(trans)
    for i in range(0, len(trans)):
        trans[i] = list(trans[i])
    return trans


def _rls(symbols):
    n = len(symbols)
    if n == 1:
        return [symbols]
    else:
        sym = choice(symbols)
        symbols.remove(sym)
        square = _rls(symbols)
        square.append(square[0].copy())
        for i in range(n):
            square[i].insert(i, sym)
        return square

def _to_text(square):
    if square:
        width = max(len(str(sym)) for row in square for sym in row)
        txt = '\n'.join(' '.join(f"{sym:>{width}}" for sym in row)
                        for row in square)
    else:
        txt = ''
    return txt

def _check(square):
    transpose = list(zip(*square))
    assert _check_rows(square) and _check_rows(transpose), \
        "Not a Latin square"

def test_square(square):
    try:
        _check(square)
    except AssertionError:
        return False

def _check_rows(square):
    if not square:
        return True
    set_row0 = set(square[0])
    return all(len(row) == len(set(row)) and set(row) == set_row0
               for row in square)


if __name__ == '__main__':
    for i in [4, 4]:
        square = make_latin_square(i)
        print(_to_text(square))
        _check(square)
        print()