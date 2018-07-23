"""Tests for Button module and classes."""

import pytest
from ktaned.bomb import Bomb
from ktaned.button import Button


@pytest.fixture()
def bomb():
    """A bomb context appropriate for proper testing of all button cases.
    """
    bomb = Bomb()
    indicators = [
        {'label': 'FRK', 'lit': True},
        {'label': 'CAR', 'lit': True},
    ]
    bomb.set_indicators(indicators)
    battery_packs = [
        {'type': 'AA', 'quantity': 2},
        {'type': 'D', 'quantity': 1},
    ]
    bomb.set_battery_packs(battery_packs)
    bomb.set_ports(['DVI-D'])
    return bomb


def test_set_color(bomb):
    """Test setting the color of the button."""
    button = Button(bomb)
    for color in button.valid_colors:
        button.set_color(color)
        actual = button.color
        expected = color
        assert actual == expected


def test_set_color_invalid(bomb):
    """Test setting the color of the button to an invalid color."""
    button = Button(bomb)
    expected_exception = 'Color (chartreuse) must be one of {}'.format(
        button.valid_colors)
    with pytest.raises(Exception, message=expected_exception):
        button.set_color('chartreuse')


def test_set(bomb):
    """Test setting the label of the button."""
    button = Button(bomb)
    for label in button.valid_labels:
        button.set_label(label)
        actual = button.label
        expected = label
        assert actual == expected


def test_set_label_invalid(bomb):
    """Test setting the label of the button to an invalid label."""
    button = Button(bomb)
    expected_exception = 'Label (hello) must be one of {}'.format(
        button.valid_labels
    )
    with pytest.raises(Exception, message=expected_exception):
        button.set_label('hello')


def test_set_light_color(bomb):
    """Test setting the light color of the button."""
    button = Button(bomb)
    for light_color in button.valid_light_colors:
        button.set_light_color(light_color)
        actual = button.light_color
        expected = light_color
        assert actual == expected


def test_set_light_color_invalid(bomb):
    """Test setting the light color of the button to an invalid light color."""
    button = Button(bomb)
    expected_exception = 'Light color (chartreuse) must be one of {}'.format(
        button.valid_light_colors
    )
    with pytest.raises(Exception, message=expected_exception):
        button.set_light_color('chartreuse')


def test_get_action_hold_blue_abort(bomb):
    """Test getting the action (abort) of the button if it is blue and says
    abort.
    """
    button = Button(bomb)
    button.set_color('blue')
    button.set_label('abort')
    actual = button.get_action()
    expected = 'hold'
    assert actual == expected


def test_get_action_hold_white_car(bomb):
    """Test getting the action (hold) of the button if it is white and the bomb
    has a CAR indicator.
    """
    bomb.set_indicators([{'label': 'CAR', 'lit': True}])
    button = Button(bomb)
    button.set_color('white')
    button.set_label('abort')
    actual = button.get_action()
    expected = 'hold'
    assert actual == expected


def test_get_action_hold_yellow(bomb):
    """Test getting the action (hold) of the button if it is yellow."""
    bomb.set_battery_packs([{'type': 'AA', 'quantity': 2}])
    button = Button(bomb)
    button.set_label('abort')
    button.set_color('yellow')
    actual = button.get_action()
    expected = 'hold'
    assert actual == expected


def test_get_action_hold_elses(bomb):
    """Test getting the action (hold) of the button for other edge cases."""
    # HOLD: blue, abort label
    #  TAP: > 1 batteries, Detonate
    # HOLD: white, lit CAR indicator
    #  TAP: > 2 batteries, lit FRK indicator
    # HOLD: yellow
    #  TAP: red, Hold label
    bomb.set_battery_packs([{'type': 'AA', 'quantity': 2}])
    button = Button(bomb)
    button.set_color('blue')
    button.set_label('hold')
    actual = button.get_action()
    expected = 'hold'
    assert actual == expected


def test_get_action_tap_2batt_det(bomb):
    """Test getting the action (tap) of the button if it says Detonate and the
    bomb has two battery packs."""
    bomb.set_battery_packs([{'type': 'AA', 'quantity': 2}])
    button = Button(bomb)
    button.set_color('blue')
    button.set_label('Detonate')
    actual = button.get_action()
    expected = 'tap'
    assert actual == expected


def test_get_action_tap_3batt_frk(bomb):
    """Test getting the action (tap) of the button if the bomb has three
    battery packs and an FRK indicator."""
    button = Button(bomb)
    button.set_color('blue')
    button.set_label('hold')
    actual = button.get_action()
    expected = 'tap'
    assert actual == expected


def test_get_action_tap_red_hold(bomb):
    """Test getting the action (tap) of the button if it is red and says hold.
    """
    button = Button(bomb)
    button.set_color('red')
    button.set_label('hold')
    actual = button.get_action()
    expected = 'tap'
    assert actual == expected


def test_get_release_light_blue(bomb):
    """Test getting the release time of the button if the light color is blue.
    """
    button = Button(bomb)
    button.set_light_color('blue')
    actual = button.get_release()
    expected = 4
    assert actual == expected


def test_get_release_light_yellow(bomb):
    """Test getting the release time of the button if the light color is
    yellow.
    """
    button = Button(bomb)
    button.set_light_color('yellow')
    actual = button.get_release()
    expected = 5
    assert actual == expected


def test_get_release_light_red(bomb):
    """Test getting the release time of the button if the light color is red.
    """
    button = Button(bomb)
    button.set_light_color('red')
    actual = button.get_release()
    expected = 1
    assert actual == expected
