class Button(object):
    """docstring for Button"""
    def __init__(self, bomb):
        super(Button, self).__init__()
        self.bomb = bomb
        self.valid_colors = ['red', 'blue', 'yellow', 'white']
        self.valid_light_colors = ['red', 'blue', 'yellow', 'white', 'green']
        self.valid_labels = ['abort', 'detonate', 'hold', 'press']

    def set_color(self, color):
        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(color, self.valid_colors))
        self.color = color

    def set_label(self, label):
        label = label.lower()
        if label not in self.valid_labels:
            raise Exception('Label ({}) must be one of {}'
                            .format(label, self.valid_labels))
        self.label = label

    def get_action(self):

        if not hasattr(self, 'color') and not hasattr(self, 'label'):
            raise Exception('Must set color and label before getting action')
        elif not hasattr(self, 'color'):
            raise Exception('Must set color before getting action')
        elif not hasattr(self, 'label'):
            raise Exception('Must set label before getting action')

        lit_indicators = self.bomb.get_indicator_labels(lit=True)

        # print(self.color, self.label)

        if self.color == 'blue' and self.label == 'abort':
            return 'hold'
        elif self.bomb.batteries > 1 and self.label == 'detonate':
            return 'tap'
        elif self.color == 'white' and 'CAR' in lit_indicators:
            return 'hold'
        elif self.bomb.batteries > 2 and 'FRK' in lit_indicators:
            return 'tap'
        elif self.color == 'yellow':
            return 'hold'
        elif self.color == 'red' and self.label == 'hold':
            return 'tap'
        else:
            return 'hold'

    def set_light(self, light_color):
        if light_color not in self.valid_light_colors:
            raise Exception('Light color ({}) must be one of {}'
                            .format(light_color, self.valid_light_colors))
        self.light = light_color

    def get_release():
        if not hasattr(self, 'light_color'):
            raise Exception('Must set light_color before getting release')

        if self.light_color is 'blue':
            return 4
        if self.light_color is 'yellow':
            return 5
        if self.light_color in ['red', 'white', 'green']:
            return 1
