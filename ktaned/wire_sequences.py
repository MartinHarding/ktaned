class WireSequences(object):
    """docstring for WireSequences"""
    def __init__(self, bomb):
        super(WireSequences, self).__init__()
        self.bomb = bomb
        self.wires = []
        self.valid_colors = ['red', 'blue', 'black']
        # Not sure if this is proper implementation of counters
        self.wire_sequences = {'red': 0, 'blue': 0, 'black': 0}

    def add_wire(self, color):
        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                .format(color, self.valid_colors))
        self.wires.append(color)

    def reset_counter():
        wire_sequences = {'red': 0, 'blue': 0, 'black': 0}

    def solve_red(letter):
        # increments wire sequence counter
        wire_sequences['red'] += 1
        if wire_sequences['red'] == 1:
            if letter == 'c':
                return 'cut'
        elif wire_sequences['red'] == 2:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['red'] == 3:
            if letter == 'a':
                return 'cut'
        elif wire_sequences['red'] == 4:
            if letter == 'a' or letter == 'c':
                return 'cut'
        elif wire_sequences['red'] == 5:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['red'] == 6:
            if letter == 'a' or letter == 'c':
                return 'cut'
        elif wire_sequences['red'] == 7:
            if letter == 'a' or letter == 'b' or letter == 'c':
                return 'cut'
        elif wire_sequences['red'] == 8:
            if letter == 'a' or letter == 'b':
                return 'cut'
        elif wire_sequences['red'] == 9:
            if letter == 'b':
                return 'cut'
        else:
            return 'don\'t cut'

    def solve_blue(letter):
        # increments wire sequence counter
        wire_sequences['blue'] += 1

        if wire_sequences['blue'] == 1:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['blue'] == 2:
            if letter == 'a' or letter == 'c':
                return 'cut'
        elif wire_sequences['blue'] == 3:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['blue'] == 4:
            if letter == 'a':
                return 'cut'
        elif wire_sequences['blue'] == 5:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['blue'] == 6:
            if letter == 'b' or letter == 'c':
                return 'cut'
        elif wire_sequences['blue'] == 7:
            if letter == 'c':
                return 'cut'
        elif wire_sequences['blue'] == 8:
            if letter == 'a' or letter == 'c':
                return 'cut'
        elif wire_sequences['blue'] == 9:
            if letter == 'a':
                return 'cut'
        else:
            return 'don\'t cut'

    def solve_black(letter):
        # increments wire sequence counter
        wire_sequences['black'] += 1

        if wire_sequences['black'] == 1:
            if letter == 'a' or letter == 'b' or letter == 'c':
                return 'cut'
        elif wire_sequences['black'] == 2:
            if letter == 'a' or letter == 'c':
                return 'cut'
        elif wire_sequences['black'] == 3:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['black'] == 4:
            if letter == 'a' or letter == 'c':
                return 'cut'
        elif wire_sequences['black'] == 5:
            if letter == 'b':
                return 'cut'
        elif wire_sequences['black'] == 6:
            if letter == 'b' or letter == 'c':
                return 'cut'
        elif wire_sequences['black'] == 7:
            if letter == 'a' or letter == 'b':
                return 'cut'
        elif wire_sequences['black'] == 8:
            if letter == 'c':
                return 'cut'
        elif wire_sequences['black'] == 9:
            if letter == 'c':
                return 'cut'
        else:
            return 'don\'t cut'


# example use:
# wire_input = list(input("color letter \n").split(' '))
# red c # (becomes ['red', 'c'])
# solve_red(wire_input[1])
# cut
# red b # (becomes ['red', 'c'])
# solve_red(wire_input[1])
# don't cut
