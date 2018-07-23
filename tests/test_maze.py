"""Tests for Maze module and classes."""

import pytest
from ktaned.bomb import Bomb
from ktaned.maze import Maze


@pytest.fixture()
def bomb():
    """A bomb context appropriate for proper testing of all maze cases."""
    bomb = Bomb()
    return bomb


@pytest.fixture()
def test_mazes():
    """Hand crafted validated result sets for each maze"""
    # TODO: is there a better way to test construct this test data?
    test_mazes = [
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(0, 2), (10, 4)],
            'data': [
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            ],
            'instructions': [
                'right',
                'right',
                'down',
                'left',
                'down',
                'right',
                'down',
                'right',
                'up',
                'right',
                'right',
                'down',
                'down',
                'down',
            ],
            'path': [
                (0, 0),
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
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(8, 2), (2, 6)],
            'data': [
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            ],
            'instructions': [
                'right',
                'down',
                'left',
                'down',
                'down',
                'right',
                'up',
                'right',
                'up',
                'right',
                'up',
                'right',
                'down',
                'right',
                'down',
                'down',
                'down',
                'down',
            ],
            'path': [
                (0, 0),
                (1, 0),
                (2, 0),
                (2, 1),
                (2, 2),
                (1, 2),
                (0, 2),
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (1, 6),
                (2, 6),
                (2, 5),
                (2, 4),
                (3, 4),
                (4, 4),
                (4, 3),
                (4, 2),
                (5, 2),
                (6, 2),
                (6, 1),
                (6, 0),
                (7, 0),
                (8, 0),
                (8, 1),
                (8, 2),
                (9, 2),
                (10, 2),
                (10, 3),
                (10, 4),
                (10, 5),
                (10, 6),
                (10, 7),
                (10, 8),
                (10, 9),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(6, 6), (10, 6)],
            'data': [
                [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            ],
            'instructions': [
                'right',
                'right',
                'down',
                'down',
                'down',
                'down',
                'left',
                'up',
                'up',
                'left',
                'down',
                'down',
                'down',
                'right',
                'right',
                'right',
                'up',
                'up',
                'up',
                'right',
                'down',
                'down',
                'down',
                'right',
            ],
            'path': [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (4, 1),
                (4, 2),
                (4, 3),
                (4, 4),
                (4, 5),
                (4, 6),
                (4, 7),
                (4, 8),
                (3, 8),
                (2, 8),
                (2, 7),
                (2, 6),
                (2, 5),
                (2, 4),
                (1, 4),
                (0, 4),
                (0, 5),
                (0, 6),
                (0, 7),
                (0, 8),
                (0, 9),
                (0, 10),
                (1, 10),
                (2, 10),
                (3, 10),
                (4, 10),
                (5, 10),
                (6, 10),
                (6, 9),
                (6, 8),
                (6, 7),
                (6, 6),
                (6, 5),
                (6, 4),
                (7, 4),
                (8, 4),
                (8, 5),
                (8, 6),
                (8, 7),
                (8, 8),
                (8, 9),
                (8, 10),
                (9, 10),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(0, 0), (0, 6)],
            'data': [
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            ],
            'instructions': [
                'right',
                'down',
                'down',
                'right',
                'up',
                'right',
                'right',
                'right',
                'down',
                'down',
                'down',
                'down',
            ],
            'path': [
                (0, 0),
                (1, 0),
                (2, 0),
                (2, 1),
                (2, 2),
                (2, 3),
                (2, 4),
                (3, 4),
                (4, 4),
                (4, 3),
                (4, 2),
                (5, 2),
                (6, 2),
                (7, 2),
                (8, 2),
                (9, 2),
                (10, 2),
                (10, 3),
                (10, 4),
                (10, 5),
                (10, 6),
                (10, 7),
                (10, 8),
                (10, 9),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(8, 4), (6, 10)],
            'data': [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            'instructions': [
                'right',
                'right',
                'right',
                'right',
                'down',
                'left',
                'left',
                'left',
                'left',
                'down',
                'right',
                'down',
                'right',
                'right',
                'down',
                'left',
                'left',
                'down',
                'right',
                'right',
                'right',
                'right',
            ],
            'path': [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (5, 0),
                (6, 0),
                (7, 0),
                (8, 0),
                (8, 1),
                (8, 2),
                (7, 2),
                (6, 2),
                (5, 2),
                (4, 2),
                (3, 2),
                (2, 2),
                (1, 2),
                (0, 2),
                (0, 3),
                (0, 4),
                (1, 4),
                (2, 4),
                (2, 5),
                (2, 6),
                (3, 6),
                (4, 6),
                (5, 6),
                (6, 6),
                (6, 7),
                (6, 8),
                (5, 8),
                (4, 8),
                (3, 8),
                (2, 8),
                (2, 9),
                (2, 10),
                (3, 10),
                (4, 10),
                (5, 10),
                (6, 10),
                (7, 10),
                (8, 10),
                (9, 10),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(8, 0), (4, 8)],
            'data': [
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            ],
            'instructions': [
                'down',
                'down',
                'down',
                'right',
                'down',
                'left',
                'down',
                'right',
                'right',
                'right',
                'up',
                'up',
                'up',
                'up',
                'right',
                'up',
                'right',
                'down',
                'down',
                'left',
                'down',
                'down',
                'right',
                'down',
            ],
            'path': [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (1, 6),
                (2, 6),
                (2, 7),
                (2, 8),
                (1, 8),
                (0, 8),
                (0, 9),
                (0, 10),
                (1, 10),
                (2, 10),
                (3, 10),
                (4, 10),
                (5, 10),
                (6, 10),
                (6, 9),
                (6, 8),
                (6, 7),
                (6, 6),
                (6, 5),
                (6, 4),
                (6, 3),
                (6, 2),
                (7, 2),
                (8, 2),
                (8, 1),
                (8, 0),
                (9, 0),
                (10, 0),
                (10, 1),
                (10, 2),
                (10, 3),
                (10, 4),
                (9, 4),
                (8, 4),
                (8, 5),
                (8, 6),
                (8, 7),
                (8, 8),
                (9, 8),
                (10, 8),
                (10, 9),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(2, 0), (2, 10)],
            'data': [
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            'instructions': [
                'right',
                'right',
                'right',
                'down',
                'right',
                'up',
                'right',
                'down',
                'down',
                'left',
                'down',
                'left',
                'left',
                'down',
                'right',
                'right',
                'down',
                'right',
            ],
            'path': [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (5, 0),
                (6, 0),
                (6, 1),
                (6, 2),
                (7, 2),
                (8, 2),
                (8, 1),
                (8, 0),
                (9, 0),
                (10, 0),
                (10, 1),
                (10, 2),
                (10, 3),
                (10, 4),
                (9, 4),
                (8, 4),
                (8, 5),
                (8, 6),
                (7, 6),
                (6, 6),
                (5, 6),
                (4, 6),
                (4, 7),
                (4, 8),
                (5, 8),
                (6, 8),
                (7, 8),
                (8, 8),
                (8, 9),
                (8, 10),
                (9, 10),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(6, 0), (4, 6)],
            'data': [
                [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            'instructions': [
                'down',
                'down',
                'down',
                'down',
                'down',
                'right',
                'right',
                'right',
                'right',
                'right',
            ],
            'path': [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (0, 7),
                (0, 8),
                (0, 9),
                (0, 10),
                (1, 10),
                (2, 10),
                (3, 10),
                (4, 10),
                (5, 10),
                (6, 10),
                (7, 10),
                (8, 10),
                (9, 10),
                (10, 10),
            ],
        },
        {
            'start': (0, 0),
            'goal': (10, 10),
            'greens': [(4, 2), (0, 8)],
            'data': [
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            ],
            'instructions': [
                'down',
                'down',
                'right',
                'up',
                'up',
                'right',
                'right',
                'right',
                'right',
                'down',
                'down',
                'down',
                'down',
                'down',
            ],
            'path': [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (1, 4),
                (2, 4),
                (2, 3),
                (2, 2),
                (2, 1),
                (2, 0),
                (3, 0),
                (4, 0),
                (5, 0),
                (6, 0),
                (7, 0),
                (8, 0),
                (9, 0),
                (10, 0),
                (10, 1),
                (10, 2),
                (10, 3),
                (10, 4),
                (10, 5),
                (10, 6),
                (10, 7),
                (10, 8),
                (10, 9),
                (10, 10),
            ],
        },
    ]
    return test_mazes


def test_find_maze(bomb, test_mazes):
    """Test finding mazes."""
    maze = Maze(bomb)
    maze.load_mazes()

    for test_maze in test_mazes:
        maze.set_greens(test_maze['greens'])
        actual = maze.find_maze()
        expected = test_maze['data']
        assert actual == expected


def test_find_maze_not_found(bomb):
    """Test (not) finding a maze with invalid greens."""
    maze = Maze(bomb)
    maze.set_greens([(10, 10), (0, 0)])  # greens won't match any maze
    expected_exception = 'No maze found for greens {}'.format(maze.greens)
    with pytest.raises(Exception, message=expected_exception):
        maze.find_maze()


def test_add_green(bomb):
    """Test adding greens to a maze."""
    greens = [(0, 1), (2, 3)]
    maze = Maze(bomb)

    maze.add_green(greens[0])
    actual = maze.greens
    expected = [greens[0]]
    assert actual == expected

    maze.add_green(greens[1])
    actual = maze.greens
    expected = greens
    assert actual == expected


def test_set_greens(bomb):
    """Test setting (overwriting) greens on a maze."""
    maze = Maze(bomb)

    original_greens = [(0, 1), (2, 3)]
    maze.set_greens(original_greens)
    actual = maze.greens
    expected = original_greens
    assert actual == expected

    new_greens = [(4, 5), (6, 7)]
    maze.set_greens(new_greens)
    actual = maze.greens
    expected = new_greens
    assert actual == expected


def test_set_goal(bomb):
    """Test setting the goal for the maze."""
    goal = (0, 1)
    maze = Maze(bomb)

    maze.set_goal(goal)
    actual = maze.goal
    expected = goal
    assert actual == expected


def test_set_start(bomb):
    """Test setting the start for the maze."""
    start = (0, 1)
    maze = Maze(bomb)
    maze.set_start(start)

    actual = maze.start
    expected = start

    assert actual == expected


def test_load_mazes(bomb, test_mazes):
    """Test loading mazes from a file."""
    # TODO: this could probably be more thorough.
    maze = Maze(bomb)
    popped_test_mazes = []
    for test_maze in test_mazes:
        test_maze.pop('start')
        test_maze.pop('goal')
        test_maze.pop('path')
        test_maze.pop('instructions')
        popped_test_mazes.append(test_maze)

    actual = maze.load_mazes()
    expected = popped_test_mazes

    assert actual == expected


def test_find_path(bomb, test_mazes):
    """Test finding paths through each maze."""
    maze = Maze(bomb)
    for test_maze in test_mazes:
        maze.set_start(test_maze['start'])
        maze.set_goal(test_maze['goal'])
        maze.set_greens(test_maze['greens'])
        actual = maze.find_path()
        expected = test_maze['path']
        assert actual == expected


def test_get_instructions(bomb, test_mazes):
    """Test getting natural language instructions for solving a maze."""
    maze = Maze(bomb)

    test_maze = test_mazes[0]
    path = test_maze['path']

    actual = maze.get_instructions(path)
    expected = test_maze['instructions']
    assert actual == expected
