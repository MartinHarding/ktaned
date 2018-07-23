import ktaned
import unittest

class SimpleWiresTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_wires(self):

        bomb = ktaned.Bomb()

        bomb.serial = 'abc123'
        bomb.batteries = True
        bomb.labels = ['FRK']

        module = ktaned.SimpleWires(bomb)
        wires = ['red', 'red', 'blue']
        module.set_wires(wires)

        # Solution should be third wire
        actual = module.solve()
        expected = 3
        self.assertEqual(actual, expected)
