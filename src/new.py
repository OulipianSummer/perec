"""
new.py

Handles the business logic of creating new things in perec including new projects and the scaffolding files, new tours, and more.

"""

from .chess import *
from collections import namedtuple
from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from InquirerPy.validator import EmptyInputValidator
from .lib import *
import os
from .pattern import pluralize
from typing import Union
from yaml import dump


#---------------------------------------------------------------------------------------|  
#  Project management
#---------------------------------------------------------------------------------------|  

def new_project(arguments: dict) -> None:
    """
    Starts a new perec project using the terminal prompt.
    """

    print("Starting a new project!")
    print()
    
    # Get the project name from the user
    name = inquirer.text(
        message="Project Name: ",
        validate=EmptyInputValidator(),
        mandatory=True,
        mandatory_message="A project name is required",
    ).execute()
    
    # Create a machine name from the project name.
    machine_name = text_to_var(name)

    # Allow the user to enter a description for their project.
    description = inquirer.text(
        message="Description: ",     
    ).execute()
    
    # Collect the size (also sometimes called "order") of the project.
    size = inquirer.number(
        message="Size: ",
        min_allowed=MIN_PROJECT_SIZE,
        max_allowed=MAX_PROJECT_SIZE,
        validate=EmptyInputValidator(),
        default=DEFAULT_PROJECT_SIZE,
        invalid_message="Input must be a number between %i and %i" % (MIN_PROJECT_SIZE, MIN_PROJECT_SIZE),
        mandatory=False
    ).execute()

    # Pick default size if the size prompt is skipped
    if size == None:
        size = DEFAULT_PROJECT_SIZE;
    
    # Prompt the user for the section header name.
    # The user-facing "name" should always be capitalized and plural. The internal "value" is lower case and singular.
    SectionChoice = namedtuple("ExpandChoice", ["key", "name", "value"])
    section_type = inquirer.expand(
        message="Section Type: ",
        choices = [ExpandChoice(**item) for item in SECTION_CHOICES],
        default="chapter",
        mandatory=False
    ).execute()

    # Default to chapter if the user skipped the above prompt.
    if section_type == None:
        section_type = "chapter"

    # If users select "other" provide another prompt to collect the custom section type.    
    elif section_type == "other":

        # Give users a chance to define their section type
        section_type_other = inquirer.text(
            message="Section Type: ",
            mandatory=True,
            validate=EmptyInputValidator(),
            mandatory_message="Enter a singular name for your sections."
        ).execute()

        section_type = pluralize(section_type_other)

    input = {
        "name": name,
        "machine_name": machine_name,
        "description": description,
        "size": size,
        "section_type": section_type,
        "lists": [],
        "mols": [],
        "tour": "",
    }
    
    path = arguments['<path>']

    # Pass the user input on to another function to create the project folder
    initialize_project_scaffolding(input, path)

def initialize_project_scaffolding(input: dict, path: Union[str, None]) -> None:
    """
    Creates a project folder from the given user input and cli arguments.

    This function should be useable both from the CLI and the TUI, as needed.

    In the future, this should also allow users to pull from pre-defined tours, mols, or lists in their system and list them in config.yml.
    """
    print()
    print("Creating project! Sit tight...")

    # If no path was provided at command time, then make one based on the user input and the current working directory
    if path == None: 
        path = os.path.join(os.getcwd(), input["machine_name"])
        check_path(path)

    # Create the project directory
    os.mkdir(path)
    
    # Create the internal directory structure
    lists_path = os.path.join(path, 'lists')
    mols_path = os.path.join(path, 'mols')
    tours_path = os.path.join(path, 'tours')
    os.mkdir(lists_path)
    os.mkdir(mols_path)
    os.mkdir(tours_path)

    # Create the config file
    config_path = os.path.join(path, 'perec_config.yml')
    stream = open(config_path, "w")
    config_file = dump(input, stream)
    stream.close()

    did_create = os.path.exists(path)

    if did_create:
        print()
        print("Project created successfully!")
        print("Location: %s" % path)
    else:
        print()
        print("The project was not created successfully. Please review your input and try again.")

#---------------------------------------------------------------------------------------|  
#  End project management
#---------------------------------------------------------------------------------------|  

#---------------------------------------------------------------------------------------|  
#  Tour management
#---------------------------------------------------------------------------------------|

def create_new_tour(arguments: object | None) -> Union[list[str], None]:

    # Parse/gather chessboard size.
    size = arguments["<size>"]
    if not size:
        size = inquirer.number(
            message="Enter chessboard size (use your arrow keys):",
            min_allowed=5,
            max_allowed=10,
            mandatory=True,
            validate=EmptyInputValidator(),
        ).execute()

    size = int(size)

    # Parse/gather starting square.
    start = arguments["--start"]
    if not start:
        start = inquirer.text(
            message="Enter the starting square (a1, b2, etc.):",
            mandatory=True,
            validate=lambda result: is_valid_square(result, size),
            default="a1"
        ).execute()

    # Confirm the current selection.
    confirm = inquirer.confirm(
        message=f"Generate a pseudo-random knight's tour of size {size} starting at square {start}?\n",
        default=True,
        confirm_letter="y",
        reject_letter="n",
        mandatory=True,
    ).execute()

    # FIXME: This technically gets calced twice (once above in is_valid_square call). The result should be cached so we don't have to calc the same answer each time.
    start_x, start_y = chess_notation_to_index(start)

    tour, board = generate_tour(int(size), start_x, start_y)

    if tour:
        return tour

#---------------------------------------------------------------------------------------|  
#  End tour management
#---------------------------------------------------------------------------------------|  

    



