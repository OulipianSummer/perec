import os
from yaml import load

def discover_projet():
    """
    Checks the current working directory for a perec_config.yml file.
    If one is found, load it and return it.
    """
    config_path = os.path.join(os.getcwd(), 'perec_config.yml')
    if(os.path.exists(config_path)):
        return load_project_info(config_path)

    
def load_project_info(config_path):
    """Given a path pointing to a perec_config.yml file, parse and return the contents of that file"""

    stream = fopen(config_path, "r")
    info = load(stream)
    fclose(stream)
    return info

def save_project_info():
    pass