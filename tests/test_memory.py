"""Tests for Memory module and classes."""

import pytest
from ktaned.bomb import Bomb
from ktaned.memory import Memory


@pytest.fixture
def memory():
    """A memory context appropriate for proper testing of all memory cases."""
    bomb = Bomb()
    memory = Memory(bomb)
    return memory


def test_add_stage(memory):
    """Test adding a stage."""
    display = 1
    buttons = [1, 2, 3, 4]

    memory.add_stage(display, buttons)

    actual = memory.stages
    expected = {
        0: {
            'display': display,
            'buttons': buttons,
            'solution': {'label': 2, 'position': 1},
        }
    }
    assert actual == expected


def test_set_stage(memory):
    """Test setting (overwriting) the stage."""
    display1 = 1
    buttons1 = [1, 2, 3, 4]
    display2 = 1
    buttons2 = [1, 2, 3, 4]

    memory.set_stage(0, display1, buttons1)
    memory.set_stage(1, display2, buttons2)

    actual = memory.stages
    expected = {
        0: {
            'display': display1,
            'buttons': buttons1,
            'solution': {'label': 2, 'position': 1},
        },
        1: {
            'display': display2,
            'buttons': buttons2,
            'solution': {'label': 4, 'position': 3},
        },
    }
    assert actual == expected


def test_set_stage_invalid_stage(memory):
    """Test setting the stage with an invalid stage."""
    display = 1
    buttons = [1, 2, 3, 4]

    with pytest.raises(Exception, message='stage must be of type int'):
        memory.set_stage('foo', display, buttons)

    with pytest.raises(Exception, message='stage must be between 0 and 4'):
        memory.set_stage(5, display, buttons)


def test_set_stage_invalid_display(memory):
    """Test setting the stage with an invalid display."""
    stage = 0
    buttons = [1, 2, 3, 4]

    with pytest.raises(Exception, message='display must be of type int'):
        memory.set_stage(stage, 'foo', buttons)

    with pytest.raises(Exception, message='display must be between 1 and 4'):
        memory.set_stage(stage, 0, buttons)


def test_set_stage_invalid_buttons(memory):
    """Test setting the stage with invalid buttons."""
    stage = 0
    display = 1

    expected_exception = 'buttons must be of type list'
    with pytest.raises(Exception, message=expected_exception):
        memory.set_stage(stage, display, '1, 2, 3, 4')

    expected_exception = 'buttons list must contain exactly 4 items'
    with pytest.raises(Exception, message=expected_exception):
        memory.set_stage(stage, display, [1, 2, 3])

    expected_exception = 'buttons list must contain one each of 1, 2, 3, 4'
    with pytest.raises(Exception, message=expected_exception):
        memory.set_stage(stage, display, [1, 2, 3, 1])

    expected_exception = 'buttons items must be of type int'
    with pytest.raises(Exception, message=expected_exception):
        memory.set_stage(stage, display, [1, 2, 3, '4'])

    expected_exception = 'buttons items must be between 1 and 4'
    with pytest.raises(Exception, message=expected_exception):
        memory.set_stage(stage, display, [1, 2, 3, 5])


def test_get_push(memory):
    """Test getting the push value of a given stage."""
    display = 1
    buttons = [1, 2, 3, 4]

    memory.add_stage(display, buttons)

    actual = memory.get_push(0)
    expected = {'label': 2, 'position': 1}
    assert actual == expected


def test_get_push_invalid_stage(memory):
    """Test getting the push value of a stage that has not yet been set."""
    display = 1
    buttons = [1, 2, 3, 4]

    memory.add_stage(display, buttons)

    with pytest.raises(Exception, message='stage key 1 is not set'):
        memory.get_push(1)


def test_solve(memory):
    """Test solving each stage.

    The number of possible combinations of stages is 8,153,726,976 if
    randomized button label positions are included (drops to 1,024 for
    non-randomized label positions), making testing every combination
    unfeasible, so we can only reasonably test each branch for each stage with
    a single branch from the previous stage(s).
    """
    # TODO: This could be done in a more readable way with some kind of mapping
    # TODO: Just how long *would* it take to go through 8 billion combos?

    buttons = [1, 2, 3, 4]

    stage = 0
    memory.set_stage(stage, 1, buttons)
    assert memory.get_push(stage) == {'position': 1, 'label': 2}
    memory.set_stage(stage, 2, buttons)
    assert memory.get_push(stage) == {'position': 1, 'label': 2}
    memory.set_stage(stage, 3, buttons)
    assert memory.get_push(stage) == {'position': 2, 'label': 3}
    memory.set_stage(stage, 4, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}

    stage = 1
    memory.set_stage(stage, 1, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 2, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 3, buttons)
    assert memory.get_push(stage) == {'position': 0, 'label': 1}
    memory.set_stage(stage, 4, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}

    stage = 2
    memory.set_stage(stage, 1, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 2, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 3, buttons)
    assert memory.get_push(stage) == {'position': 2, 'label': 3}
    memory.set_stage(stage, 4, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}

    stage = 3
    memory.set_stage(stage, 1, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 2, buttons)
    assert memory.get_push(stage) == {'position': 0, 'label': 1}
    memory.set_stage(stage, 3, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 4, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}

    stage = 4
    memory.set_stage(stage, 1, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 2, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 3, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
    memory.set_stage(stage, 4, buttons)
    assert memory.get_push(stage) == {'position': 3, 'label': 4}
