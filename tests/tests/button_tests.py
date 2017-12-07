import ktaned
import unittest


class ButtonTestCase(unittest.TestCase):

    def setUp(self):
        # Generic bomb configured specifically to allow proper testing of all
        # button cases
        self.bomb = ktaned.Bomb()
        indicators = [{'label': 'FRK', 'lit': True},
                      {'label': 'CAR', 'lit': True}]
        self.bomb.set_indicators(indicators)
        battery_packs = [{'type': 'AA', 'quantity': 2},
                         {'type': 'D', 'quantity': 1}]
        self.bomb.set_battery_packs(battery_packs)
        self.bomb.set_ports(['DVI-D'])

    def test_set_color(self):
        button = ktaned.Button(self.bomb)
        for color in button.valid_colors:
            button.set_color(color)
            actual = button.color
            expected = color
            self.assertEqual(actual, expected)

    def test_set_color_invalid(self):
        button = ktaned.Button(self.bomb)
        with self.assertRaises(Exception) as context:
            button.set_color('chartreuse')
        actual = str(context.exception)
        expected = 'Color (chartreuse) must be one of {}'.format(
            button.valid_colors)
        self.assertEqual(actual, expected)

    def test_set_label(self):
        button = ktaned.Button(self.bomb)
        for label in button.valid_labels:
            button.set_label(label)
            actual = button.label
            expected = label
            self.assertEqual(actual, expected)

    def test_set_label_invalid(self):
        button = ktaned.Button(self.bomb)
        with self.assertRaises(Exception) as context:
            button.set_label('hello')
        actual = str(context.exception)
        expected = 'Label (hello) must be one of {}'.format(
            button.valid_labels)
        self.assertEqual(actual, expected)

    def test_set_light(self):
        button = ktaned.Button(self.bomb)
        for light_color in button.valid_light_colors:
            button.set_light(light_color)
            actual = button.light
            expected = light_color
            self.assertEqual(actual, expected)

    def test_set_light_invalid(self):
        button = ktaned.Button(self.bomb)
        with self.assertRaises(Exception) as context:
            button.set_light('chartreuse')
        actual = str(context.exception)
        expected = 'Light color (chartreuse) must be one of {}'.format(
            button.valid_light_colors)
        self.assertEqual(actual, expected)

    def test_get_action_hold_blue_abort_label(self):
        button = ktaned.Button(self.bomb)
        button.set_color('blue')
        button.set_label('Abort')
        actual = button.get_action()
        expected = 'hold'
        self.assertEqual(actual, expected)

    def test_get_action_hold_white_car_indicator(self):
        self.bomb.set_indicators([{'label': 'CAR', 'lit': True}])
        button = ktaned.Button(self.bomb)
        button.set_color('white')
        button.set_label('Abort')
        actual = button.get_action()
        expected = 'hold'
        self.assertEqual(actual, expected)

    def test_get_action_hold_yellow(self):
        button = ktaned.Button(self.bomb)
        button.set_label('Abort')
        button.set_color('yellow')
        actual = button.get_action()
        expected = 'hold'
        self.assertEqual(actual, expected)

    def test_get_action_hold_elses(self):
        # Tests for if not explicit conditions
        # HOLD: blue, Abort label
        # HOLD: white, lit CAR indicator
        # HOLD: yellow
        #  TAP: > 1 batteries, Detonate
        #  TAP: > 2 batteries, lit FRK indicator
        #  TAP: red, Hold label

        button = ktaned.Button(self.bomb)
        button.set_color('blue')
        button.set_label('Hold')
        actual = button.get_action()
        expected = 'hold'
        self.assertEqual(actual, expected)

    def test_get_action_tap_2batteries_detonate_label(self):
        self.bomb.set_battery_packs([{'type': 'AA', 'quantity': 2}])
        button = ktaned.Button(self.bomb)
        button.set_color('blue')
        button.set_label('Detonate')
        actual = button.get_action()
        expected = 'tap'
        self.assertEqual(actual, expected)

    def test_get_action_tap_3batteries_frk_indicator(self):
        button = ktaned.Button(self.bomb)
        button.set_color('white')
        button.set_label('Hold')
        actual = button.get_action()
        expected = 'tap'
        self.assertEqual(actual, expected)

    def test_get_action_tap_red_hold_label(self):
        button = ktaned.Button(self.bomb)
        button.set_color('red')
        button.set_label('Hold')
        actual = button.get_action()
        expected = 'tap'
        self.assertEqual(actual, expected)
