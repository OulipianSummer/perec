from re import sub

MIN_PROJECT_SIZE = 5
MAX_PROJECT_SIZE = 10
DEFAULT_PROJECT_SIZE = 8
SECTION_CHOICES = [
  {"key": "c", "name":"Chapters", "value":"Chapter"},
  {"key": "s", "name":"Stanzas", "value":"Stanza"},
  {"key": "g", "name":"Paragraphs", "value":"Paragraph"},
  {"key": "p", "name":"Poems", "value":"Poem"},
  {"key": "o", "name":"Other", "value":"Other"}
]

def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()