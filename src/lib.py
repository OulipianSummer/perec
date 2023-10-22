from re import sub

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