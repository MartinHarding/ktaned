class SimonSays(object):
    """Represents the the simon says module"""

    def __init__(self, bomb):
        super(SimonSays, self).__init__()
        self.bomb = bomb
        self.valid_colors = ['red', 'blue', 'green', 'yellow']

        self.light_sequence = []
        self.push_sequence = []

        if bomb.check_serial_for_vowel():
            self.mappings_offset = 0
        else:
            self.mappings_offset = 3  # non-vowel mappings start at 3

        self.mappings = [
            {
                'red': 'blue',
                'blue': 'yellow',
                'green': 'green',
                'yellow': 'red'
            },
            {
                'red': 'red',
                'blue': 'blue',
                'green': 'green',
                'yellow': 'green'
            },
            {
                'red': 'yellow',
                'blue': 'green',
                'green': 'blue',
                'yellow': 'red'
            },
            {
                'red': 'blue',
                'blue': 'red',
                'green': 'yellow',
                'yellow': 'green'
            },
            {
                'red': 'yellow',
                'blue': 'green',
                'green': 'blue',
                'yellow': 'red'
            },
            {
                'red': 'green',
                'blue': 'red',
                'green': 'yellow',
                'yellow': 'blue'
            }
        ]

    def add_light_color(self, light_color):
        """Add a light color to the light sequence

        Args:
            light_color (string): color that the light lit up
        """

        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(color, self.valid_colors))

        self.light_sequence.append(color)

    def set_light_sequence(self, colors):
        """Set the light sequence to a list of colors

        Args:
            colors (list): chronological list of colors that the lights lit up
        """
        for color in colors:
            self.add_color(color)

    def get_push_sequence(self):
        """Get the sequence

        Returns:
            list: order in which to push the colored buttons
        """

        if len(self.light_sequence) == 0:
            raise Exception('light_sequence must contain at least one color')

        color_mappings_index = int(self.bomb.strikes + self.mappings_offset)
        mapping = self.mappings[mappings_offset]
        push_sequence = []
        for light_color in self.light_sequence:
            push_color = mapping[light_color]
            push_sequence.append(push_color)

        return push_sequence

    def reset(self):
        """Reset the module"""
        self.sequence = []
