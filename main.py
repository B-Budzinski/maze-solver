import curses
from curses import wrapper
from src.Maze import Maze
from src.Solver import Solver


maze = [
    ["#", "#", "#", "#", "#", "#", "#", "X", "#", "#"],
    ["#", "#", " ", " ", " ", "#", "#", " ", "#", "#"],
    ["#", "#", " ", "#", " ", "#", "#", " ", "#", "#"],
    ["#", "#", " ", "#", " ", "#", "#", " ", "#", "#"],
    ["#", "#", " ", "#", " ", "#", "#", " ", "#", "#"],
    ["#", "#", " ", "#", " ", " ", " ", " ", "#", "#"],
    ["#", "#", " ", "#", "#", "#", "#", "#", "#", "#"],
    [" ", " ", " ", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", " ", "#", "#", "#", "#", " ", "#", "#"],
    ["#", "#", "O", " ", " ", " ", " ", " ", "#", "#"],
]


# New main
def main(stdscr, maze):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    maze = Maze(stdscr=stdscr, maze=maze)
    maze.col_maze = BLUE
    maze.col_path = RED

    solver = Solver(maze)
    solver.find_path()
    stdscr.getch()


wrapper(main, maze)
