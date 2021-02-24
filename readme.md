# Tracking on a Graph - Dr. Jessica Enright
## Description
> This Project will create a Python script that will attempt to locate a Target on a graph in the most optimal number of moves possible as per the specification described below.
---
## Installation
> The required packages for the project are as follows
> * Numpy
> * NetworkX
> * MatPlotLib
> * TreeLib
> 
> Packages can be installed by navigating to the required directory and using command:
```` 
pip install -r requirements.txt
````
> This will autommatically install all requirements of the project.
> Upon installation of these packages the command
````
python main.py [ARGUMENTS : playable graph_size tower_count]
````
> Will run the script. By default the Evaluation script will be run. With Graph Size of 25 and Tower Count of 3
---
## Authors and Acknowledgement
> Patrick Justin Devanney -- Student at the University of Glasgow, Email: patrickdevanney28@gmail.com
> 
> Supervised by Dr. Jessica Enright -- Lecturer of Computing Science at the University of Glasgow
---
## Initial Project Specification
> I am interested in the following pursuit game: imagine that I have a number of tracking towers that I can place on a graph. 
On each turn, an opponent is going to move from one vertex to another in the graph. I then get to know how far that opponent is from each of my towers. 
Then the next turn begins, the opponent moves, and I get to know the distance it *now* is from each of my towers. 
The opponent is not allowed to visit a vertex it has already visited. 
If I ever know exactly where the opponent is at the current time, then I win! How can I place my towers so that I am guaranteed to win as quickly as possible? 
How many moves will the opponent be able to take? Some work on this problem on simple graph classes (e.g. cycles, hypercubes) has already been done that can be shared with a student. 
> ### Project
> In this project, a student should investigate this game using computational approaches combined with some formal reasoning. 
A student might implement a simple search approach to simulate an optimal opponent, and then use that to asses the ability of heuristic approaches to find good tower locations on various 
kind of graphs. 
They might also implement a provably-exhaustive search to find the best possible tower locations for various numbers of towers on various graph classes. This topic could be suitable for a L4 (undergrad) or L5 (MSci) project.
---
