directions = 'R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1'
# directions = 'R8, R4, R4, R8'
current_direction = 1  # 1: North, 2: East, 3: South, 4: West
grid_locations_current_coordinates = {
    'x': 0,
    'y': 0
}
grid_locations_coordinates_visited = [{'x': 0, 'y': 0}]
bunny_hq_coordinates = {
    'x': 0,
    'y': 0
}
found_hq = False

# function declaration

def change_direction(turn):
    global current_direction

    # turn the right direction
    if turn == 'R':
        current_direction += 1
    elif turn == 'L':
        current_direction -= 1

    # loop back around if necessary
    if current_direction == 5:
        current_direction = 1
    elif current_direction == 0:
        current_direction = 4

    return


def check_if_already_visited(coordinates_to_check):
    global grid_locations_coordinates_visited
    for coordinates in grid_locations_coordinates_visited:
        if coordinates['x'] == coordinates_to_check['x'] and coordinates['y'] == coordinates_to_check['y']:
            return True

    return False


# computes the movement of santa and marks nodes as visited or not
def compute_movement(distance_to_move):
    global current_direction
    global grid_locations_current_coordinates
    global grid_locations_coordinates_visited
    global bunny_hq_coordinates
    global found_hq

    while distance_to_move != 0:
        if current_direction == 1:  # north
            grid_locations_current_coordinates['y'] += 1
        elif current_direction == 2:  # east
            grid_locations_current_coordinates['x'] += 1
        elif current_direction == 3:  # south
            grid_locations_current_coordinates['y'] -= 1
        elif current_direction == 4:  # west
            grid_locations_current_coordinates['x'] -= 1

        if check_if_already_visited(grid_locations_current_coordinates.copy()):
            bunny_hq_coordinates = grid_locations_current_coordinates.copy()
            found_hq = True
            return

        grid_locations_coordinates_visited.append(grid_locations_current_coordinates.copy())

        # decrement distance left to move
        distance_to_move -= 1

    return


# actual main functionality
for instruction in directions.split(', '):
        change_direction(instruction[:1])  # change direction to whatever direction
        compute_movement(int(instruction[1:]))
        if found_hq:
            break

# solution
# print grid_locations_coordinates_visited
print bunny_hq_coordinates
print abs(bunny_hq_coordinates['x'])+abs(bunny_hq_coordinates['y'])
