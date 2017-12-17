class Memory(object):
    """docstring for Memory"""
    def __init__(self, bomb):
        super(Memory, self).__init__()
        self.bomb = bomb
        self.valid_numbers = ['1','2','3','4']

    def add_number(self, number):
        if number not in self.valid_number:
            raise Exception('Number ({}) must be one of {}'
                .format(number, self.valid_number))
        self.number.append(number)

    def create_memory_set(self):
        memory_set = list(input("numbers? e.g. '11234'"))
        for i in range(len(memory_set)):
            # checks if the numbers and number set is valid
            if memory_set[i] not in self.valid_numbers or len(memory_set) is not 5:
                raise Exception('Number ({}) must be one of {}'
                                .format(number, self.valid_number))
        return memory_set

    def solve_stage_one(self):
        # Stage one only cares about positions
        stage_one_memory_set = create_memory_set()
        if stage_one_memory_set[0] == '1' or stage_one_memory_set[1] == '2':
            label = stage_one_memory_set[2]
        elif stage_one_memory_set[0] == '3':
            label = stage_one_memory_set[3]
        elif stage_one_memory_set[0] == '4':
            label = stage_one_memory_set[4]
        else:
            raise Exception('no solution found stage 1')
        # Finds position of activated number
        # Converts 0 index to 1 index
        position = 1 + memory_set[1::].index(label[0])
        # Return these somewhere?
        stage_one_activated = (label, position)
        return stage_one_activated

    def solve_stage_two(self):
        stage_two_memory_set = create_memory_set()
        if stage_two_memory_set[0] == '1':
            # button labeled '4'
            position = stage_two_memory_set.index('4')
            label = stage_two_memory_set[position]
        elif stage_two_memory_set[0] == '2' or stage_two_memory_set[0] == '4':
            # same position as stage 1
            position = stage_one_activated[1]
            label = stage_two_memory_set[position]
        elif stage_two_memory_set[0] == '3':
            # button in first position
            position = stage_two_memory_set[1]
            label = stage_two_memory_set[position]
        else:
            raise Exception('no solution found for stage 2')
        stage_two_activated = (label, position)
        return stage_two_activated

    def solve_stage_three(self):
        stage_three_memory_set = create_memory_set()
        if stage_three_memory_set[0] == '1':
            # Label from stage 2
            label = stage_two_activated[0]
            position = stage_three_memory_set.index(label)
        elif stage_three_memory_set[0] == '2':
            # Label from stage 1
            label = stage_one_activated[0]
            position = stage_three_memory_set.index(label)
        elif stage_three_memory_set[0] == '3':
            # 3rd position
            label = stage_three_memory_set[3]
            # Finds position of activated number
            # Converts 0 index to 1 index
            position = 1 + memory_set[1::].index(label[0])
        elif stage_three_memory_set[0] == '4':
            # label '4'
            position = stage_three_memory_set.index('4')
            label = stage_three_memory_set[position]
        else:
            raise Exception('no solution found for stage 3')
        stage_three_activated = (label, position)
        return stage_three_activated

    def solve_stage_four(self):
        stage_four_memory_set = create_memory_set()
        if stage_two_memory_set[0] == '1':
            # same position as stage 1
            position = stage_one_activated[1]
            label = stage_four_memory_set[position]
        elif stage_four_memory_set[0] == '2':
        # 3rd position
            label = stage_three_memory_set[3]
            # Finds position of activated number
            # Converts 0 index to 1 index
            position = 1 + memory_set[1::].index(label[0])
        elif stage_four_memory_set[0] == '3' or stage_four_memory_set[0] == 4:
            # same position as stage 2
            position = stage_two_activated[1]
            label = stage_four_memory_set[position]
        else:
            raise Exception('no solution found for stage 4'
        # Worth noting that stage 4 positions aren't used
        stage_four_activated = (label, position)
        return stage_four_activated

    def solve_stage_five(self):
        stage_five_memory_set = create_memory_set()
        # Because this is the last stage, there's no need to store these values
        if stage_five_memory_set[0] == '1':
            # label from stage 1
            label = stage_one_activated[0]
        elif stage_five_memory_set[0] == '2':
            # label from stage 2
            label = stage_two_activated[0]
        elif stage_five_memory_set[0] == '3':
            # label from stage *4*
            label = stage_four_activated[0]
        elif stage_five_memory_set[0] == '4':
            # label from stage *3*
            label = stage_three_activated[0]
        else:
            raise Exception('no solution found for stage 5')
        return label
      
