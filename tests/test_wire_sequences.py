"""Tests for wire sequences module"""

import pytest
from ktaned.bomb import Bomb
from ktaned.wire_sequences import WireSequences


@pytest.fixture()
def bomb():
    """A bomb context appropriate for proper testing of all wire sequences
    cases.
    """
    bomb = Bomb()
    return bomb


@pytest.fixture()
def cuts():
    """Hand crafted validated result sets for cuts on each wire sequence. The
    named key represents the color of the wire, the index of the list
    represents how many times that wire color has appeared, and the list of
    values represent you should cut the wire if it is connected to that letter.

    e.g. "third time I've seen a red wire, it's connected to letter c" would
    map to cuts['red'][3], which contains ['a', 'c'], so should be cut.
    """
    cuts = {
        'red': [
            ['c'],
            ['b'],
            ['a'],
            ['a', 'c'],
            ['b'],
            ['a', 'c'],
            ['a', 'b', 'c'],
            ['a', 'b'],
            ['b'],
        ],
        'blue': [
            ['b'],
            ['a', 'c'],
            ['b'],
            ['a'],
            ['b'],
            ['b', 'c'],
            ['c'],
            ['a', 'c'],
            ['a'],
        ],
        'black': [
            ['a', 'b', 'c'],
            ['a', 'c'],
            ['b'],
            ['a', 'c'],
            ['b'],
            ['b', 'c'],
            ['a', 'b'],
            ['c'],
            ['c'],
        ],
    }
    return cuts


def test_add_wire_invalid_color(bomb):
    """Test adding a wire to a sequence with an invalid color."""
    wire_sequences = WireSequences(bomb)
    expected_exception = 'Color (chartreuse) must be one of {}'.format(
        wire_sequences.valid_colors)
    with pytest.raises(Exception, message=expected_exception):
        wire_sequences.add_wire('chartreuse', 'c')


def test_add_wire_invalid_letter(bomb):
    """Test adding a wire to a sequence connected to an invalid letter."""
    wire_sequences = WireSequences(bomb)
    expected_exception = 'Letter (d) must be one of {}'.format(
        wire_sequences.valid_letters)
    with pytest.raises(Exception, message=expected_exception):
        wire_sequences.add_wire('red', 'd')


def test_add_wire_by_color_letter(bomb, cuts):
    """Test adding wire by color and letter (iterates through every color,
    letter, and appearance combination).
    """
    # TODO: actually iterate through every combination.
    for color in ['red', 'blue', 'black']:
        for letter in ['a', 'b', 'c']:
            wire_sequences = WireSequences(bomb)
            for cut in cuts[color]:
                actual = wire_sequences.add_wire(color, letter)
                expected = bool(letter in cut)
                assert actual == expected


def test_add_wire_mixed(bomb):
    """Test some random wire sequences."""
    wire_sequences = WireSequences(bomb)
    wires = [
        ('red', 'c', True),
        ('blue', 'a', False),
        ('black', 'b', True),
        ('blue', 'a', True),
        ('red', 'c', False),
        ('black', 'b', False),
        ('red', 'a', True),
        ('blue', 'c', False),
        ('black', 'b', True),
    ]

    for wire in wires:
        color, letter, cut = wire
        actual = wire_sequences.add_wire(color, letter)
        expected = cut
        assert actual == expected
