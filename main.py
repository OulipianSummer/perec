#!/usr/bin/python3
"""perec

Usage:
    perec new project [<path>]
    perec -h | --help
    perec -v | --version

Options:
    new project [<path>]  Starts a new perec project. If no path is chosen, the progam will create a new project in the current working directory
    -h --help   Shows this screen
    -v --version   Shows the version number of perec

"""


### Imports ###
from docopt import docopt
import os
from src import new, lib

OPS_NEW_PROJECT = "new_project"

def main(op: str, arguments: dict) -> None:
    """
    Executes the main function
    """

    # Execute top level functions after input validation
    match op:
        case OPS_NEW_PROJECT:
            new.new_project(arguments)

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

            main(OPS_NEW_PROJECT, arguments)

    except KeyboardInterrupt:
        pass