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
            # 0 strikes, vowel
            {
                'red': 'blue',
                'blue': 'yellow',
                'green': 'green',
                'yellow': 'red'
            },
            # 1 strikes, vowel
            {
                'red': 'red',
                'blue': 'blue',
                'green': 'green',
                'yellow': 'green'
            },
            # 2 strikes, vowel
            {
                'red': 'yellow',
                'blue': 'green',
                'green': 'blue',
                'yellow': 'red'
            },
            # 0 strikes, no vowel
            {
                'red': 'blue',
                'blue': 'red',
                'green': 'yellow',
                'yellow': 'green'
            },
            # 1 strikes, no vowel
            {
                'red': 'yellow',
                'blue': 'green',
                'green': 'blue',
                'yellow': 'red'
            },
            # 2 strikes, no vowel
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

        if light_color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(light_color, self.valid_colors))

        self.light_sequence.append(light_color)

    def set_light_sequence(self, colors):
        """Set the light sequence to a list of colors

        Args:
            colors (list): chronological list of colors that the lights lit up
        """
        self.light_sequence = []
        for color in colors:
            self.add_light_color(color)
            self.push_sequence = self.get_push_sequence()

    def get_push_sequence(self):
        """Get the sequence

        Returns:
            list: order in which to push the colored buttons
        """

        if len(self.light_sequence) == 0:
            raise Exception('light_sequence must contain at least one color')

        color_mappings_index = int(self.bomb.strikes + self.mappings_offset)
        mapping = self.mappings[self.mappings_offset]
        push_sequence = []
        for light_color in self.light_sequence:
            push_color = mapping[light_color]
            push_sequence.append(push_color)

        return push_sequence

    def reset(self):
        """Reset the module"""
        self.light_sequence = []
