import random


class Bomb(object):
    """Represents the Bomb context that modules should compute against"""

    def __init__(self):
        super(Bomb, self).__init__()

        self.valid_battery_types = ['AA', 'D']
        self.valid_ports = ['DVI-D', 'Parallel', 'PS/2',
                            'RJ-45', 'Serial', 'Stereo RCA']
        self.valid_indicator_labels = ['SND', 'CLR', 'CAR',
                                       'IND', 'FRQ', 'SIG',
                                       'NSA', 'MSA', 'TRN',
                                       'BOB', 'FRK']

        self.explode_messages = ['You died!', 'Not my fault.', 'Idgit']

        self.reset()  # Sets up defaults for bomb

    def add_battery_pack(self, battery_type, quantity):
        """Add battery pack to bomb (required for certain modules)

        Args:
            battery_type (string): type of battery in the pack
            quantity (int): number batteries in the pack
        """

        if battery_type not in self.valid_battery_types:
            raise Exception('Battery type ({}) must be one of {}'
                            .format(battery_type, self.valid_battery_types))

        if quantity < 1:
            raise Exception('Battery packs must have at least one battery')

        self.battery_packs.append({'type': battery_type, 'quantity': quantity})

    def set_battery_packs(self, battery_packs):
        """Set battery packs on the bomb (replaces existing battery packs)

        Args:
            battery_packs (list): list of dicts representing battery packs
        """

        self.battery_packs = []
        for battery_pack in battery_packs:
            self.add_battery_pack(battery_pack['type'],
                                  battery_pack['quantity'])
        self.batteries = self.get_battery_count()

    def get_battery_count(self):
        """Set battery packs on the bomb (replaces existing battery packs)

        Returns:
            battery_count (int): sum total of batteries accross all types
        """

        return sum([d['quantity'] for d in self.battery_packs])

    def add_port(self, port):
        """Add port to bomb (required for certain modules)

        Args:
            port (string): name of port
        """

        if port not in self.valid_ports:
            raise Exception('Port ({}) must be one of {}'
                            .format(port, self.valid_ports))

        self.ports.append(port)

    def set_ports(self, ports):
        """Set ports on the bomb (replaces existing ports)

        Args:
            ports (list): list of ports
        """

        self.ports = []
        for port in ports:
            self.add_port(port)

    def add_indicator(self, label, lit):
        """Add indicator to bomb (required for certain modules)

        Args:
            label (string): label for the indicator
            lit (boolean): whether the indicator is lit (True) or not (False)
        """

        if label not in self.valid_indicator_labels:
            raise ValueError('Indicator "label" property must be one of {}'
                             .format(self.valid_indicator_labels))

        if lit not in [True, False]:
            raise ValueError('Indicator "lit" property must be boolean')

        self.indicators.append({'label': label, 'lit': lit})

    def set_indicators(self, indicators):
        """Set indicators on the bomb (replaces existing indicators)

        Args:
            indicators (list): list of dicts representing indicators
        """

        self.indicators = []
        for indicator in indicators:
            self.add_indicator(indicator['label'], indicator['lit'])

    def get_indicator_labels(self, lit=None):
        """Retrieve the label strings of the indicators on the bomb

        Args:
            indicators (list): list of indicator labels
            lit (mixed): optional bool that filters by lit or unlit indicators

        Returns:
            list: a list of strings representing indicator labels
        """

        indicator_labels = []
        for indicator in self.indicators:
            if lit is None or indicator['lit'] is lit:
                indicator_labels.append(indicator['label'])
        return indicator_labels

    def check_serial_for_vowel(self):
        """Check whether the serial set contains a vowel

        Returns:
            bool: True if contains a vowel
        """

        if not hasattr(self, 'serial') or self.serial is None:
            raise Exception('Must set serial before checking for vowel')

        if set(self.serial) & set('aeiou'):
            return True
        else:
            return False

    def check_serial_ends_odd(self):
        """Check whether the serial ends in an odd or even number

        Returns:
            bool: True if ends in odd
        """

        if not hasattr(self, 'serial') or self.serial is None:
            raise Exception('Must set serial before checking ends in odd')

        try:
            last_character_as_int = int(self.serial[-1])
        except Exception as e:
            return False
        return bool(last_character_as_int % 2)

    def add_strikes(self, strikes=1):
        """Add one or more strikes (mistake) to the bomb context

        Args:
            strikes (int): number of strikes to add (defaults to 1)
        """
        self.strikes += strikes
        if self.strikes > 2:
            self.explode()

    def set_strikes(self, strikes):
        """Add one or more strikes (mistake) to the bomb context
        Args:
            strikes (int): what number to set the strikes at
        """
        self.strikes = strikes
        if self.strikes > 2:
            self.explode()

    def reset(self):
        """Reset bomb properties to their default values (called in __init__,
        but may be useful for starting over"""
        self.ports = []
        self.indicators = []
        self.battery_packs = []
        self.strikes = 0
        self.serial = None

    def explode(self):
        """Kaboom"""
        r = random.randint(0, len(self.explode_messages)-1)
        message = self.explode_messages[r]
        raise Exception(message)
