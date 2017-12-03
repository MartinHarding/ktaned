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
        self.ports = []
        self.indicators = []
        self.batteries = []

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

        self.batteries.append({'type': battery_type, 'quantity': quantity})

    def set_battery_packs(self, battery_packs):
        """Set battery packs on the bomb (replaces existing battery packs)

        Args:
            battery_packs (list): list of dicts representing battery packs
        """

        self.batteries = []
        for battery_pack in battery_packs:
            self.add_battery_pack(battery_pack['type'],
                                  battery_pack['quantity'])

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
