import ktaned
import unittest


class MazeTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maze(self):

        bomb = ktaned.Bomb()

        bomb.serial = 'abc123'
        bomb.batteries = True
        bomb.labels = ['FRK']

        maze = ktaned.Maze(bomb)

        maze.set_start((0, 0))
        maze.set_goal((10, 10))
        maze.set_greens([(10, 4), (0, 2)])

        actual = maze.solve()
        expected = [(0, 0),
                    (1, 0),
                    (2, 0),
                    (3, 0),
                    (4, 0),
                    (4, 1),
                    (4, 2),
                    (3, 2),
                    (2, 2),
                    (2, 3),
                    (2, 4),
                    (3, 4),
                    (4, 4),
                    (4, 5),
                    (4, 6),
                    (5, 6),
                    (6, 6),
                    (6, 5),
                    (6, 4),
                    (7, 4),
                    (8, 4),
                    (9, 4),
                    (10, 4),
                    (10, 5),
                    (10, 6),
                    (10, 7),
                    (10, 8),
                    (10, 9),
                    (10, 10)]
        self.assertEqual(actual, expected)
