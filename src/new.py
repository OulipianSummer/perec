from collections import namedtuple
from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from InquirerPy.validator import EmptyInputValidator
from .lib import *
from .pattern import pluralize
from typing import Union


def new_project(path: Union[bool, str]) -> None:
    """
    Starts a new perec project using the terminal prompt.
    """
    print("Starting a new project!\n")
    
    project_name = inquirer.text(
        message="Project Name: ",
        validate=EmptyInputValidator(),
        mandatory=True,
        mandatory_message="A project name is required",
    ).execute()
    
    project_machine_name = snake_case(project_name)

    description = inquirer.text(
        message="Description: ",     
    ).execute()
    
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
    
    SectionChoice = namedtuple("ExpandChoice", ["key", "name", "value"])
    section_type = inquirer.expand(
        message="Section Type: ",
        choices = [ExpandChoice(**item) for item in SECTION_CHOICES],
        default="Chapter",
        mandatory=False
    ).execute()

    if section_type == None:
        section_type = "Chapter"
    elif section_type == "Other":

        # Give users a chance to define their own input
        section_type_other = inquirer.text(
            message="Section Type: ",
            mandatory=True,
            validate=EmptyInputValidator(),
            mandatory_message="Enter a singular name for your sections."
        ).execute()

        section_type_other = pluralize(section_type_other) 

        print(section_type_other)