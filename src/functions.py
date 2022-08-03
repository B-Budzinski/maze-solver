from curses import wrapper
import curses
import queue
import time
import logging

# Logging config
logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def draw_maze(maze, stdscr, path=None):
    """Function that displays draws the maze using stdscr

    Args:
        maze (list): maze object
        stdscr (Any): stdscr object
        path (list, optional): List of tuples containing position of the path to be drawn. Defaults to None.
    """
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) not in path:
                stdscr.addstr(i, j * 2, value, BLUE)
            else:
                stdscr.addstr(i, j * 2, "=", RED)


def find_start_pos(maze, start):
    """Takes maze object and returns coordinates of starting position (denoted by "O")

    Returns:
        tuple: contains x, y coordinates of starting position
    """

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)


def find_neighbors(maze, x, y):
    """Find free neighboring nodes

    Args:
        maze (list): maze object
        x (int): pos x
        y (int): pos y

    Returns:
        list: list of tuples with neighbors positions. Not checking diagonals.
    """
    neighbors = []
    to_check = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for pos in to_check:
        try:
            if maze[pos[0]][pos[1]] == " ":
                neighbors.append(pos)
        except IndexError:
            pass

    return neighbors


def find_path(maze, stdscr):
    """Find the path

    Args:
        maze (list): maze object
        stdscr (Any): stdscr object
    """
    START = "O"
    END = "X"
    q = queue.Queue()  # initialise Queue object (FIFO)
    visited = set()
    start_pos = find_start_pos(maze, start=START)  # get starting position

    q.put(
        (start_pos, [start_pos])
    )  # put starting position in queue along with the path so far

    while not q.empty():

        time.sleep(0.1)
        pos, path = q.get()
        row, col = pos
        path = list(path)
        visited.add((row, col))

        logging.info(f"visited: {visited}")
        logging.info(f"queue: {list(q.queue)}")
        logging.info(f"drawing path: {path}")
        stdscr.clear()
        draw_maze(maze, stdscr, path)
        stdscr.refresh()
        if maze[row][col] == END:
            logging.info(f"Found Solution! Maze ends at {row}, {col}")

            return (pos, path)
        else:
            neighbors = find_neighbors(maze, x=row, y=col)
            for i, pos in enumerate(neighbors):
                if pos not in visited:

                    logging.info(f"{pos}, not yet in visited")
                    logging.info(f"path before: {path}")
                    logging.info(f"que before: {list(q.queue)}")
                    new_path = path + [pos]

                    q.put((pos, new_path))
                    logging.info(f"path after: {new_path}")
                    logging.info(f"que after: {list(q.queue)}")

    print("finished!")
