import ktaned
import unittest


class SimonSaysTestCase(unittest.TestCase):

    def setUp(self):
        bomb = ktaned.Bomb()
        self.bomb = bomb

    def test_add_light_color(self):
        simon = ktaned.SimonSays(self.bomb)
        simon.add_color('red')

        actual = simon.get_push_sequence()
        expected = ['blue']
        self.assertEqual(actual, expected)

    def test_add_light_color_invalid(self):
        simon = ktaned.SimonSays(self.bomb)
        simon.add_color('chartreuse')

        with self.assertRaises(Exception) as context:
            button.add_color('chartreuse')
        actual = str(context.exception)
        expected = 'Color (chartreuse) must be one of {}'.format(
            simon.valid_colors)
        self.assertEqual(actual, expected)

    def test_set_get_light_sequence(self):
        simon = ktaned.SimonSays(self.bomb)
        colors = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(colors)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_light_sequence()
        expected = light_sequence
        self.assertEqual(actual, expected)

    def test_get_push_sequence_0_strikes(self):
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['blue', 'yellow', 'green', 'red', 'blue']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_1_strikes(self):
        self.bomb.add_strike()
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['red', 'blue', 'yellow', 'green', 'red']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_2_strikes(self):
        self.bomb.add_strike()
        self.bomb.add_strike()
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['yellow', 'green', 'blue', 'red', 'yellow']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_vowel_0_strikes(self):
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['blue', 'red', 'yellow', 'green', 'blue']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_vowel_1_strikes(self):
        self.bomb.add_strike()
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['yellow', 'green', 'blue', 'red', 'yellow']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_vowel_2_strikes(self):
        self.bomb.add_strike()
        self.bomb.add_strike()
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['green', 'red', 'yellow', 'blue', 'green']
        self.assertEqual(actual, expected)

    def test_reset(self):
        simon = ktaned.SimonSays(self.bomb)
        simon.set_light_sequence(['green', 'blue'])
        simon.reset()
        simon.add_color('red')

        actual = simon.get_push_sequence()
        expected = ['blue']
        self.assertEqual(actual, expected)
