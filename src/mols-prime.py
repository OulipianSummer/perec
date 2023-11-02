""" Generate sets of mutually orthogonal Latin squares (MOLS)

    See https://math.stackexchange.com/a/1624875/207316

    Written by PM 2Ring 2016.01.24
    Updated 2021.01.31

    Updated by Andrew Benbow
"""

#from __future__ import print_function

import sys
import random

def show_grid(g):
    for row in g:
        print(row)
    print()

def test_mols(g):
    """ Check that all entries in g are unique """
    a = set()
    for row in g:
        a.update(row)
    return len(a) == len(g) ** 2

def mols(n):
    """ Generate a set of mutually orthogonal Latin squares
        n must be prime
    """
    r = range(n)

    #Generate each Latin square
    allgrids = []
    for k in range(1, n):
        grid = []
        for i in r:
            row = []
            for j in r:
                a = (k*i + j) % n
                row.append(a)
            grid.append(row)

        # Test that there are no repeated items in the 1st column.
        # This test is unnecessary for prime n, but it lets us
        # produce some pairs of MOLS for odd composite n
        if len(set([row[0] for row in grid])) == n:
            allgrids.append(grid)
    
    # HACK Test shuffling the grids to see if we get some new mols
    for i in range(0, len(allgrids) * n):
        allgrids.append(random.sample(allgrids[i], len(allgrids[i])))



    for i, g in enumerate(allgrids):
        print(i)
        show_grid(g)

    print('- ' * 20 + '\n')

    # Combine the squares to show their orthogonality
    m = len(allgrids)
    for i in range(m):
        g0 = allgrids[i]
        for j in range(i+1, m):
            g1 = allgrids[j]
            newgrid = []
            for r0, r1 in zip(g0, g1):
                newgrid.append(list(zip(r0, r1)))
            result = test_mols(newgrid)
            if result is True:
                print(i, j, result)
                show_grid(newgrid)

def main():
    # Get order from command line, or use default
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    mols(n)

if __name__ == '__main__':
    main()

