# Readme

This project has created a evaluative product in python. This project is an implemenation of a alternative approach to the well known "Cops and Robbers" game. Within this approach there are two main entities, one or more towers and a singular target. At the start of the game both objects would be positioned on the graph. Each turn, the tower would assess every node on the graph and be returned a vector D(G) = (d_1, d_2, ..., d_n) where d_i is the distance from the tower to every node on the graph G. The towers would also receive the current distance at that turn to the target. Using this provided information the tower would attempt to assess the current location of the target. If the target is not found then it can move to an adjacent node on the graph. The tower wins if the target is ever located. The specification discussed varying investigations and evaluations into the various aspects of the newly devised game specification.

By default, the project will perform an evalautive review of this game. Parameters can be adapted via Command Line arguments or editing of the source code to allow for a varied evaluation or the playable version of this game. The primary driving functionality behind the code is seen in main.py and will deal with the conducting the basic game. All other files named accordingly deal with their own section of the code.

* main.py - Driving functionality.
* playable.py - Functions exclusive to the playable section of the game - graph visualisation, setting node colour.
* distances.py - Code for computing distance to all nodes and distance to target functionality.
* search.py - Code for performing the search of the target node.
* target.py - Functions exclusive to the target objects. Split into classes Random, Heuristic, and Optimal.
* tower.py - Functions exclusive to the tower objects. Split into classes Random, Heuristic, and Optimal.
* optimal.py - Functionality for computing the optimal path within a graph.

* tests directory - Folder containing appropriate unittest files for the project. test files named representative of the functionality they are testing.



## Build instructions

**You must** include the instructions necessary to build and deploy this project successfully. If appropriate, also include 
instructions to run automated tests.

### Requirements
* Python 3.8.5
* PIP -- PIP is automatically installed with Python 2.7.9+ and Python 3.4+. Check if pip is installed using `pip help`
* Packages: listed in `requirements.txt` 
* Tested on Windows 10 using the ANACONDA Distribution

### Build steps

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

#### Run automated tests by running 
* `python -m unittest` from within the "src\tests" folder

#### Start the software by running:
* `python main.py` Will run the program. By default the evaluative section will be run. The following arguments can be passed in to adapt the section
* `ARGUMENTS : playable graph_size tower_count`
* `USAGE : python main.py False 50 3` Will perform the evaluative section on a graph of size 50 with 3 tower nodes.
* `USAGE : python main.py True 50 3` Will perform the playable section on a graph of size 50 with 3 tower nodes.
* Note **all** arguments must be passed in or default options will be used
* The default options are set as False 50 3.

