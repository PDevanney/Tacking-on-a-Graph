# Tracking on a Graph - Dr. Jessica Enright
## Description
> This Project will create a Python script that will attempt to locate a Target on a graph in the most optimal number of moves possible as per the specification described below.
---
## Installation
> ** ToDo Update Installation **
---
## Authors and Acknowledgement
> Patrick Justin Devanney -- patrickdevanney28@gmail.com
---
## License
> MIT License

> Copyright (c) 2020 Patrick Justin Devanney

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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
