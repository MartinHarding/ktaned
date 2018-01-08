class Password(object):
    """docstring for Password"""
    def __init__(self, bomb):
        super(Password, self).__init__()
        self.bomb = bomb

        self.valid_characters = list('abcdefghijklmnopqrstuvwxyz')

        self.columns = []

        self.passwords = ['about', 'after', 'again', 'below', 'could', 'every',
                          'first', 'found', 'great', 'house', 'large', 'learn',
                          'never', 'other', 'place', 'plant', 'point', 'right',
                          'small', 'sound', 'spell', 'still', 'study', 'their',
                          'there', 'these', 'thing', 'think', 'three', 'water',
                          'where', 'which', 'world', 'would', 'write']

    def set_columns(self, columns):
        """Set the columns of characters to match passwords against
        """
        if len(columns) > 5:
            raise Exception('Too many columns (must be 5 or less)')
        for column_index, column in enumerate(columns):
            for character_index, character in enumerate(column):
                if character not in self.valid_characters:
                    raise Exception('Character {}:{} ({}) must be one of {}'
                                    .format(column_index, character_index,
                                            character, self.valid_characters))
        self.columns = columns

    def get_possibilities(self):
        """Get a list of potential password combinations

        Returns:
            list: strings representing the possible password(s)
        """
        possibilities = []

        for password in self.passwords:

            possibility = True
            for position, column in enumerate(self.columns):

                # Ensures that a passwords' nth character also matches at least
                # one character in the appropriate entry column
                if password[position] not in column:
                    possibility = False

            # Only append this to the possibilities list if it's a possibility
            if possibility:
                possibilities.append(password)

        return possibilities
