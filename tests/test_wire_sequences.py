import ktaned
import unittest


class WireSequencesTestCase(unittest.TestCase):

    def setUp(self):
        self.bomb = ktaned.Bomb()
        self.cuts = {
            'red': [
                ['c'],
                ['b'],
                ['a'],
                ['a', 'c'],
                ['b'],
                ['a', 'c'],
                ['a', 'b', 'c'],
                ['a', 'b'],
                ['b']
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
                ['a']
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
                ['c']
            ]
        }

    def test_add_wire_invalid_color(self):

        wire_sequences = ktaned.WireSequences(self.bomb)

        with self.assertRaises(Exception) as context:
            wire_sequences.add_wire('chartreuse', 'c')

        actual = str(context.exception)
        expected = 'Color (chartreuse) must be one of {}'.format(
            wire_sequences.valid_colors)

        self.assertEqual(actual, expected)

    def test_add_wire_invalid_letter(self):

        wire_sequences = ktaned.WireSequences(self.bomb)

        with self.assertRaises(Exception) as context:
            wire_sequences.add_wire('red', 'd')

        actual = str(context.exception)
        expected = 'Letter (d) must be one of {}'.format(
            wire_sequences.valid_letters)

        self.assertEqual(actual, expected)

    def test_add_wire_by_color_letter(self):

        for color in ['red', 'blue', 'black']:
            for letter in ['a', 'b', 'c']:

                wire_sequences = ktaned.WireSequences(self.bomb)

                for index in range(0, 8):
                    cuts = self.cuts[color][index]

                    actual = wire_sequences.add_wire(color, letter)
                    expected = bool(letter in cuts)

                    self.assertEqual(actual, expected)

    def test_add_wire_mixed(self):

        wire_sequences = ktaned.WireSequences(self.bomb)

        wires = [('red', 'c', True),
                 ('blue', 'a', False),
                 ('black', 'b', True),
                 ('blue', 'a', True),
                 ('red', 'c', False),
                 ('black', 'b', False),
                 ('red', 'a', True),
                 ('blue', 'c', False),
                 ('black', 'b', True)]

        for wire in wires:
            color, letter, cut = wire

            actual = wire_sequences.add_wire(color, letter)
            expected = cut

            self.assertEqual(actual, expected)
