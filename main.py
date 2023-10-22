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

def main():
    """
    Executes the main function
    """
    pass

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')

    # Start a new project
    if arguments['new'] and arguments['project']:

        # Do a check on the user provided path (if one exists) before we do anything else
        path = arguments['<path>']
        if path != None:
            if not lib.is_pathname_valid(path): raise TypeError("The provided path name is not valid")
            if os.path.exists(path): raise TypeError("The provided pathname points to an existing directory. Please delete it to continue.")

        new.new_project(arguments)
