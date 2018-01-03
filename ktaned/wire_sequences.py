from collections import Counter


class WireSequences(object):
    """docstring for WireSequences"""
    def __init__(self, bomb):
        super(WireSequences, self).__init__()
        self.bomb = bomb
        self.valid_colors = ['red', 'blue', 'black']
        self.valid_letters = ['a', 'b', 'c']
        self.wires = []
        self.cuts = {
            'red': [
                ('c'),
                ('b'),
                ('a'),
                ('a', 'c'),
                ('b'),
                ('a', 'c'),
                ('a', 'b', 'c'),
                ('a', 'b'),
                ('b')
            ],
            'blue': [
                ('b'),
                ('a', 'c'),
                ('b'),
                ('a'),
                ('b'),
                ('b', 'c'),
                ('c'),
                ('a', 'c'),
                ('a')
            ],
            'black': [
                ('a', 'b', 'c'),
                ('a', 'c'),
                ('b'),
                ('a', 'c'),
                ('b'),
                ('b', 'c'),
                ('a', 'b'),
                ('c'),
                ('c')
            ]
        }

    def add_wire(self, color, letter):
        """Add a wire

        Args:
            color (string): color of wire
            letter (string): letter wire is connected to

        Returns:
            boolean: whether to cut the wire or not
        """

        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(color, self.valid_colors))

        if letter not in self.valid_letters:
            raise Exception('Letter ({}) must be one of {}'
                            .format(letter, self.valid_letters))

        # Count previous wires of this color
        color_count = Counter(wire[0] for wire in self.wires).get(color, 0)

        # Append wire to list
        self.wires.append((color, letter))

        # Check the index of the cuts corresponding color key and return result
        return letter in self.cuts[color][color_count]

    def reset(self):
        """Reset module"""
        self.wires = []
