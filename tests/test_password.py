import ktaned
import unittest

class PasswordTestCase(unittest.TestCase):
    def setUp(self):
        self.bomb = ktaned.Bomb()

    def test_get_possibilities(self):
        password = ktaned.Password(self.bomb)

        # This set is constructed so that it (1) uses every alphebetical
        # character and (2) contains a single password possibility 'about'
        # TODO: Add more comprehensive tests for false-positives?
        columns = [
            'aetolz',
            'cdbefg',
            'hjklom',
            'opqrsu',
            'utvwxy'
        ]

        password.set_columns(columns)

        actual = password.get_possibilities()
        expected = ['about']

        self.assertEqual(actual, expected)

    def test_set_columns(self):
        password = ktaned.Password(self.bomb)

        columns = [
            'abcdef',
            'bhijkl',
            'onopqp',
            'urstuv',
            'txyzac'
        ]

        password.set_columns(columns)

        actual = password.columns
        expected = columns

        self.assertEqual(actual, expected)

    def test_set_columns_invalid_character(self):
        password = ktaned.Password(self.bomb)

        columns = [
            'abcdef',
            'ghijkl',
            'mnopqp',
            'qrstuv',
            'wxyza@'
        ]

        with self.assertRaises(Exception) as context:
            password.set_columns(columns)

        actual = str(context.exception)
        expected = 'Character 4:5 (@) must be one of {}'.format(
            password.valid_characters)

        self.assertEqual(actual, expected)

    def test_set_columns_invalid_length(self):
        password = ktaned.Password(self.bomb)

        columns = ['a', 'g', 'a', 'i', 'n', 'e']

        with self.assertRaises(Exception) as context:
            password.set_columns(columns)

        actual = str(context.exception)
        expected = 'Too many columns (must be 5 or less)'

        self.assertEqual(actual, expected)
