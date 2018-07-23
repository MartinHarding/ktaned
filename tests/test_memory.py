import ktaned
import unittest


class MemoryTestCase(unittest.TestCase):
    def setUp(self):
        bomb = ktaned.Bomb()
        memory = ktaned.Memory(bomb)
        self.memory = memory

    def test_add_stage(self):
        display = 1
        buttons = [1, 2, 3, 4]

        self.memory.add_stage(display, buttons)

        actual = self.memory.stages
        expected = {
            0: {
                'display': display,
                'buttons': buttons,
                'solution': {
                    'label': 2,
                    'position': 1
                }
            }
        }
        self.assertEqual(actual, expected)

    def test_set_stage(self):
        display1 = 1
        buttons1 = [1, 2, 3, 4]
        display2 = 1
        buttons2 = [1, 2, 3, 4]

        self.memory.set_stage(0, display1, buttons1)
        self.memory.set_stage(1, display2, buttons2)

        actual = self.memory.stages
        expected = {
            0: {
                'display': display1,
                'buttons': buttons1,
                'solution': {
                    'label': 2,
                    'position': 1
                }
            },
            1: {
                'display': display2,
                'buttons': buttons2,
                'solution': {
                    'label': 4,
                    'position': 3
                }
            }
        }
        self.assertEqual(actual, expected)

    def test_set_stage_invalid_stage(self):
        display = 1
        buttons = [1, 2, 3, 4]

        stage = 'foo'
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(stage, display, buttons)
        actual = str(context.exception)
        expected = 'stage must be of type int'
        self.assertEqual(actual, expected)

        stage = 10
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(stage, display, buttons)
        actual = str(context.exception)
        expected = 'stage must be between 0 and 4'
        self.assertEqual(actual, expected)

    def test_set_stage_invalid_display(self):
        buttons = [1, 2, 3, 4]

        display = '1'
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'display must be of type int'
        self.assertEqual(actual, expected)

        display = 5
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'display must be between 1 and 4'

    def test_set_stage_invalid_buttons(self):
        display = 1

        buttons = '1, 2, 3, 4'
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'buttons must be of type list'
        self.assertEqual(actual, expected)

        buttons = [1, 2, 3]
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'buttons list must contain exactly 4 items'

        buttons = [1, 2, 3, 1]
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'buttons list must contain one each of 1, 2, 3, 4'

        buttons = [1, 2, 3, '4']
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'buttons items must be of type int'

        buttons = [1, 2, 3, 5]
        with self.assertRaises(Exception) as context:
            self.memory.set_stage(0, display, buttons)
        actual = str(context.exception)
        expected = 'buttons items must be between 1 and 4'

    def test_get_push(self):
        display = 1
        buttons = [1, 2, 3, 4]

        self.memory.add_stage(display, buttons)

        actual = self.memory.get_push(0)
        expected = {'label': 2, 'position': 1}
        self.assertEqual(actual, expected)

    def test_get_push_invalid_stage(self):
        display = 1
        buttons = [1, 2, 3, 4]

        self.memory.add_stage(display, buttons)

        with self.assertRaises(Exception) as context:
            self.memory.get_push(1)
        actual = str(context.exception)
        expected = 'stage key 1 is not set'
        self.assertEqual(actual, expected)

    def test_solve(self):
        # Number of possible combinations is 8,153,726,976 for randomized
        # button label positions, and 1,024 for non-randomized label positions,
        # making testing every combination unfeasible, so test each branch for
        # each stage but with only one branch from the previous stage(s)

        buttons = [1, 2, 3, 4]

        stage = 0

        self.memory.set_stage(stage, 1, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 1, 'label': 2}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 2, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 1, 'label': 2}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 3, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 2, 'label': 3}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 4, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        stage = 1

        self.memory.set_stage(stage, 1, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 2, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 3, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 0, 'label': 1}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 4, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        stage = 2

        self.memory.set_stage(stage, 1, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 2, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 3, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 2, 'label': 3}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 4, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        stage = 3

        self.memory.set_stage(stage, 1, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 2, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 0, 'label': 1}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 3, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 4, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        stage = 4

        self.memory.set_stage(stage, 1, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 2, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 3, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)

        self.memory.set_stage(stage, 4, buttons)
        actual = self.memory.get_push(stage)
        expected = {'position': 3, 'label': 4}
        self.assertEqual(actual, expected)
