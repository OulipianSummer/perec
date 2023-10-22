import errno
from re import sub
import os
import sys

MIN_PROJECT_SIZE = 5
MAX_PROJECT_SIZE = 10
DEFAULT_PROJECT_SIZE = 8

#-------------------------------------------------------------------------------------------------------#
# Section Choices
#
# Users are allowed to choose from (or create) their own section headers called "section types".
# This helps users organize their prompts according to the type of project they are using perec for.
# The list below organizes a few popular choices as well as the "Other" option which indicates custom input.
#
# The basic idea is that the "name" key in the dict represents the user facing name of the section in the
# inquirer interface. This should always be pluraland the first character uppercase.
# The "value" key is the internal, machine-friendly name that gets passed to perec. This is always
# lower case alphanumeric characers separated by underscores (snake case).
# The "key" key is a keyboard shortcut for selecting the given choice.
#-------------------------------------------------------------------------------------------------------#
SECTION_CHOICES = [
    {"key": "c", "name":"Chapters", "value":"chapter"},
    {"key": "s", "name":"Stanzas", "value":"stanza"},
    {"key": "g", "name":"Paragraphs", "value":"paragraph"},
    {"key": "p", "name":"Poems", "value":"poem"},
    {"key": "o", "name":"Other", "value":"other"}
]

def text_to_var(s):
    """
    Convert user input text to a snake case variable name free from punctuation
    """
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        sub('([!@#\$%\^&\*,.?:_\-\'\"])', r'', # Strip out punctuation characters we don't want
        s.replace('-', ' ')))).split()).lower()


def check_path(path:str) -> None:
    """
    A function that pulls together a few path validation techniques
    """
    if not is_pathname_valid(path): raise TypeError("The provided path name is not valid")
    if os.path.exists(path): raise TypeError("The provided pathname points to an existing directory. Please delete it to continue.")


# Sadly, Python fails to provide the following magic number for us.
ERROR_INVALID_NAME = 123
'''
Windows-specific error code indicating an invalid pathname.

See Also
----------
https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
    Official listing of all such codes.
'''

def is_pathname_valid(pathname: str) -> bool:
    '''
    Source: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    '''
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)   # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True
    # If any other exception was raised, this is an unrelated fatal issue
    # (e.g., a bug). Permit this exception to unwind the call stack.
