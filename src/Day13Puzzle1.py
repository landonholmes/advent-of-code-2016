office_designer_fav_num = 1352
office_grid_size = 50
cubicle = {'value': 0, 'visited': False}
office_grid = [[cubicle.copy() for columns in range(office_grid_size)] for rows in range(office_grid_size)]
# office_grid[height y][width x]


def display_office_grid():
    display = "["

    office_grid_x = 0
    while office_grid_x < len(office_grid):
        office_grid_y = 0
        while office_grid_y < len(office_grid[office_grid_x]):
            display += str(office_grid[office_grid_x][office_grid_y]['value'])+"\t"
            office_grid_y += 1

        display += ']\n['
        office_grid_x += 1

    print display[:len(display)-1]


def put_up_walls():
    office_grid_x = 0
    while office_grid_x < len(office_grid):
        office_grid_y = 0
        while office_grid_y < len(office_grid[office_grid_x]):
            number_for_wall_calc = (office_grid_x*office_grid_x + 3*office_grid_x + 2*office_grid_x*office_grid_y + office_grid_y + office_grid_y*office_grid_y)
            # number_for_wall_calc = (office_grid_y*office_grid_y + 3*office_grid_y + 2*office_grid_y*office_grid_x + office_grid_x + office_grid_x*office_grid_x)
            number_for_wall_calc = bin(number_for_wall_calc+office_designer_fav_num)
            if number_for_wall_calc.count('1') % 2 == 0:  # if even number of 1s
                office_grid[office_grid_y][office_grid_x]['value'] = '#'
            office_grid_y += 1
        office_grid_x += 1
    office_grid[1][1]['value'] = -1  # the start point can't be a wall


def check_if_valid_point(point):  # point = (x,y)
    valid_point = False
    if 0 <= point[0] < office_grid_size and 0 <= point[1] < office_grid_size:  # if point within grid
            if office_grid[point[1]][point[0]]['value'] != '#':  # and point not a wall
                valid_point = True
    return valid_point


def visit_neighbors(points, distance):
    # visit the current point
    point_x = points[0]
    point_y = points[1]
    if not check_if_valid_point((point_x, point_y)):
        return

    current_point_distance = int(office_grid[point_y][point_x]['value'])
    if distance < current_point_distance or current_point_distance == 0:
        office_grid[point_y][point_x]['value'] = distance

    if office_grid[point_y][point_x]['visited']:
        return

    office_grid[point_y][point_x]['visited'] = True

    display_office_grid()
    # 4 neighbors to visit, up/down/left/right
    up_neighbor = (point_x, point_y-1)
    down_neighbor = (point_x, point_y+1)
    left_neighbor = (point_x-1, point_y)
    right_neighbor = (point_x+1, point_y)

    next_distance = (distance+1)
    visit_neighbors(up_neighbor, next_distance)
    visit_neighbors(down_neighbor, next_distance)
    visit_neighbors(left_neighbor, next_distance)
    visit_neighbors(right_neighbor, next_distance)

    return

put_up_walls()
# display_office_grid()
visit_neighbors((1, 1), 0)
display_office_grid()
print 'Distance to 31,39: ', office_grid[31][39]['value']
