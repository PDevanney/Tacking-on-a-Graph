
## Tracking on a Graph - Dr. Jessica Enright

I am interested in the following pursuit game: imagine that I have a number of tracking towers that I can place on a graph. 
On each turn, an opponent is going to move from one vertex to another in the graph. I then get to know how far that opponent is from each of my towers. 
Then the next turn begins, the opponent moves, and I get to know the distance it *now* is from each of my towers. 
The opponent is not allowed to visit a vertex it has already visited. 
If I ever know exactly where the opponent is at the current time, then I win! How can I place my towers so that I am guaranteed to win as quickly as possible? 
How many moves will the opponent be able to take? Some work on this problem on simple graph classes (e.g. cycles, hypercubes) has already been done that can be shared with a student. 

### Project
In this project, a student should investigate this game using computational approaches combined with some formal reasoning. 
A student might implement a simple search approach to simulate an optimal opponent, and then use that to asses the ability of heuristic approaches to find good tower locations on various 
kind of graphs. 
They might also implement a provably-exhaustive search to find the best possible tower locations for various numbers of towers on various graph classes. This topic could be suitable for a L4 (undergrad) or L5 (MSci) project.
