# maze-solver


This is an implementation of a path finding algorithm.

Currently only one algorithm is available (*Breadth First Search*), but more will be added in the future (hopefully).

What I practiced on this project:
* logging module
* curses module - allowing to display and refresh standard console output in a more managable way
* @property decorator - dealing with setters & getters the pythonic way
* OOP python programming
* docstrings
* FIFO queues
* enumerate() function

---
Feel free to play around with the project by constructing different types of mazes!

The definition of the maze pattern occurs in the main.py and is defined by a list of lists, using the following signs:
* ' ' - empty space
* '#' - occupied space/wall
* 'O' - starting position
* 'X' - goal

![screenshot1](src/screenshots/screenshot1.png?raw=true "Screenshot of default maze")