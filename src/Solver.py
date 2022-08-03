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


class Solver:
    """
    Solver class deals with the path finding algorithm logic
    Initially it will implement Breadth First Search -> later it should be a parent class for a few pathfinding algo's
    """

    def __init__(self, maze):
        self.maze = maze
        self.start = None
        self.solution = None

    def find_start_pos(self):
        """Takes maze object and returns coordinates of starting position (denoted by "O")

        Returns:
            tuple: contains x, y coordinates of starting position
        """

        for i, row in enumerate(self.maze.maze):
            for j, value in enumerate(row):
                if value == self.maze.start_sign:
                    return (i, j)

    def find_neighbors(self, x, y):
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
                if self.maze.maze[pos[0]][pos[1]] == " ":
                    neighbors.append(pos)
            except IndexError:
                pass

        return neighbors

    def find_path(self):
        """Find the path (using BFS algo)

        Args:
            maze (list): maze object
            stdscr (Any): stdscr object
        """

        q = queue.Queue()  # initialise Queue object (FIFO)
        visited = set()
        # start_pos = self.find_start_pos(  # get starting position
        #     self.maze.maze, start=self.maze.start_sign
        # )
        start_pos = self.find_start_pos()

        q.put(  # put starting position in queue along with the path so far
            (start_pos, [start_pos])
        )

        while not q.empty():

            time.sleep(0.1)
            pos, path = q.get()
            row, col = pos
            path = list(path)
            visited.add((row, col))

            logging.info(f"visited: {visited}")
            logging.info(f"queue: {list(q.queue)}")
            logging.info(f"drawing path: {path}")
            self.maze.stdscr.clear()
            # self.maze.draw_maze(self.maze.maze, self.maze.stdscr, path)
            self.maze.path = path
            self.maze.draw_maze()
            self.maze.stdscr.refresh()
            if self.maze.maze[row][col] == self.maze.end_sign:
                logging.info(f"Found Solution! Maze ends at {row}, {col}")

                return (pos, path)
            else:
                neighbors = self.find_neighbors(x=row, y=col)
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
