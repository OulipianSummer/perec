#!/usr/bin/python3

"""perec is a tool used for generating a list of Oulipian writing prompts

Usage:
    perec new project [<path>]
    perec new mols [<size>] [<number>]
    perec new latin square [<size>] [<number>]
    perec -h | --help
    perec -v | --version

Commands: 
    new project [<path>]  Starts a new perec project. If no path is chosen, the progam will create a new project in the current working directory
    new latin square [<size>] [<number>]  Generate <number> latin squares of <size>.  If both arguments are omitted, perec will use the info from your current project.
    new mols [<size>] [<number>]  Generate <number> of mututally orthogonal latin square of <size>. If both arguments are omitted, perec will use the info from your current project.

Options:
    -h --help   Shows this screen
    -v --version   Shows the version number of perec

"""


### Imports ###
from docopt import docopt
import os
from src import new, lib, latin_squares

class Operations:
    NEW_PROJECT = "new_project"
    NEW_MOLS = "new_mols"
    NEW_LS = "new_latin_square"

def main(op: str, arguments: dict) -> None:
    """
    Executes the main function
    """

    # Execute top level functions after input validation
    match op:
        case Operations.NEW_PROJECT:
            new.new_project(arguments)

        case Operations.NEW_LS:
            latin_squares.new_ls(arguments)

        case Operations.NEW_MOLS:
            #squares.new_mols(arguments)
            pass

    pass

# Parse arguments and throw exceptions if needed
if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')

    try:

        # Start a new project
        if arguments['new'] and arguments['project']:

            # Do a pre-check on the user provided path. The pathname must at least be plausible and it must NOT exist in order to proceed.
            # Also modify the argument path using os.path.abspath so we can use it later
            if arguments['<path>'] != None:
                arguments['<path>'] = os.path.abspath(arguments['<path>']);
                path = arguments['<path>']
                lib.check_path(path)

            main(Operations.NEW_PROJECT, arguments)
        
        elif arguments['new'] and arguments['latin'] and arguments['square']:
            main(Operations.NEW_LS, arguments)

        elif arguments['new'] and arguments['mols']:
            main(Operations.NEW_MOLS, arguments)

    except KeyboardInterrupt:
        pass