class SimpleWires(object):
    """docstring for SimpleWires"""
    def __init__(self, bomb):
        super(SimpleWires, self).__init__()
        self.bomb = bomb
        self.wires = []
        self.valid_colors = ['red', 'blue', 'yellow', 'white', 'black']

    def add_wire(self, color):
        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                .format(color, self.valid_colors))
        self.wires.append(color)

    def set_wires(self, wires):
        self.wires = []
        for wire in wires:
            self.add_wire(wire)

    def last_color(self, color):
        for index, wire in reversed(list(enumerate(self.wires))):
            if wire is color:
                return index+1

    def solve(self):
        wire_count = len(self.wires)

        if wire_count is 3:
            if 'red' not in self.wires:
                return 2 # cut second
            elif self.wires[-1] is 'white':
                return wire_count # cut last
            elif 'blue' in self.wires:
                return self.last_color('blue') # cut last blue
            else:
                return wire_count # cut last

        elif wire_count is 4:
            if 'red' in self.wires and int(self.bomb.serial[-1]) % 2:
                return self.last_color('red') # cut last red
            elif ('red' not in self.wires and
                  self.wires[-1] is 'yellow' or
                  self.wires.count('blue') is 1):
                return 1 # cut first
            elif 'yellow' in self.wires:
                return wire_count # cut last
            else:
                return 2 # cut second

        elif wire_count is 5:
            if self.wires[-1] is 'black' and int(self.bomb.serial[-1]) % 2:
                return 4 # cut fourth
            elif (self.wires.count('red') is 1 and
                  self.wires.count('yellow') is 1):
                return 1 # cut first
            elif 'black' not in self.wires:
                return 2 # cut second
            else:
                return 1 # cut first

        elif wire_count is 6:
            if 'yellow' not in self.wires and int(self.bomb.serial[-1]) % 2:
                return 3 # cut third
            elif (self.wires.count('yellow') is 1 and
                  self.wires.count('white') is 1):
                return 4 # cut fourth
            elif 'red' not in self.wires:
                return wire_count # cut last
            else:
                return 4 # cut fourth

        else:
            raise Exception(
                'Wire count should be between 3 and 6, but {} wires were set'
                .format(wire_count))
