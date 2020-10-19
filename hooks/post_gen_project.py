"""Post-Generate Hooks.

Cookiecutter will automatically run these after the project is created.
The current working directory is the newly created directory by default.
"""
import os
import sys
import glob

from pathlib import Path


# Remove .keep files
try:
    for filename in glob.glob("**/.keep", recursive=True):
        os.remove(filename)
except:
    sys.exit(1)


# Move info file one directory up
path = "{{ cookiecutter.info_file }}"
p = Path(path).absolute()
newname = p.parents[1] / p.name
if not os.path.exists(newname):
    p.rename(newname)
else:
    print(f"\nWARNING: file `{path}` already exists, the newly created"\
          +f" one was placed in `{{ cookiecutter.docs_dir }}/{path}`.")
