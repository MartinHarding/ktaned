import ktaned
import inflect

p = inflect.engine()

bomb = ktaned.Bomb()


def solve_wires():
    if not hasattr(bomb, 'serial'):
        serial = input("Serial #: ")
        bomb.serial = serial
    wires = ktaned.SimpleWires(bomb)
    wire_colors = input('Enter wire colors: ')
    wire_colors = wire_colors.split(' ')
    try:
        wires.set_wires(wire_colors)
    except Exception as e:
        print(e)
        return

    solution = wires.solve()
    print('Cut the {} wire'.format(p.ordinal(int(solution))))


def solve_button():
    if not hasattr(bomb, 'serial'):
        serial = input("Serial #: ")
        bomb.serial = serial
    if len(bomb.battery_packs) == 0:
        batteries = int(input("Batteries: "))
        if batteries > 0:
            bomb.set_battery_packs([{'type': 'AA', 'quantity': batteries}])
    if len(bomb.indicators) == 0:
        frk_ind = input("FRK indicator? [y/n]: ")
        if frk_ind == 'y':
            bomb.add_indicator('FRK', lit=True)

        car_ind = input("CAR indicator? [y/n]: ")
        if car_ind == 'y':
            bomb.add_indicator('CAR', lit=True)

    button = ktaned.Button(bomb)

    color = input('Button color: ')
    button.set_color(color)

    # if bomb.get_battery_count() > 0 or color == 'white':
    label = input('Button label: ')
    label = label.lower()
    button.set_label(label)

    action = button.get_action()
    if action == 'tap':
        print('Tap the button')
    else:
        print('Hold the button')
        light_strip_color = input('Light strip color: ')
        button.set_light_color(light_strip_color)
        release = button.get_release()
        print(release)


def solve_maze():
    maze = ktaned.Maze(bomb)
    coords = input("Greens column1,row1 column2,row2: ")
    coords = coords.split(' ')
    green1 = coords[0].split(',')
    green2 = coords[1].split(',')
    gc1 = int(int(green1[0])-1)*2
    gr1 = int(int(green1[1])-1)*2
    gc2 = int(int(green2[0])-1)*2
    gr2 = int(int(green2[1])-1)*2
    greens = [(gc1, gr1), (gc2, gr2)]
    maze.set_greens(greens)
    try:
        maze.find_maze()
    except Exception as e:
        print(e)
        return

    start_coords = input("Start column,row: ")
    start = start_coords.split(',')
    startc = int(int(start[0])-1)*2
    startr = int(int(start[1])-1)*2
    maze.set_start((startc, startr))

    goal_coords = input("Goal column,row: ")
    goal = goal_coords.split(',')
    goalc = int(int(goal[0])-1)*2
    goalr = int(int(goal[1])-1)*2
    maze.set_goal((goalc, goalr))

    path = maze.find_path()
    print(path)
    instructions = maze.get_instructions(path)
    print(instructions)

    # goal = input("Goal column,row")
    # goal = set(goal)
    # maze.set_goal()

while True:
    mod = input("Enter module [w,b,m]: ")
    if mod == 'w':
        solve_wires()
    if mod == 'b':
        solve_button()
    if mod == 'm':
        solve_maze()
