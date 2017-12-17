class Button(object):
    """Represents the button module"""
    def __init__(self, bomb):
        super(Button, self).__init__()
        self.bomb = bomb
        self.valid_colors = ['red', 'blue', 'yellow', 'white']
        self.valid_light_colors = ['red', 'blue', 'yellow', 'white', 'green']
        self.valid_labels = ['abort', 'detonate', 'hold', 'press']

    def set_color(self, color):
        """Set and validate the color of the button

        Args:
            color (string): color of the button
        """
        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(color, self.valid_colors))
        self.color = color

    def set_label(self, label):
        """Set and validate the label on the button

        Args:
            label (string): label on the button
        """
        label = label.lower()
        if label not in self.valid_labels:
            raise Exception('Label ({}) must be one of {}'
                            .format(label, self.valid_labels))
        self.label = label

    def set_light_color(self, light_color):
        """Set and validate the color of the light strip next to the button

        Args:
            light_color (string): color of the light strip
        """
        if light_color not in self.valid_light_colors:
            raise Exception('Light color ({}) must be one of {}'
                            .format(light_color,
                                    self.valid_light_colors))
        self.light_color = light_color

    def get_action(self):
        """Determine whether to release or tap the button"""
        if not hasattr(self, 'color') and not hasattr(self, 'label'):
            raise Exception('Must set color and label before getting action')
        elif not hasattr(self, 'color'):
            raise Exception('Must set color before getting action')
        elif not hasattr(self, 'label'):
            raise Exception('Must set label before getting action')

        lit_indicators = self.bomb.get_indicator_labels(lit=True)

        if self.color == 'blue' and self.label == 'abort':
            return 'hold'
        elif self.bomb.get_battery_count() > 1 and self.label == 'detonate':
            return 'tap'
        elif self.color == 'white' and 'CAR' in lit_indicators:
            return 'hold'
        elif self.bomb.get_battery_count() > 2 and 'FRK' in lit_indicators:
            return 'tap'
        elif self.color == 'yellow':
            return 'hold'
        elif self.color == 'red' and self.label == 'hold':
            return 'tap'
        else:
            return 'hold'

    def get_release(self):
        """Determine which number must be shown in timer during release"""

        if not hasattr(self, 'light_color'):
            raise Exception('Must set light_color before getting release')

        if self.light_color == 'blue':
            return 4
        elif self.light_color == 'yellow':
            return 5
        else:
            return 1
