"""Tests for Bomb module and classes."""

import pytest
from ktaned.bomb import Bomb


@pytest.fixture()
def bomb():
    """Bomb context appropriate for testing all bomb cases."""
    bomb = Bomb()
    return bomb


def test_add_battery_pack(bomb):
    """Test adding battery packs to the bomb."""
    pack1 = {'type': 'AA', 'quantity': 2}
    pack2 = {'type': 'D', 'quantity': 1}

    bomb.add_battery_pack(pack1['type'], pack1['quantity'])
    actual = bomb.battery_packs
    expected = [pack1]
    assert actual == expected

    bomb.add_battery_pack(pack2['type'], pack2['quantity'])
    actual = bomb.battery_packs
    expected = [pack1, pack2]
    assert actual == expected


def test_add_battery_pack_invalid_t(bomb):
    """Test adding battery a pack with invalid battery type to the bomb."""
    expected_exception = "Battery type (C) must be one of ['AA', 'D']"
    with pytest.raises(Exception, message=expected_exception):
        bomb.add_battery_pack('C', 2)


def test_add_battery_pack_invalid_q(bomb):
    """Test adding a battery pack with invalid quantity to the bomb."""
    expected_exception = 'Battery packs must have at least one battery'
    with pytest.raises(Exception, message=expected_exception):
        bomb.add_battery_pack('AA', -1)


def test_set_battery_packs(bomb):
    """Test setting (overwriting) battery packs that have been previously set
    on the bomb.
    """
    packs_original = [
        {'type': 'AA', 'quantity': 2},
        {'type': 'D', 'quantity': 1}
    ]
    packs_new = [
        {'type': 'D', 'quantity': 2},
        {'type': 'AA', 'quantity': 3}
    ]

    bomb.set_battery_packs(packs_original)
    actual = bomb.battery_packs
    expected = packs_original
    assert actual == expected

    bomb.set_battery_packs(packs_new)
    actual = bomb.battery_packs
    expected = packs_new
    assert actual == expected


def test_get_battery_count(bomb):
    """Test getting battery packs that have been set on the bomb."""
    packs = [{'type': 'AA', 'quantity': 2}, {'type': 'D', 'quantity': 1}]
    bomb.set_battery_packs(packs)
    actual = bomb.get_battery_count()
    expected = 3
    assert actual == expected


def test_add_port(bomb):
    """Test adding ports to the bomb."""
    port1 = 'RJ-45'
    port2 = 'PS/2'

    bomb.add_port(port1)
    actual = bomb.ports
    expected = [port1]
    assert actual == expected

    bomb.add_port(port2)
    actual = bomb.ports
    expected = [port1, port2]
    assert actual == expected


def test_add_port_invalid(bomb):
    """Test adding an invalid port to the bomb."""
    valid_ports = ['DVI-D', 'Parallel', 'PS/2',
                   'RJ-45', 'Serial', 'Stereo RCA']
    expected_exception = 'Port (USB-C) must be one of {}'.format(
        str(valid_ports))
    with pytest.raises(Exception, message=expected_exception):
        bomb.add_port('USB-C')


def test_set_ports(bomb):
    """Test setting (overwriting) ports that have been set on the
    bomb previously
    """
    ports_original = ['RJ-45', 'PS/2']
    ports_new = ['DVI-D', 'Parallel']

    bomb.set_ports(ports_original)
    actual = bomb.ports
    expected = ports_original
    assert actual == expected

    bomb.set_ports(ports_new)
    actual = bomb.ports
    expected = ports_new
    assert actual == expected


def test_add_indicator(bomb):
    """Test adding indicators to the bomb."""
    indicator1 = {'label': 'FRK', 'lit': True}
    indicator2 = {'label': 'BOB', 'lit': False}

    bomb.add_indicator(indicator1['label'], indicator1['lit'])
    actual = bomb.indicators
    expected = [indicator1]
    assert actual == expected

    bomb.add_indicator(indicator2['label'], indicator2['lit'])
    actual = bomb.indicators
    expected = [indicator1, indicator2]
    assert actual == expected


def test_add_indicator_invalid_l(bomb):
    """Test adding an indicator with an invalid label to the bomb."""
    valid_labels = ['SND', 'CLR', 'CAR', 'IND', 'FRQ',
                    'SIG', 'NSA', 'MSA', 'TRN', 'BOB', 'FRK']
    expected_exception = 'Indicator "label" property must be one of {}'.format(
        str(valid_labels))
    with pytest.raises(Exception, message=expected_exception):
        bomb.add_indicator('ASDF', True)


def test_set_indicators(bomb):
    """Test setting (overwriting) indicators that have been previously set on
    the bomb.
    """
    indicators = [
        {'label': 'FRK', 'lit': True},
        {'label': 'BOB', 'lit': False}
    ]
    bomb.set_indicators(indicators)
    actual = bomb.indicators
    expected = indicators
    assert actual == expected


def test_get_indicator_labels(bomb):
    """Test getting labels for all indicators that have been added to the bomb.
    """
    indicators = [
        {'label': 'FRK', 'lit': True},
        {'label': 'BOB', 'lit': False}
    ]
    bomb.set_indicators(indicators)
    actual = bomb.get_indicator_labels()
    expected = [d['label'] for d in indicators]
    assert actual == expected


def test_get_indicator_labels_lit(bomb):
    """Test getting labels for indicators which are lit that have been added to
    the bomb.
    """
    indicators = [
        {'label': 'FRK', 'lit': True},
        {'label': 'BOB', 'lit': False}
    ]
    bomb.set_indicators(indicators)
    actual = bomb.get_indicator_labels(lit=True)
    expected = ['FRK']
    assert actual == expected


def test_get_indicator_labels_unlit(bomb):
    """Test getting labels for indicators which are not lit that have been
    added to the bomb.
    """
    indicators = [
        {'label': 'FRK', 'lit': True},
        {'label': 'BOB', 'lit': False}
    ]
    bomb.set_indicators(indicators)
    actual = bomb.get_indicator_labels(lit=False)
    expected = ['BOB']
    assert actual == expected


def test_serial_has_vowel(bomb):
    """Test checking if a serial number has vowels (curiously there is no
    mention of whether 'y' is a vowel in the KTANE manual).
    """
    # TODO: determine if Y is considered a value
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        bomb.serial = '{}bcdfghjklmnpqrstvwxyz1234567890'.format(vowel)
        actual = bomb.check_serial_for_vowel()
        expected = True
        assert actual == expected


def test_serial_has_no_vowel(bomb):
    """Test checking that the bomb's serial number has no values."""
    # TODO: this should actually throw an error, because it's too long!
    bomb.serial = 'bcdfghjklmnpqrstvwxyz1234567890'
    actual = bomb.check_serial_for_vowel()
    expected = False
    assert actual == expected


def test_serial_ends_in_odd(bomb):
    """Test checking that the bomb's serial ends in an odd number."""
    bomb.serial = 'abc123'
    actual = bomb.check_serial_ends_odd()
    expected = True
    assert actual == expected


def test_serial_does_not_end_in_odd(bomb):
    """Test checking that the bomb's serial does not end in an odd number."""
    bomb.serial = 'abc234'
    actual = bomb.check_serial_ends_odd()
    expected = False
    assert actual == expected


def test_add_strikes(bomb):
    """Test adding strikes to the bomb."""
    bomb.add_strikes()
    actual = bomb.strikes
    expected = 1
    assert actual == expected

    bomb.add_strikes()
    actual = bomb.strikes
    expected = 2
    assert actual == expected


def test_set_strikes(bomb):
    """Test setting (overwriting) strikes that have been previously set on the
    bomb.
    """
    bomb.add_strikes(2)
    bomb.set_strikes(1)
    actual = bomb.strikes
    expected = 1
    assert actual == expected


def test_kaboom(bomb):
    """Test blowing up the bomb by adding too many strikes to it."""
    # TODO: should this really raise an exception?
    with pytest.raises(Exception, message='Kaboom! You have exploded.'):
        bomb.add_strikes(3)
