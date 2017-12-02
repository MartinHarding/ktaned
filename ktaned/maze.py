import pkg_resources
import yaml

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


class Maze(object):
    """docstring for Maze"""
    def __init__(self, bomb):
        super(Maze, self).__init__()
        self.bomb = bomb
        self.wires = []
        self.valid_colors = ['red', 'blue', 'yellow', 'white', 'black']
        self.greens = []

    def add_green(self, coordinates):
        """Add a green location for determining the maze to use in the solution

        Args:
            coordinates (tuple): a tuple representing (x,y) coordinates
        """
        if len(self.greens) > 1:
            raise Exception('You may not add more than two greens to a maze')
        self.greens.append(coordinates)

    def set_greens(self, greens):
        """Set green locations for determining the maze to use in the solution

        Args:
            greens (list): an array of tuples representing (x,y) coordinates

        """
        self.greens = []
        for coordinates in greens:
            self.add_green(coordinates)

    def set_goal(self, coordinates):
        """Set the goal (end) location for the path finding algorithm

        Args:
            coordinates (tuple): a tuple representing (x,y) coordinates
        """
        self.goal = coordinates

    def set_start(self, coordinates):
        """Set the start location for the path finding algorithm

        Args:
            coordinates (tuple): a tuple representing (x,y) coordinates
        """
        self.start = coordinates

    def find_maze(self):
        """Find a maze based on a set of 'greens' coordinates.

        Args:
            greens (list): an array of tuples representing (x,y) coordinates

        Returns:
            dict: a dictionary representing a maze

        """
        if not hasattr(self, 'greens'):
            raise Exception('Must set greens before finding a maze')

        if not hasattr(self, 'mazes'):
            self.mazes = self.load_mazes()

        for maze in self.mazes:
            # Sort the greens first, so it doesn't matter which order they were
            # entered in (since it'd be hard to determine a standard order)
            if sorted(self.greens) == sorted(maze['greens']):
                return maze['data']

        raise Exception('No maze found for greens {}'.format(self.greens))

    def load_mazes(self):
        """Load mazes from a terse-yaml file into a pathfinding-friendly format

        Returns:
            list: a list of dictionaries representing mazes

        """
        mazes = []
        mazes_yml = pkg_resources.resource_string(__name__, 'mazes.yml')
        mazes_raw = yaml.safe_load(mazes_yml)

        # Loop through all mazes in yaml file
        for maze_raw in mazes_raw['mazes']:

            # Setup maze dict
            maze = {'greens': [], 'data': []}

            # Split text blocks into rows on new line character
            rows = maze_raw.split('\n')
            for row_index, row in enumerate(rows):

                # Ignore empty new lines
                if row:

                    # Split into columns on spaces
                    columns = row.split(' ')
                    for column_index, column_value in enumerate(columns):

                        # If this coordinate was a * (green), then replace it
                        # with a 0 and append to the maze's greens coordinates
                        if column_value is '*':
                            maze['greens'].append((column_index, row_index))
                            columns[column_index] = 0
                            if len(maze['greens']) > 2:
                                raise Exception('Mazes may only have 2 greens')

                        # Ensure column is int
                        else:
                            columns[column_index] = int(column_value)

                    # Append the row columns to the maze dict
                    maze['data'].append(columns)

            # Append the maze dict to the mazes dictionary
            mazes.append(maze)

        # return the loaded mazes
        return mazes

    def find_path(self):
        if not len(self.greens) == 2:
            raise Exception('greens must be exactly two row and column tuples')
        maze = self.find_maze()
        grid = Grid(matrix=maze)

        if not hasattr(self, 'start') or type(self.start) is not tuple:
            raise Exception('Missing start row and column tuple')
        if not hasattr(self, 'goal') or type(self.goal) is not tuple:
            raise Exception('Missing goal row and column tuple')

        start = grid.node(self.start[0], self.start[1])
        goal = grid.node(self.goal[0], self.goal[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, goal, grid)

        # print('operations:', runs, 'path length:', len(path))
        # print(grid.grid_str(path=path, start=start, end=goal))
        # print(path)

        return path

    def get_instructions(self, path):

        # Since the mazes are encoded with exactly 2x resolution to support
        # arbitrarily thin walls, the path must be converted to exactly half
        # its original resolution
        resized_path = []
        for i in range(len(path)):
            if i % 2 == 0:
                resized_path.append(path[i])

        instructions = []

        for i in range(len(resized_path)-1):
            last_xy = resized_path[i]
            next_xy = resized_path[i+1]
            if last_xy[0] > next_xy[0]:
                instructions.append('left')
            elif last_xy[0] < next_xy[0]:
                instructions.append('right')
            elif last_xy[1] > next_xy[1]:
                instructions.append('up')
            elif last_xy[1] < next_xy[1]:
                instructions.append('down')
            elif last_xy[0] is next_xy[0] and last_xy[1] is next_xy[1]:
                raise Exception('Next instruction is same as last instruction')
            else:
                raise Exception('Encountered an invalid move instruction')

        return instructions
