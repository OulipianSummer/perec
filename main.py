#!/usr/bin/python3

"""perec is a tool used for generating a list of Oulipian writing prompts

Usage:
    perec start
    perec new project [<path>] [-t | --tui]
    perec new mols [<size>] [<number>]
    perec new latin square [<size>] [<number>]
    perec new tour [<size> | [--tour=<sequence>] [--start=<start_square>]] [-t | --tui]
    perec -h | --help
    perec -v | --version

Commands:
    start  Launches the interactive perec terminal user interface
    new project [<path>]  Starts a new perec project. If no path is chosen, the progam will create a new project in the current working directory
    new latin square [<size>] [<number>]  Generate <number> latin squares of <size>.  If both arguments are omitted, perec will use the info from your current project.
    new mols [<size>] [<number>]  Generate <number> of mututally orthogonal latin square of <size>. If both arguments are omitted, perec will use the info from your current project.
    new tour [<size>] [-t | --tui]

Options:
    -h --help   Shows this screen
    -v --version   Shows the version number of perec
    -t --tui  Launch the current command in the terminal user interface. Only works for certain commands.
    --tour=<sequence>  Manually input a knight's tour with comma separated squares. a1, b3, c5... etc.
    --start=<start_square>  Manually input a starting square for a knight's tour

"""


### Imports ###
from docopt import docopt
import os
from src import new, lib, latin_squares, textual

class Operations:
    LAUNCH_TUI = "launch_tui"
    NEW_PROJECT = "new_project"
    NEW_MOLS = "new_mols"
    NEW_LS = "new_latin_square"
    NEW_TOUR = "new_tour"

def main(op: str, arguments: dict) -> None:
    """
    Executes the main function
    """

    # Execute top level functions after input validation
    match op:

        case Operations.LAUNCH_TUI:
            textual.launch_tui(None, None)

        case Operations.NEW_TOUR:

            size = None

            if arguments["<size>"]:
                size = int(arguments["<size>"])

            if arguments['--tui']:
                textual.launch_tui(textual.TuiOperations.NEW_TOUR, arguments)
            else:
                new.create_new_tour(arguments)

        case Operations.NEW_PROJECT:
            new.new_project(arguments)

        case textual.TuiOperations.NEW_PROJECT:
            textual.launch_tui(textual.TuiOperations.NEW_PROJECT, arguments)

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
        
        # Launch the textual TUI
        if arguments['start']:
            main(Operations.LAUNCH_TUI, arguments)

        elif arguments['new'] and arguments['tour']:
            main(Operations.NEW_TOUR, arguments)

        # Start a new project
        elif arguments['new'] and arguments['project']:

            # Do a pre-check on the user provided path. The pathname must at least be plausible and it must NOT exist in order to proceed.
            # Also modify the argument path using os.path.abspath so we can use it later
            if arguments['<path>'] != None:
                arguments['<path>'] = os.path.abspath(arguments['<path>']);
                path = arguments['<path>']
                lib.check_path(path)

            if arguments["--tui"]:
                main(textual.TuiOperations.NEW_PROJECT, arguments)
            else:
                main(Operations.NEW_PROJECT, arguments)

        
        elif arguments['new'] and arguments['latin'] and arguments['square']:
            main(Operations.NEW_LS, arguments)

        elif arguments['new'] and arguments['mols']:
            main(Operations.NEW_MOLS, arguments)

    except KeyboardInterrupt:
        pass