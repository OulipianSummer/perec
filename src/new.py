from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from .lib import snake_case, MIN_PROJECT_SIZE, MAX_PROJECT_SIZE
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
        default=8,
        invalid_message="Input must be a number between %i and %i" % (MIN_PROJECT_SIZE, MIN_PROJECT_SIZE),
    ).execute()


