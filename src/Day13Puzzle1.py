office_designer_fav_num = 1352
office_grid_size = 50
cubicle = {'distance': ' ', 'visited': False}
office_grid = [[cubicle.copy() for columns in range(office_grid_size)] for rows in range(office_grid_size)]
# office_grid[height y][width x]


def get_visited(point):
    return office_grid[point[1]][point[0]]['visited']


def set_visited(point, new_distance):
    office_grid[point[1]][point[0]]['visited'] = new_distance


def get_distance(point):
    return office_grid[point[1]][point[0]]['distance']


def set_distance(point, new_distance):
    office_grid[point[1]][point[0]]['distance'] = new_distance


def display_office_grid():
    display = "["

    office_grid_y = 0
    while office_grid_y < len(office_grid):
        office_grid_x = 0
        while office_grid_x < len(office_grid[office_grid_y]):
            display += str(office_grid[office_grid_y][office_grid_x]['distance'])+"\t"
            office_grid_x += 1

        display += ']\n['
        office_grid_y += 1

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
                office_grid[office_grid_y][office_grid_x]['distance'] = '#'
            office_grid_y += 1
        office_grid_x += 1
    office_grid[1][1]['distance'] = 0  # the start point can't be a wall


def check_if_valid_point(point):  # point = (x,y)
    if_valid_point = False
    if 0 <= point[0] < office_grid_size and 0 <= point[1] < office_grid_size:  # if point within grid
            if get_distance(point) != '#':  # and point not a wall
                if_valid_point = True
    return if_valid_point


def visit_neighbors(current_point, distance):
    # get the x and y of current point, need for finding neighbors
    point_x = current_point[0]
    point_y = current_point[1]

    # if we aren't currently on a valid point, get outta here
    if not check_if_valid_point(current_point):
        return

    # check and set current distance
    if distance < get_distance(current_point):
        set_distance(current_point, distance)

    # 4 neighbors to visit, up/down/left/right
    up_neighbor = (point_x, point_y-1)
    down_neighbor = (point_x, point_y+1)
    left_neighbor = (point_x-1, point_y)
    right_neighbor = (point_x+1, point_y)

    if check_if_valid_point(up_neighbor):
        try:
            if distance < int(get_distance(up_neighbor)):
                set_distance(up_neighbor, distance)
        except:
            set_distance(up_neighbor, distance)

    if check_if_valid_point(down_neighbor):
        try:
            if distance < int(get_distance(down_neighbor)):
                set_distance(down_neighbor, distance)
        except:
            set_distance(down_neighbor, distance)

    if check_if_valid_point(left_neighbor):
        try:
            if distance < int(get_distance(left_neighbor)):
                set_distance(left_neighbor, distance)
        except:
            set_distance(left_neighbor, distance)

    if check_if_valid_point(right_neighbor):
        try:
            if distance < int(get_distance(right_neighbor)):
                set_distance(right_neighbor, distance)
        except:
            set_distance(right_neighbor, distance)

    set_visited(current_point, True)

    if not get_visited(up_neighbor):
        visit_neighbors(up_neighbor, (distance+1))
    if not get_visited(down_neighbor):
        visit_neighbors(down_neighbor, (distance+1))
    if not get_visited(left_neighbor):
        visit_neighbors(left_neighbor, (distance+1))
    if not get_visited(right_neighbor):
        visit_neighbors(right_neighbor, (distance+1))

    return

put_up_walls()
# display_office_grid()
visit_neighbors((1, 1), 1)
display_office_grid()
print 'Distance to 31,39: ', office_grid[39][31]['distance']
