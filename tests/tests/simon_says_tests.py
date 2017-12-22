import ktaned
import unittest


class SimonSaysTestCase(unittest.TestCase):

    def setUp(self):
        bomb = ktaned.Bomb()
        self.bomb = bomb
        self.bomb.serial = 'zzz123'  # No vowel by default

    def test_add_light_color(self):
        simon = ktaned.SimonSays(self.bomb)
        simon.add_light_color('red')

        actual = simon.get_push_sequence()
        expected = ['blue']
        self.assertEqual(actual, expected)

    def test_add_light_color_invalid(self):
        simon = ktaned.SimonSays(self.bomb)

        with self.assertRaises(Exception) as context:
            simon.add_light_color('chartreuse')
        actual = str(context.exception)
        expected = 'Color (chartreuse) must be one of {}'.format(
            simon.valid_colors)
        self.assertEqual(actual, expected)

    def test_set_light_sequence(self):
        simon = ktaned.SimonSays(self.bomb)
        colors = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(colors)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.light_sequence
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
        self.bomb.add_strikes(1)
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['red', 'blue', 'yellow', 'green', 'red']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_2_strikes(self):
        self.bomb.add_strikes(2)
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['yellow', 'green', 'blue', 'red', 'yellow']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_vowel_0_strikes(self):
        self.bomb.serial = 'abc123'  # Checking sequences with vowel in serial
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['blue', 'red', 'yellow', 'green', 'blue']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_vowel_1_strikes(self):
        self.bomb.serial = 'abc123'  # Checking sequences with vowel in serial
        self.bomb.add_strikes(1)
        simon = ktaned.SimonSays(self.bomb)

        light_sequence = ['red', 'blue', 'green', 'yellow', 'red']
        simon.set_light_sequence(light_sequence)

        actual = simon.get_push_sequence()
        expected = ['yellow', 'green', 'blue', 'red', 'yellow']
        self.assertEqual(actual, expected)

    def test_get_push_sequence_vowel_2_strikes(self):
        self.bomb.serial = 'abc123'  # Checking sequences with vowel in serial
        self.bomb.add_strikes(2)
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
        simon.add_light_color('red')

        actual = simon.get_push_sequence()
        expected = ['blue']
        self.assertEqual(actual, expected)