instructions = """rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 6
rotate row y=0 by 2
rect 1x2
rotate column x=32 by 1
rotate column x=23 by 1
rotate column x=13 by 1
rotate row y=0 by 6
rotate column x=0 by 1
rect 5x1
rotate row y=0 by 2
rotate column x=30 by 1
rotate row y=1 by 20
rotate row y=0 by 18
rotate column x=13 by 1
rotate column x=10 by 1
rotate column x=7 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 17x1
rotate column x=16 by 3
rotate row y=3 by 7
rotate row y=0 by 5
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate column x=28 by 1
rotate row y=1 by 24
rotate row y=0 by 21
rotate column x=19 by 1
rotate column x=17 by 1
rotate column x=16 by 1
rotate column x=14 by 1
rotate column x=12 by 2
rotate column x=11 by 1
rotate column x=9 by 1
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=4 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 20x1
rotate column x=47 by 1
rotate column x=40 by 2
rotate column x=35 by 2
rotate column x=30 by 2
rotate column x=10 by 3
rotate column x=5 by 3
rotate row y=4 by 20
rotate row y=3 by 10
rotate row y=2 by 20
rotate row y=1 by 16
rotate row y=0 by 9
rotate column x=7 by 2
rotate column x=5 by 2
rotate column x=3 by 2
rotate column x=0 by 2
rect 9x2
rotate column x=22 by 2
rotate row y=3 by 40
rotate row y=1 by 20
rotate row y=0 by 20
rotate column x=18 by 1
rotate column x=17 by 2
rotate column x=16 by 1
rotate column x=15 by 2
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 1
rotate column x=10 by 1
rotate column x=8 by 3
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 19x1
rotate column x=44 by 2
rotate column x=40 by 3
rotate column x=29 by 1
rotate column x=27 by 2
rotate column x=25 by 5
rotate column x=24 by 2
rotate column x=22 by 2
rotate column x=20 by 5
rotate column x=14 by 3
rotate column x=12 by 2
rotate column x=10 by 4
rotate column x=9 by 3
rotate column x=7 by 3
rotate column x=3 by 5
rotate column x=2 by 2
rotate row y=5 by 10
rotate row y=4 by 8
rotate row y=3 by 8
rotate row y=2 by 48
rotate row y=1 by 47
rotate row y=0 by 40
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 4
rotate column x=43 by 2
rotate column x=42 by 3
rotate column x=41 by 2
rotate column x=38 by 5
rotate column x=37 by 5
rotate column x=36 by 5
rotate column x=33 by 1
rotate column x=28 by 1
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=25 by 1
rotate column x=23 by 5
rotate column x=22 by 1
rotate column x=21 by 2
rotate column x=18 by 1
rotate column x=17 by 3
rotate column x=12 by 2
rotate column x=11 by 2
rotate column x=7 by 5
rotate column x=6 by 5
rotate column x=5 by 4
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 3
rotate column x=0 by 4"""

screen = [[0 for columns in range(50)] for rows in range(6)]
# screen[row][col]


def display_screen():
    display = "["
    for row in screen:
        for col in row:
            display += str(col)+" "
        display += ']\n['

    print display[:len(display)-1]


def rect(col, row):
    # need to reduce by 1 since arrays indexed from 0
    col -= 1
    row -= 1

    # loop over rows and columns and fill in 1's
    while col >= 0:
        temp_row = row
        while temp_row >= 0:
            screen[temp_row][col] = 1
            temp_row -= 1
        col -= 1


def rotate_col(which_col, magnitude):
    while magnitude > 0:
        current_col = len(screen)-1  # start at bottom of height
        original_ending = screen[len(screen)-1][which_col]
        while current_col > 0:
            screen[current_col][which_col] = screen[current_col-1][which_col]
            current_col -= 1
        screen[0][which_col] = original_ending
        magnitude -= 1


def rotate_row(which_row, magnitude):
    while magnitude > 0:
        current_col = len(screen[0])-1  # start at right of width
        original_ending = screen[which_row][len(screen[0])-1]
        while current_col > 0:
            screen[which_row][current_col] = screen[which_row][current_col-1]
            current_col -= 1
        screen[which_row][0] = original_ending
        magnitude -= 1

for line in instructions.split("\n"):
    if "rect" in line:
        (cols, rows) = line.split("rect ")[1].split("x")
        rect(int((cols, rows)[0]), int((cols, rows)[1]))
    else:
        if "rotate column" in line:
            (column, amount) = line.split("rotate column x=")[1].split(" by ")
            rotate_col(int((column, amount)[0]), int((column, amount)[1]))

        else:
            (row, amount) = line.split("rotate row y=")[1].split(" by ")
            rotate_row(int((row, amount)[0]), int((row, amount)[1]))


display_screen()
print sum(row.count(1) for row in screen)

# This is puzzle 1 and 2 because puzzle 2 is just reading the display.
# This way, my display_screen for debugging was used to see the letters
