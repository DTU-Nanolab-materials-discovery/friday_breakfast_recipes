#add checks parsing the md files
from pathlib import Path
import re
import sys

title_re = re.compile("^# + ", re.MULTILINE)
ingredients_re = re.compile("^#+ +ingredients", re.IGNORECASE | re.MULTILINE)
instructions_re = re.compile("^#+ +instructions", re.IGNORECASE | re.MULTILINE)
tools_re = re.compile("^#+ +tools", re.IGNORECASE | re.MULTILINE)

paths = Path(__file__).parent.glob("*/*.md")
errors = 0
for path in paths:
    if not title_re.search(path.read_text()):
        print(f'File {path} is missing any title: "# ..."')
        errors += 1
    if not ingredients_re.search(path.read_text()):
        print(f'File {path} is missing a section: "## Ingredients"')
        errors += 1
    if not instructions_re.search(path.read_text()):
        print(f'File {path} is missing a section: "## Instructions"')
        errors += 1
    if not tools_re.search(path.read_text()):
        print(f'File {path} is missing a section: "## Tools"')
        errors += 1

if errors:
    sys.exit(1)
