# make a custom directory tree command

bash command `ls` and `ls -la` are used to get a list of files of current working directory.  
Sometimes we need much more list depthness than just the current directory,  
and thus 
we can make our own `lst` command (list tree).  

## Steps
1. Fisrt create a python file `lst.py`, and add this code  

```python3
import os

startpath = os.getcwd()
ignore_files = ['.DS_Store']

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if(f not in ignore_files):
                print('{}{}'.format(subindent, f))

list_files(startpath)
```  
I got this code for printing tree from [here](https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python)

2. make a alias in your .bashrc file
```bash
alias lst='python3 /Users/apple/lst.py'
```
* Note : /Users/apple/ is my path where lst.py is located, if your path is different use that path.

3.relauch the terminal
