import curses
from curses import wrapper
from src.functions import find_path


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


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_path(maze, stdscr)
    stdscr.getch()


wrapper(main)
