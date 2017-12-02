import ktaned
import unittest


class MazeTestCase(unittest.TestCase):
    def setUp(self):
        self.bomb = ktaned.Bomb()
        self.test_mazes = [
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(0, 2), (10, 4)],
                'data': [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]],
                'instructions': ['right', 'right', 'down', 'left', 'down', 'right', 'down', 'right', 'up', 'right', 'right', 'down', 'down', 'down'],
                'path': [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(8, 2), (2, 6)],
                'data': [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
                'instructions': ['right', 'down', 'left', 'down', 'down', 'right', 'up', 'right', 'up', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'down', 'down'],
                'path': [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (2, 5), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (5, 2), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (9, 2), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(6, 6), (10, 6)],
                'data': [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]],
                'instructions': ['right', 'right', 'down', 'down', 'down', 'down', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'right', 'right', 'right', 'up', 'up', 'up', 'right', 'down', 'down', 'down', 'right'],
                'path': [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (3, 8), (2, 8), (2, 7), (2, 6), (2, 5), (2, 4), (1, 4), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (7, 4), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (9, 10), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(0, 0), (0, 6)],
                'data': [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]],
                'instructions': ['right', 'down', 'down', 'right', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'down'],
                'path': [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(8, 4), (6, 10)],
                'data': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                'instructions': ['right', 'right', 'right', 'right', 'down', 'left', 'left', 'left', 'left', 'down', 'right', 'down', 'right', 'right', 'down', 'left', 'left', 'down', 'right', 'right', 'right', 'right'],
                'path': [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 7), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (2, 9), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(8, 0), (4, 8)],
                'data': [[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]],
                'instructions': ['down', 'down', 'down', 'right', 'down', 'left', 'down', 'right', 'right', 'right', 'up', 'up', 'up', 'up', 'right', 'up', 'right', 'down', 'down', 'left', 'down', 'down', 'right', 'down'],
                'path': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (2, 7), (2, 8), (1, 8), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (7, 2), (8, 2), (8, 1), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (9, 4), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 8), (10, 8), (10, 9), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(2, 0), (2, 10)],
                'data': [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                'instructions': ['right', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'down', 'left', 'down', 'left', 'left', 'down', 'right', 'right', 'down', 'right'],
                'path': [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, 1), (6, 2), (7, 2), (8, 2), (8, 1), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (9, 4), (8, 4), (8, 5), (8, 6), (7, 6), (6, 6), (5, 6), (4, 6), (4, 7), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 9), (8, 10), (9, 10), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(6, 0), (4, 6)],
                'data': [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                'instructions': ['down', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'right'],
                'path': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10)]
            },
            {
                'start': (0, 0),
                'goal': (10, 10),
                'greens': [(4, 2), (0, 8)],
                'data': [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]],
                'instructions': ['down', 'down', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'down'],
                'path': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
            }]

    def tearDown(self):
        pass

    def test_find_maze(self):
        maze = ktaned.Maze(self.bomb)
        loaded_mazes = maze.load_mazes()

        for test_maze in self.test_mazes:
            maze.set_greens(test_maze['greens'])

            actual = maze.find_maze()
            expected = test_maze['data']
            self.assertEqual(actual, expected)

    def test_find_maze_not_found(self):
        maze = ktaned.Maze(self.bomb)
        maze.set_greens([(10, 10), (0, 0)])  # greens won't match any maze

        with self.assertRaises(Exception) as context:
            maze.find_maze()

        actual = str(context.exception)
        expected = 'No maze found for greens {}'.format(maze.greens)

        self.assertEqual(actual, expected)

    def test_add_green(self):
        greens = [(0, 1), (2, 3)]
        maze = ktaned.Maze(self.bomb)

        maze.add_green(greens[0])
        actual = maze.greens
        expected = [greens[0]]

        self.assertEqual(actual, expected)

        maze.add_green(greens[1])
        actual = maze.greens
        expected = greens

        self.assertEqual(actual, expected)

    def test_set_greens(self):
        greens = [(0, 1), (2, 3)]
        maze = ktaned.Maze(self.bomb)
        maze.set_greens(greens)

        actual = maze.greens
        expected = greens

        self.assertEqual(actual, expected)

    def test_set_goal(self):
        goal = (0, 1)
        maze = ktaned.Maze(self.bomb)
        maze.set_goal(goal)

        actual = maze.goal
        expected = goal

        self.assertEqual(actual, expected)

    def test_set_start(self):
        start = (0, 1)
        maze = ktaned.Maze(self.bomb)
        maze.set_start(start)

        actual = maze.start
        expected = start

        self.assertEqual(actual, expected)

    def test_load_mazes(self):
        maze = ktaned.Maze(self.bomb)
        popped_test_mazes = []
        for test_maze in self.test_mazes:
            test_maze.pop('start')
            test_maze.pop('goal')
            test_maze.pop('path')
            test_maze.pop('instructions')
            popped_test_mazes.append(test_maze)

        actual = maze.load_mazes()
        expected = popped_test_mazes

        self.assertEqual(actual, expected)

    def test_find_path(self):

        for test_maze in self.test_mazes:
            maze = ktaned.Maze(self.bomb)

            maze.set_start(test_maze['start'])
            maze.set_goal(test_maze['goal'])
            maze.set_greens(test_maze['greens'])

            actual = maze.find_path()
            expected = test_maze['path']

            self.assertEqual(actual, expected)

    def test_get_instructions(self):
        test_maze = self.test_mazes[0]
        path = test_maze['path']

        maze = ktaned.Maze(self.bomb)
        actual = maze.get_instructions(path)
        expected = test_maze['instructions']

        self.assertEqual(actual, expected)
