class Memory(object):
    """docstring for Memory"""
    def __init__(self, bomb):
        super(Memory, self).__init__()
        self.bomb = bomb
        self.mappings = []

        self.stages = {}

    def add_stage(self, display, buttons):
        """Add a stage to the stage list (allows easily adding stages without
        keeping track of the next stage number manually)

        Args:
            display (int): number on the big display
            buttons (list): ordered list of integers representing the buttons
        """

        stage = len(self.stages)
        self.set_stage(stage, display, buttons)

    def set_stage(self, stage, display, buttons):
        """Set the data for a specific stage

        Args:
            stage (int): index of the stage to set
            display (int): number on the big display
            buttons (list): ordered list of integers representing the buttons
        """

        # Stages are keyed starting at 0 as if it were a list
        if not isinstance(stage, int):
            raise Exception('stage must be of type int')
        if not 0 <= stage <= 4:
            raise Exception('stage must be between 0 and 4')

        if not isinstance(display, int):
            raise Exception('display must be of type int')
        if not 1 <= display <= 4:
            raise Exception('display must be between 1 and 4')

        if not isinstance(buttons, list):
            raise Exception('buttons must be of type list')
        if len(buttons) != 4:
            raise Exception('buttons list must contain exactly 4 items')
        if sorted(buttons) != [1, 2, 3, 4]:
            raise Exception('buttons list must contain one each of 1, 2, 3, 4')
        for button in buttons:
            if not isinstance(button, int):
                raise Exception('buttons items must be of type int')
            if not 1 <= button <= 4:
                raise Exception('buttons items must be between 1 and 4')

        # Validated, so set the stage
        self.stages[stage] = {
            'display': display,
            'buttons': buttons
        }
        self.solve()

    def solve(self):
        """Solves all stages set and adds the solutions to self.stages
        """
        for index, stage in self.stages.items():

            if index == 0:
                if stage['display'] in [1, 2]:
                    # press the button in the second position
                    position = 1
                    label = stage['buttons'][position]
                elif stage['display'] == 3:
                    # press the button in the third position
                    position = 2
                    label = stage['buttons'][position]
                elif stage['display'] == 4:
                    # press the button in the fourth position
                    position = 3
                    label = stage['buttons'][position]

            elif index == 1:
                if stage['display'] == 1:
                    # press the button labeled "4"
                    label = 4
                    position = stage['buttons'].index(label)
                elif stage['display'] in [2, 4]:
                    # press the button in the same position pressed in stage 1
                    position = self.stages[0]['solution']['position']
                    label = stage['buttons'][position]
                elif stage['display'] == 3:
                    # press the button in the first position
                    position = 1
                    label = stage['buttons'][0]

            elif index == 2:
                if stage['display'] == 1:
                    # press the button with the same label pressed in stage 2
                    label = self.stages[1]['solution']['label']
                    position = stage['buttons'].index(label)
                elif stage['display'] == 2:
                    # press the button with the same label pressed in stage 1
                    label = self.stages[0]['solution']['label']
                    position = stage['buttons'].index(label)
                elif stage['display'] == 3:
                    # press the button in the third position
                    position = 2
                    label = stage['buttons'][position]
                elif stage['display'] == 4:
                    # press the button labeled "4"
                    label = 4
                    position = stage['buttons'].index(label)

            elif index == 3:
                if stage['display'] == 1:
                    # press the button in the same position pressed in stage 1
                    position = self.stages[0]['solution']['position']
                    label = stage['buttons'][position]
                elif stage['display'] == 2:
                    # press the button in the first position
                    position = 0
                    label = stage['buttons'][position]
                elif stage['display'] in [3, 4]:
                    # press the button in the same position pressed in stage 2
                    position = self.stages[1]['solution']['position']
                    label = stage['buttons'][position]

            elif index == 4:
                if stage['display'] == 1:
                    # press the button with the same label pressed in stage 1
                    position = self.stages[0]['solution']['label']
                    label = stage['buttons'][position]
                elif stage['display'] == 2:
                    # press the button with the same label pressed in stage 2
                    position = self.stages[1]['solution']['label']
                    label = stage['buttons'][position]
                elif stage['display'] == 3:
                    # press the button with the same label pressed in stage 4
                    position = self.stages[3]['solution']['label']
                    label = stage['buttons'][position]
                elif stage['display'] == 4:
                    # press the button with the same label pressed in stage 3
                    position = self.stages[2]['solution']['label']
                    label = stage['buttons'][position]

            solution = {'position': position, 'label': label}
            self.stages[index]['solution'] = solution

    def get_push(self, stage_number):
        """Gets the solution to a stage

        Args:
            stage_number (int): key for the stage to solve

        Returns:
            dict: label and position of the button to push
        """

        return self.stages[stage_number]['solution']
