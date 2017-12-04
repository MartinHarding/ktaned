class button(object):
    """docstring for button"""

    def __init__(self, bomb):
        super(button, self).__init__()
        self.bomb = bomb
        self.valid_colors = ['red', 'blue', 'yellow', 'white']
        self.valid_labels = ['abort', 'detonate', 'hold', 'press']

    def create_button(self, color, label):
        color = input('button color?')
        if color not in self.valid_colors:
            raise Exception('Color ({}) must be one of {}'
                            .format(color, self.valid_colors))
        label = input('button label?')
        if label not in self.valid_labels:
            raise Exception('Label ({}) must be one of {}'
                            .format(label, self.valid_labels))
        self.current_button.append(color)
        self.current_button.append(label)

    # TODO, refactor hold()
    # It should be called after hold_or_tap() to inform holding
    def hold_button():
        print("HOLD THE BUTTON")
        print("release when the countdown timer has the correct number")
        print("Blue strip: 4\nYellow strip: 5\nRed, white, or green: 1\n")

    def tap_button():
        print("TAP THE BUTTON!\n")

    # TODO, refactor hold_or_tap()
    # This determines if the Button should be held or tapped
    # This is not using correct bomb variables
    def hold_or_tap(self, bomb_settings):
        if button_color is 'blue' and button_label is 'abort':
            hold_button()
        elif bomb['batteries'] == True and button_label is 'detonate':
            tap_button()
        elif button_color is 'white' and 'CAR' in bomb['labels']:
            hold_button()
        elif bomb['batteries'] == True and 'FRK' in bomb['labels']:
            tap_button()
        elif button_color is 'yellow':
            hold_button()
        elif button_color is 'red' and button_label is 'hold':
            tap_button()
        else:
            hold_button()
