from collections import namedtuple
from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from InquirerPy.validator import EmptyInputValidator
from .lib import *
import os
from .pattern import pluralize
from yaml import dump

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
        "tour": ""
    }

    # Pass the user input on to another function to create the project folder
    create_project_folder(arguments, input)

    return


def create_project_folder(arguments: dict, input: dict) -> None:
    """
    Creates a project folder from the given user input and cli arguments.

    In the future, this should also allow users to pull from pre-defined tours, mols, or lists in their system.
    """
    print()
    print("Creating project! Sit tight...")

    path = arguments['<path>']

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
    config_path = os.path.join(path, 'config.yml')
    stream = open(config_path, "w")
    config_file = dump(input, stream)
    stream.close()
    
