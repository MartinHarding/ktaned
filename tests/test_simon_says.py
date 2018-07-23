"""Tests for Simon Says module and classes."""

import pytest
from ktaned.bomb import Bomb
from ktaned.simon_says import SimonSays


@pytest.fixture()
def bomb():
    """A bomb context appropriate for proper testing of all simon says cases.
    """
    bomb = Bomb()
    bomb.serial = 'zzz123'  # No vowel by default
    return bomb


def test_add_light_color(bomb):
    """Test adding a light color blink."""
    simon = SimonSays(bomb)
    simon.add_light_color('red')

    actual = simon.get_push_sequence()
    expected = ['blue']
    assert actual == expected


def test_add_light_color_invalid(bomb):
    """Test adding a light color blink that is invalid."""
    simon = SimonSays(bomb)
    expected_exception = 'Color (chartreuse) must be one of {}'.format(
        simon.valid_colors)
    with pytest.raises(Exception, message=expected_exception):
        simon.add_light_color('chartreuse')


def test_set_light_sequence(bomb):
    """Test setting a sequence of light blinks."""

    simon = SimonSays(bomb)
    colors = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(colors)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.light_sequence
    expected = light_sequence
    assert actual == expected


def test_get_push_sequence_0s(bomb):
    """Test getting the push sequence with 0 strikes."""
    simon = SimonSays(bomb)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.get_push_sequence()
    expected = ['blue', 'yellow', 'green', 'red', 'blue']
    assert actual == expected


def test_get_push_sequence_1s(bomb):
    """Test getting the push sequence with 1 strikes."""
    bomb.add_strikes(1)
    simon = SimonSays(bomb)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.get_push_sequence()
    expected = ['red', 'blue', 'yellow', 'green', 'red']
    assert actual == expected


def test_get_push_sequence_2s(bomb):
    """Test getting the push sequence with 2 strikes."""
    bomb.add_strikes(2)
    simon = SimonSays(bomb)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.get_push_sequence()
    expected = ['yellow', 'green', 'blue', 'red', 'yellow']
    assert actual == expected


def test_get_push_sequence_0s_vow(bomb):
    """Test getting the push sequence with 0 strikes and a vowel in the bomb
    serial.
    """
    bomb.serial = 'abc123'
    simon = SimonSays(bomb)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.get_push_sequence()
    expected = ['blue', 'red', 'yellow', 'green', 'blue']
    assert actual == expected


def test_get_push_sequence_1s_vow(bomb):
    """Test getting the push sequence with 1 strikes and a vowel in the bomb
    serial.
    """
    bomb.serial = 'abc123'
    bomb.add_strikes(1)
    simon = SimonSays(bomb)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.get_push_sequence()
    expected = ['yellow', 'green', 'blue', 'red', 'yellow']
    assert actual == expected


def test_get_push_sequence_2s_vow(bomb):
    """Test getting the push sequence with 2 strikes and a vowel in the bomb
    serial.
    """
    bomb.serial = 'abc123'
    bomb.add_strikes(2)
    simon = SimonSays(bomb)

    light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
    simon.set_light_sequence(light_sequence)

    actual = simon.get_push_sequence()
    expected = ['green', 'red', 'yellow', 'blue', 'green']
    assert actual == expected


def test_reset(bomb):
    """Test reseting the simon says module."""
    simon = SimonSays(bomb)
    simon.set_light_sequence(['green', 'blue'])
    simon.reset()
    simon.add_light_color('red')

    actual = simon.get_push_sequence()
    expected = ['blue']
    assert actual == expected
