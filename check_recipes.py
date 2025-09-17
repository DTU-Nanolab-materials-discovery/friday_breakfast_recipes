#add checks parsing the md files
import glob
from pathlib import Path
import re
import sys

ingredients_re = re.compile("^#+ +ingredients", re.IGNORECASE | re.MULTILINE)
instructions_re = re.compile("^#+ +instructions", re.IGNORECASE | re.MULTILINE)
tools_re = re.compile("^#+ +tools", re.IGNORECASE | re.MULTILINE)

paths = Path(__file__).parent.glob("*/*.md")
errors = 0
for path in paths:
    if not ingredients_re.search(path.read_text()):
        print(f'File {path} is missing a section: "## Ingredients"')
        errors += 1
    if not instructions_re.search(path.read_text()):
        print(f'File {path} is missing a section: "## Instructions"')
        errors += 1
    if not tools_re.search(path.read_text()):
        print(f'File {path} is missing a section: "## TOOLS"')
        errors += 1

if errors:
    sys.exit(1)
