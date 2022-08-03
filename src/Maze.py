import curses
from curses import wrapper


class Maze:
    """
    Maze object deals with maze drawing and represantation
    You can pass a path to it if you want it to be drawn with a different color from the rest of the maze.
    """

    def __init__(self, stdscr, maze) -> None:

        self.stdscr = stdscr
        self.maze = maze

        self.col_maze = None
        self.col_path = None
        self.path = []
        self.start_sign = "O"
        self.end_sign = "X"

    @property
    # getter method
    def maze(self):
        return self._maze

    # setter method
    @maze.setter
    def maze(self, new_maze):
        self._maze = new_maze

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        self._path = new_path

    @property
    def col_maze(self):
        return self._col_maze

    @col_maze.setter
    def col_maze(self, new_col):
        self._col_maze = new_col

    @property
    def col_path(self):
        return self._col_path

    @col_path.setter
    def col_path(self, new_col):
        self._col_path = new_col

    def draw_maze(self):
        """Method that displays draws the maze using stdscr

        Args:
            maze (list): maze object
            stdscr (Any): stdscr object
            path (list, optional): List of tuples containing position of the path to be drawn. Defaults to None.
        """

        for i, row in enumerate(self.maze):
            for j, value in enumerate(row):
                if (i, j) not in self.path:
                    self.stdscr.addstr(i, j * 2, value, self.col_maze)
                else:
                    self.stdscr.addstr(i, j * 2, "=", self.col_path)
