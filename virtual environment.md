# Virtual Environment

virtual environment, is a **good practice** to do projects in python.
It helps to organised the required working modules and python interpreter version.

## here are some commands for working with virtual env:
* create
* activate
* check
* export requirements.txt
* use requirements.txt to create 
* deactivate


*pip --> pip or pip3*

To download virtual evn for python:

* `$ pip install virtualenv`

list the downloaded packages and modules:

* `$ pip list`

## In the project director

create a virtual environment

* `$ virtualenv <name of environment>`

activates the virtual environment

* `$ source <name of environment>/bin/activate`

To tell the path of python interpreter which is going to run files
* `$ which python`

To tell the path of the pip
* `$ which pip`

To make a .txt file of installed packages
* `$ pip freeze --local > requirements.txt`

To deactivate
* `$ deactivate`

To remove virtual env folder
* `$ rm -rf <directory name>`

To download the required packages, from requirements.txt
* `$ pip install -r requirements.txt`


