"""Tests for Simple Wires module and classes."""

import pytest
from ktaned.bomb import Bomb
from ktaned.simple_wires import SimpleWires


@pytest.fixture()
def bomb():
    """Bomb context appropriate for testing all simple wires cases."""
    bomb = Bomb()
    bomb.serial = 'abc123'
    bomb.batteries = True
    bomb.labels = ['FRK']
    return bomb


def test_simple_wires(bomb):
    """Basic simple wires test."""
    # TODO: add more comprehensive test suite.

    simple_wires = SimpleWires(bomb)

    wires = ['red', 'red', 'blue']
    simple_wires.set_wires(wires)

    # Solution should be third wire
    actual = simple_wires.solve()
    expected = 3
    assert actual == expected
