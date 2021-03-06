# instruction input
directions = ['R5', 'L2', 'L1', 'R1', 'R3', 'R3', 'L3', 'R3', 'R4', 'L2', 'R4', 'L4', 'R4', 'R3', 'L2', 'L1', 'L1', 'R2', 'R4', 'R4', 'L4', 'R3', 'L2', 'R1', 'L4', 'R1', 'R3', 'L5', 'L4', 'L5', 'R3', 'L3', 'L1', 'L1', 'R4', 'R2', 'R2', 'L1', 'L4', 'R191', 'R5', 'L2', 'R46', 'R3', 'L1', 'R74', 'L2', 'R2', 'R187', 'R3', 'R4', 'R1', 'L4', 'L4', 'L2', 'R4', 'L5', 'R4', 'R3', 'L2', 'L1', 'R3', 'R3', 'R3', 'R1', 'R1', 'L4', 'R4', 'R1', 'R5', 'R2', 'R1', 'R3', 'L4', 'L2', 'L2', 'R1', 'L3', 'R1', 'R3', 'L5', 'L3', 'R5', 'R3', 'R4', 'L1', 'R3', 'R2', 'R1', 'R2', 'L4', 'L1', 'L1', 'R3', 'L3', 'R4', 'L2', 'L4', 'L5', 'L5', 'L4', 'R2', 'R5', 'L4', 'R4', 'L2', 'R3', 'L4', 'L3', 'L5', 'R5', 'L4', 'L2', 'R3', 'R5', 'R5', 'L1', 'L4', 'R3', 'L1', 'R2', 'L5', 'L1', 'R4', 'L1', 'R5', 'R1', 'L4', 'L4', 'L4', 'R4', 'R3', 'L5', 'R1', 'L3', 'R4', 'R3', 'L2', 'L1', 'R1', 'R2', 'R2', 'R2', 'L1', 'L1', 'L2', 'L5', 'L3', 'L1']
current_direction = 1
distance_traveled_in_direction = {
    1: 0,  # north
    2: 0,  # east
    3: 0,  # south
    4: 0  # west
}
useful_distance_traveled = 0


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

for instruction in directions:
        instruction_turn = instruction[:1]  # grab turn direction from first character
        instruction_distance = instruction[1:]  # grab the distance needed to travel from the remaining characters

        change_direction(instruction_turn)  # change direction to whatever direction
        distance_traveled_in_direction[current_direction] += int(instruction_distance)  # add to the total distance for that direction


# computing distance
useful_distance_traveled = abs(distance_traveled_in_direction[1]-distance_traveled_in_direction[3]) + abs(distance_traveled_in_direction[2]-distance_traveled_in_direction[4])

# solution
print useful_distance_traveled
