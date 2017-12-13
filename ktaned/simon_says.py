class Simon_says(object):
    """Represents the the simon says module"""

    def __init__(self, bomb):
        super(Simon_says, self).__init__()
        self.bomb = bomb
        self.valid_colors = ['red', 'blue', 'green', 'yellow']
        # TODO, get strikes from bomb case?
        self.valid_strikes = [0, 1 , 2]
        # TODO, change vowel to get it from bomb case
        # use bomb.check_serial_for_vowel() ?
        self.vowel = False

    def set_color(self, color):
        """Checks if the input is a valid color"""
        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(color, self.valid_colors))
        self.color = color
    
    def set_strike(self, strike):
        """Checks if the strikes is a valid number"""
        if strike not in self.valid_strikes:
            raise Exception('Strike ({}) must be one of {}'
                            .format(strike, self.valid_strikes))
        self.strike = strike

    def solve(self, vowel, strikes):
        """Returns the translated colors for simon says"""
        if not hasattr(self, 'color') and not hasattr(self, 'label'):
            raise Exception('Must set color and label before getting action')
        elif not hasattr(self, 'strikes'):
            raise Exception('Must set strike before getting action')
        elif not hasattr(self, 'vowel'):
            raise Exception('Must set vowel boolean before getting action')

        lit_indicators = self.bomb.get_indicator_labels(lit=True)

        simon_list = list(input("color?, e.g. 'red blue'\n").split(' '))
        simon_translated = list()

        if len(simon_list) > 5 or len(simon_list) < 1:
            raise Exception('Invalid length for simon says:\n 1 < items < 5')

        # vowel and strikes determine the correct color translation
        if vowel == False:
            if strikes == 0:
                for i in range(len(simon_list)):
                    print(simon_list[i])
                    if simon_list[i] == 'red':
                        simon_translated.append('blue')
                    elif simon_list[i] == 'blue':
                        simon_translated.append('yellow')
                    elif simon_list[i] == 'green':
                        simon_translated.append('green')
                    elif simon_list[i] == 'yellow':
                        simon_translated.append('red')
            elif strikes == 1:
                for i in range(len(simon_list)):
                    print(simon_list[i])
                    if simon_list[i] == 'red':
                        simon_translated.append('red')
                    elif simon_list[i] == 'blue':
                        simon_translated.append('blue')
                    elif simon_list[i] == 'green':
                        simon_translated.append('green')
                    elif simon_list[i] == 'yellow':
                        simon_translated.append('green')
            elif strikes == 2:
                for i in range(len(simon_list)):
                    print(simon_list[i])
                    if simon_list[i] == 'red':
                        simon_translated.append('yellow')
                    elif simon_list[i] == 'blue':
                        simon_translated.append('green')
                    elif simon_list[i] == 'green':
                        simon_translated.append('blue')
                    elif simon_list[i] == 'yellow':
                        simon_translated.append('red')

        elif vowel == True:
            if strikes == 0:
                for i in range(len(simon_list)):
                    print(simon_list[i])
                    if simon_list[i] == 'red':
                        simon_translated.append('blue')
                    elif simon_list[i] == 'blue':
                        simon_translated.append('red')
                    elif simon_list[i] == 'green':
                        simon_translated.append('yellow')
                    elif simon_list[i] == 'yellow':
                        simon_translated.append('green')
            elif strikes == 1:
                for i in range(len(simon_list)):
                    print(simon_list[i])
                    if simon_list[i] == 'red':
                        simon_translated.append('yellow')
                    elif simon_list[i] == 'blue':
                        simon_translated.append('green')
                    elif simon_list[i] == 'green':
                        simon_translated.append('blue')
                    elif simon_list[i] == 'yellow':
                        simon_translated.append('red')
            elif strikes == 2:
                for i in range(len(simon_list)):
                    print(simon_list[i])
                    if simon_list[i] == 'red':
                        simon_translated.append('green')
                    elif simon_list[i] == 'blue':
                        simon_translated.append('red')
                    elif simon_list[i] == 'green':
                        simon_translated.append('yellow')
                    elif simon_list[i] == 'yellow':
                        simon_translated.append('blue')
        else:
            return 'Simon says solution failed'

        return simon_translated
        
        # TODO, Unit test
        # vowel, strikes == False, 2
        # list = ['red', 'blue', 'green', 'yellow']
        # EXPECTED OUTPUT
        # ['yellow', 'green', 'blue', 'red']
            
