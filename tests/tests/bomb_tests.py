import ktaned
import unittest


class BombTestCase(unittest.TestCase):

    def test_add_battery_pack(self):
        bomb = ktaned.Bomb()
        pack1 = {'type': 'AA', 'quantity': 2}
        pack2 = {'type': 'D', 'quantity': 1}

        bomb.add_battery_pack(pack1['type'], pack1['quantity'])
        actual = bomb.battery_packs
        expected = [pack1]
        self.assertEqual(actual, expected)

        bomb.add_battery_pack(pack2['type'], pack2['quantity'])
        actual = bomb.battery_packs
        expected = [pack1, pack2]
        self.assertEqual(actual, expected)

    def test_add_battery_pack_invalid_type(self):
        bomb = ktaned.Bomb()
        with self.assertRaises(Exception) as context:
            bomb.add_battery_pack('C', 2)
        actual = str(context.exception)
        expected = "Battery type (C) must be one of ['AA', 'D']"
        self.assertEqual(actual, expected)

    def test_add_battery_pack_invalid_quantity(self):
        bomb = ktaned.Bomb()
        with self.assertRaises(Exception) as context:
            bomb.add_battery_pack('AA', -1)
        actual = str(context.exception)
        expected = 'Battery packs must have at least one battery'
        self.assertEqual(actual, expected)

    def test_set_battery_packs(self):
        bomb = ktaned.Bomb()

        packs1 = [{'type': 'AA', 'quantity': 2},
                  {'type': 'D', 'quantity': 1}]
        packs2 = [{'type': 'D', 'quantity': 2},
                  {'type': 'AA', 'quantity': 3}]

        bomb.set_battery_packs(packs1)

        actual = bomb.battery_packs
        expected = packs1
        self.assertEqual(actual, expected)

        bomb.set_battery_packs(packs2)

        actual = bomb.battery_packs
        expected = packs2
        self.assertEqual(actual, expected)

    def test_get_battery_count(self):
        bomb = ktaned.Bomb()

        packs = [{'type': 'AA', 'quantity': 2},
                 {'type': 'D', 'quantity': 1}]

        bomb.set_battery_packs(packs)

        actual = bomb.get_battery_count()
        expected = 3
        self.assertEqual(actual, expected)

    def test_add_port(self):
        bomb = ktaned.Bomb()

        port1 = 'RJ-45'
        port2 = 'PS/2'

        bomb.add_port(port1)

        actual = bomb.ports
        expected = [port1]
        self.assertEqual(actual, expected)

        bomb.add_port(port2)

        actual = bomb.ports
        expected = [port1, port2]
        self.assertEqual(actual, expected)

    def test_add_port_invalid(self):
        bomb = ktaned.Bomb()
        with self.assertRaises(Exception) as context:
            bomb.add_port('USB-C')
        actual = str(context.exception)
        expected = ("Port (USB-C) must be one of ['DVI-D', 'Parallel', 'PS/2', 'RJ-45', 'Serial', 'Stereo RCA']")
        self.assertEqual(actual, expected)

    def test_set_ports(self):
        bomb = ktaned.Bomb()

        ports1 = ['RJ-45', 'PS/2']
        ports2 = ['DVI-D', 'Parallel']

        bomb.set_ports(ports1)

        actual = bomb.ports
        expected = ports1
        self.assertEqual(actual, expected)

        bomb.set_ports(ports2)

        actual = bomb.ports
        expected = ports2
        self.assertEqual(actual, expected)

    def test_add_indicator(self):
        bomb = ktaned.Bomb()

        indicator1 = {'label': 'FRK', 'lit': True}
        indicator2 = {'label': 'BOB', 'lit': False}

        bomb.add_indicator(indicator1['label'], indicator1['lit'])
        actual = bomb.indicators
        expected = [indicator1]
        self.assertEqual(actual, expected)

        bomb.add_indicator(indicator2['label'], indicator2['lit'])
        actual = bomb.indicators
        expected = [indicator1, indicator2]
        self.assertEqual(actual, expected)

    def test_add_indicator_invalid_label(self):
        bomb = ktaned.Bomb()
        with self.assertRaises(Exception) as context:
            bomb.add_indicator('ASDF', True)
        actual = str(context.exception)
        expected = ("Indicator \"label\" property must be one of ['SND', 'CLR', 'CAR', 'IND', 'FRQ', 'SIG', 'NSA', 'MSA', 'TRN', 'BOB', 'FRK']")
        self.assertEqual(actual, expected)

    def test_set_indicators(self):
        bomb = ktaned.Bomb()
        indicators = [{'label': 'FRK', 'lit': True},
                      {'label': 'BOB', 'lit': False}]
        bomb.set_indicators(indicators)

        actual = bomb.indicators
        expected = indicators
        self.assertEqual(actual, expected)

    def test_get_indicator_labels(self):
        bomb = ktaned.Bomb()
        indicators = [{'label': 'FRK', 'lit': True},
                      {'label': 'BOB', 'lit': False}]
        bomb.set_indicators(indicators)

        actual = bomb.get_indicator_labels()
        expected = [d['label'] for d in indicators]
        self.assertEqual(actual, expected)

    def test_get_indicator_labels_lit(self):
        bomb = ktaned.Bomb()
        indicators = [{'label': 'FRK', 'lit': True},
                      {'label': 'BOB', 'lit': False}]
        bomb.set_indicators(indicators)

        actual = bomb.get_indicator_labels(lit=True)
        expected = ['FRK']
        self.assertEqual(actual, expected)

    def test_get_indicator_labels_unlit(self):
        bomb = ktaned.Bomb()
        indicators = [{'label': 'FRK', 'lit': True},
                      {'label': 'BOB', 'lit': False}]
        bomb.set_indicators(indicators)

        actual = bomb.get_indicator_labels(lit=False)
        expected = ['BOB']
        self.assertEqual(actual, expected)

    def test_serial_has_vowel(self):
        bomb = ktaned.Bomb()

        vowels = ['a', 'e', 'i', 'o', 'u']

        for vowel in vowels:

            bomb.serial = '{}bcdfghjklmnpqrstvwxyz1234567890'.format(vowel)

            actual = bomb.check_serial_for_vowel()
            expected = True
            self.assertEqual(actual, expected)

    def test_serial_has_no_vowel(self):
        bomb = ktaned.Bomb()

        bomb.serial = 'bcdfghjklmnpqrstvwxyz1234567890'

        actual = bomb.check_serial_for_vowel()
        expected = False
        self.assertEqual(actual, expected)

    def test_serial_ends_in_odd(self):
        bomb = ktaned.Bomb()

        bomb.serial = 'abc123'

        actual = bomb.check_serial_ends_odd()
        expected = True
        self.assertEqual(actual, expected)

    def test_serial_does_not_end_in_odd(self):
        bomb = ktaned.Bomb()

        bomb.serial = 'abc234'

        actual = bomb.check_serial_ends_odd()
        expected = False
        self.assertEqual(actual, expected)

    def test_add_strikes(self):
        bomb = ktaned.Bomb()
        bomb.add_strikes()

        actual = bomb.strikes
        expected = 1
        self.assertEqual(actual, expected)

    def test_set_strikes(self):
        bomb = ktaned.Bomb()
        bomb.add_strikes(2)
        bomb.set_strikes(1)

        actual = bomb.strikes
        expected = 1
        self.assertEqual(actual, expected)

    def test_kaboom(self):
        bomb = ktaned.Bomb()

        with self.assertRaises(Exception) as context:
            bomb.add_strikes(3)

        actual = str(context.exception)
        expected = bomb.explode_messages
        self.assertIn(actual, expected)
