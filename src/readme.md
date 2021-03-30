# Readme

Put a brief description of your code here. This should at least describe the file structure.

## Build instructions

**You must** include the instructions necessary to build and deploy this project successfully. If appropriate, also include 
instructions to run automated tests.

### Requirements
* Python 3.8.5
* PIP -- PIP is automatically installed with Python 2.7.9+ and Python 3.4+. Check if pip is installed using `pip help`
* Packages: listed in `requirements.txt` 
* Tested on Windows 10 using the ANACONDA Distribution

### Build steps

List the steps required to build software. 

Utilisation of the ANACONDA distribution is the simplest route to build and the run the code. Installation instructions can be located at;
[Anaconda](https://www.anaconda.com/products/individual) The use of this distribution is optional.

Once downloaded the following commands can be used to create a new environment and install the relevant packages.

* `conda create -n env-name python=3.8.5`
* `conda activate env-name`

Once in this enviroment. Navigate to the src file of the project repository using the command.
* `cd src`

To install required packages run the following from within the "src" folder.
* `pip install -r requirements.txt`

### Test steps

#### Run automated tests by running `python -m unittest` from within the "src\tests" folder


#### Start the software by running:
* `python main.py` Will run the program. By default the evaluative section will be run. The following arguments can be passed in to adapt the section
* `ARGUMENTS : playable graph_size tower_count`
* `USAGE : python main.py False 50 3` Will perform the evaluative section on a graph of size 50 with 3 tower nodes.
* `USAGE : python main.py True 50 3` Will perform the playable section on a graph of size 50 with 3 tower nodes.
* Note **all** arguments must be passed in or default options will be used

