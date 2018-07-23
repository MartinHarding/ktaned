"""Tests for Password module and classes."""

import pytest
from ktaned.bomb import Bomb
from ktaned.password import Password


@pytest.fixture()
def bomb():
    """A bomb context appropriate for proper testing of all bomb cases."""
    bomb = Bomb()
    return bomb


def test_get_password_about(bomb):
    """Test getting potential passwords from a given set of columns of
    characters.

    The set of columns in this test is constructed so that it:
    - 1. uses every alphebetical character
    - 2. contains a single password possibility 'about'
    """
    # TODO: Add more comprehensive tests for false-positives?

    password = Password(bomb)
    columns = ['aetolz', 'cdbefg', 'hjklom', 'opqrsu', 'utvwxy']
    password.set_columns(columns)
    actual = password.get_possibilities()
    expected = ['about']
    assert actual == expected


def test_set_columns(bomb):
    """Test setting the password character columns."""
    password = Password(bomb)
    columns = ['abcdef', 'bhijkl', 'onopqp', 'urstuv', 'txyzac']
    password.set_columns(columns)
    actual = password.columns
    expected = columns
    assert actual == expected


def test_set_columns_invalid_char(bomb):
    """Test setting the password character columns with an invalid
    character.
    """
    password = Password(bomb)
    columns = ['abcdef', 'ghijkl', 'mnopqp', 'qrstuv', 'wxyza@']
    expected_exception = 'Character 4:5 (@) must be one of {}'.format(
        password.valid_characters)
    with pytest.raises(Exception, message=expected_exception):
        password.set_columns(columns)


def test_set_columns_invalid_length(bomb):
    """Test setting the password character columns with an invalid length.
    """
    password = Password(bomb)
    columns = ['a', 'g', 'a', 'i', 'n', 'e']
    expected_exception = 'Too many columns (must be 5 or less)'
    with pytest.raises(Exception, message=expected_exception):
        password.set_columns(columns)
