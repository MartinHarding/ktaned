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

    def test_get_push(self):
        display = 1
        buttons = [1, 2, 3, 4]

        self.memory.add_stage(display, buttons)

        actual = self.memory.get_push(0)
        expected = {'label': 2, 'position': 1}
        self.assertEqual(actual, expected)

    # def test_memory_11234(self):
    #     s1buttons = list('1234')

    #     self.memory.set_stage(number, display, buttons)

    #     actual = self.memory.get_push()
    #     expected = {'label': 1, 'position': 1}
    #     self.

    # def test_memory_11234():
    #     s1buttons = list('1234')
    #     s2buttons = list('1234')
    #     s3buttons = list('1234')
    #     s4buttons = list('1234')

    #     self.memory.set_stage(number, display, buttons)

    #     actual = self.memory.get_push()
    #     expected = {'label': 1, 'position': 1}

    # def test_memory_stage_3():
    #     buttons = list('1234')

    #     self.memory.set_stage(number, display, buttons)

    #     actual = self.memory.get_push()
    #     expected = {'label': 1, 'position': 1}

    # def test_memory_stage_4():
    #     buttons = list('1234')

    #     self.memory.set_stage(number, display, buttons)

    #     actuall = self.memory.get_push()
    #     expected = {'label': 1, 'position': 1}
