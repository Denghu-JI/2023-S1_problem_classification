import git
import subprocess
import pathlib
import os


path = pathlib.Path().resolve()
a = '/'.join(str(path).split('/')[:-2])
repo = git.Repo(a)
for submodule in repo.submodules:
    submodule.update(init=True)
    
for root, dirs, files in os.walk(path):
    for name in files:
        print(name)
        if name.endswith(("fi", "o")):
            print(name)
    

    
