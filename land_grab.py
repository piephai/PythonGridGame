
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10265813
#    Student name: Emilie Pomeroy
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  LAND GRAB
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "process_moves".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various rectangular icons, using data stored in a
#  list to determine which icons to place and where.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#


#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *

# Define constant values for setting up the drawing canvas
cell_width = 120  # pixels (default is 120)
cell_height = 90  # pixels (default is 90)
grid_size = 7  # width and height of the grid (default is 7)
x_margin = cell_width * 2.4  # pixels, the size of the margin left/right of the board
y_margin = cell_height // 2.1  # pixels, the size of the margin below/above the board
canvas_height = grid_size * cell_height + y_margin * 2
canvas_width = grid_size * cell_width + x_margin * 2

# Validity checks on grid size
assert cell_width >= 100, 'Cells must be at least 100 pixels wide'
assert cell_height >= 75, 'Cells must be at least 75 pixels high'
assert grid_size >= 5, 'Grid must be at least 5x5'
assert grid_size % 2 == 1, 'Grid size must be odd'
assert cell_width / cell_height >= 4 / 3, 'Cells must be much wider than high'

#
#--------------------------------------------------------------------#


#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You may NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(show_instructions=True,  # show Part B instructions
                          label_locations=True,  # label axes and home coord
                          bg_colour='light grey',  # background colour
                          line_colour='grey'):  # line colour for grid

    # Set up the drawing canvas with enough space for the grid
    setup(canvas_width, canvas_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coordinate of the grid
    left_edge = -(grid_size * cell_width) // 2
    bottom_edge = -(grid_size * cell_height) // 2

    # Draw the horizontal grid lines
    setheading(0)  # face east
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge, bottom_edge + line_no * cell_height)
        pendown()
        forward(grid_size * cell_width)

    # Draw the vertical grid lines
    setheading(90)  # face north of grid
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge + line_no * cell_width, bottom_edge)
        pendown()
        forward(grid_size * cell_height)

    # Optionally label the axes and centre point
    if label_locations:

        # Mark the centre of the board (coordinate [0, 0])
        penup()
        home()
        dot(30)
        pencolor(bg_colour)
        dot(20)
        pencolor(line_colour)
        dot(10)

        # Define the font and position for the axis labels
        small_font = ('Arial', (18 * cell_width) // 100, 'normal')
        y_offset = (32 * cell_height) // 100  # pixels

        # Draw each of the labels on the x axis
        penup()
        for x_label in range(0, grid_size):
            goto(left_edge + (x_label * cell_width) +
                 (cell_width // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align='center', font=small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10  # pixels
        for y_label in range(0, grid_size):
            goto(left_edge - x_offset, bottom_edge +
                 (y_label * cell_height) + (cell_height // 2) - y_offset)
            write(str(y_label + 1), align='right', font=small_font)

    # Optionally write the instructions
    if show_instructions:
        # Font for the instructions
        competitor_font = ('Arial', (10 * cell_width) // 100, 'normal')
        pencolor('black')
        # Competitor A label
        goto((-grid_size * cell_width) // 2 - 150, (cell_height * 3) - 10)
        write('Competitor A:\nRainy weather',
              align='left', font=competitor_font, )
        # Competitor B label
        goto((-grid_size * cell_width) // 2 - 150, (-cell_height * 3) - 10)
        write('Competitor C:\nSunny weather',
              align='left', font=competitor_font, )
        # Competitor C label
        goto((grid_size * cell_width) // 2 + 25, (cell_height * 3) - 10)
        write('Competitor B:\nSnowy weather',
              align='left', font=competitor_font, )
        # Competitor D label
        goto((grid_size * cell_width) // 2 + 25, (-cell_height * 3) - 10)
        write('Competitor D:\nCloudy weather',
              align='left', font=competitor_font, )
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    # Ensure any drawing still in progress is displayed
    update()
    tracer(True)
    # Optionally hide the cursor
    if hide_cursor:
        hideturtle()
    # Release the drawing canvas
    done()

#
#--------------------------------------------------------------------#


#-----Test Data for Use During Code Development----------------------#
#
# The data sets in this section are provided to help you develop and
# test your code.  You can use them as the argument to the
# "process_moves" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_moves" function appearing below.
# Your program must work correctly for any data set that can be
# generated by calling "random_moves()" with no argument.
#
# Each of the data sets is a list of moves, each specifying which
# competitor is attempting to move and in which direction.  The
# general form of each move is
#
#     [competitor_identity, direction]
#
# where the competitor identities range from 'Competitor A' to
# 'Competitor D' and the directions are 'Up', 'Down', 'Left' and
# 'Right'.
#
# Note that all the data sets below assume the second argument
# to "random_moves" has its default value.
#
# The following data set makes no moves at all and can be used
# when developing the code to draw the competitors in their
# starting positions.
fixed_data_set_00 = []

# The following data sets each move one of the competitors
# several times but do not attempt to go outside the margins
# of the grid or overwrite previous moves
fixed_data_set_01 = [['Competitor A', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor A', 'Up']]
fixed_data_set_02 = [['Competitor B', 'Left'],
                     ['Competitor B', 'Left'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Right'],
                     ['Competitor B', 'Up']]
fixed_data_set_03 = [['Competitor C', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Left']]
fixed_data_set_04 = [['Competitor D', 'Left'],
                     ['Competitor D', 'Left'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Right'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Right'],
                     ['Competitor D', 'Down']]

# The following data set moves all four competitors and
# will cause them all to go outside the grid unless such
# moves are prevented by your code
fixed_data_set_05 = [['Competitor C', 'Right'],
                     ['Competitor B', 'Up'],
                     ['Competitor D', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor C', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor D', 'Left'],
                     ['Competitor A', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor B', 'Right'],
                     ['Competitor D', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor C', 'Right'],
                     ['Competitor B', 'Down'],
                     ['Competitor D', 'Right'],
                     ['Competitor A', 'Right']]

# We can also control the random moves by providing a "seed"
# value N to the random number generator by using
# "random_moves(N)" as the argument to function "process_moves".
# You can copy the following function calls into the main
# program to force the program to produce a fixed sequence of
# moves while debugging your code.

# The following seeds all produce moves in which each
# competitor captures a small number of squares in their
# own corner, but do not interfere with one another.
#
#   random_moves(39) - Only one round occurs
#   random_moves(58) - Only two rounds
#   random_moves(12)
#   random_moves(27)
#   random_moves(38)
#   random_moves(41)

# The following seeds all produce moves in which two or
# more competitors overlap one another's territory.
#
#   random_moves(20) - Competitors C and D touch but don't overlap
#   random_moves(23) - Competitors A and B overlap
#   random_moves(15) - Competitors A and D overlap
#   random_moves(29) - Competitors B and D overlap slightly
#   random_moves(18) - Competitors B, C and D overlap
#   random_moves(31) - A and C overlap slightly, B and D touch but don't overlap
#   random_moves(36) - Competitor D overlaps Competitor C
#
# We haven't yet found a seed that causes a player to
# be completely eliminated - can you find one?

# The following seeds all produce very long sequences of
# moves which result in most of the grid being filled.
#
#   random_moves(19)
#   random_moves(75)
#   random_moves(43) - Competitor D reaches opposite corner
#   random_moves(87) - C occupies A's corner and A occupies B's corner
#   random_moves(90) - Only 4 squares left unoccupied
#
# We haven't yet found a seed that causes every cell
# to be occupied - can you find one?

# The following seeds produce data sets which have a special
# meaning in the second part of the assignment. Their
# significance will be explained in the Part B instructions.
#
#   random_moves(21)
#   random_moves(26)
#   random_moves(24)
#   random_moves(35)
#
#   random_moves(52)
#   random_moves(51)
#   random_moves(47)
#   random_moves(46)
#
#   random_moves(53)
#   random_moves(62)
#   random_moves(81)
#   random_moves(48)
#
#   random_moves(54)
#   random_moves(98)

# If you want to create your own test data sets put them here.

#
#--------------------------------------------------------------------#


#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.

# The following function creates a random data set as a list
# of moves.  Your program must work for any data set that
# can be returned by this function.  The results returned by
# calling "random_moves()" will be used as the argument to your
# "process_moves" function during marking.  For convenience during
# code development and marking this function also prints each move
# to the shell window.
#
# NB: As a matter of style your code should not print anything else
# to the shell.  Make sure any debugging calls to the "print"
# function are disabled before you submit your solution.
#
# The function makes no attempt to avoid moves that will go
# outside the grid.  It is your responsibility to detect and
# ignore such moves.
#
def random_moves(the_seed=None, max_rounds=35):
    # Welcoming message
    print('\nWelcome to Land Grab!')
    print('Here are the randomly-generated moves:')
    # Set up the random number generator
    seed(the_seed)
    # Randomise the order in which competitors move
    competitors = ['Competitor A', 'Competitor B',
                   'Competitor C', 'Competitor D', ]
    shuffle(competitors)
    # Decide how many rounds of moves to make
    num_rounds = randint(0, max_rounds)
    # For each round generate a random move for each competitor
    # and save and print it
    moves = []
    for round_no in range(num_rounds):
        print()
        for competitor in competitors:
            # Create a random move
            move = [competitor, choice(['Left', 'Right', 'Up', 'Down'])]
            # Print it to the shell and remember it
            print(move)
            moves.append(move)
    # Print a final message and return the list of moves
    print('\nThere were', len(competitors) * num_rounds,
          'moves generated in', num_rounds,
          ('round' if num_rounds == 1 else 'rounds'))
    return moves


#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "process_moves" function.
#
# Draw competitors on the grid as per the provided data set


# Initialise the random_moves list
random_moves = random_moves(62)


# ---------------------Helper functions----------------------------

# xSign and ySign cases. Should only be either 1 or -1
# Case 1: -1 for xSign and -1 for ySign mean that it's in the top right quadrants of the grid
# Case 2: -1 xSign and 1 ySign mean that it's in the bottom right quadrants of the grid
# Case 3: 1 xSign and -1 ySign mean that it's in the top left quadrants of the grid
# Case 4: 1 xSign and 1 ySign mean that it's in the bottom left quadrants of the grid


# This function allows the goto to take in positional arguments of cell_width(n)/2 where n is the xIndex, the number of cells in the horizonal plane and cell_height(n)/2 where n is the yIndex, the number of cells in the vertical plane
# Meanwhile the xSign and ySign allow for the determination of quandrant in which the cell is located in. As such goto(xIndex, yIndex, xSign, ySign) allows the turtle to goto the middle of a specific cell on the grid

def goto_cell(xIndex, yIndex, xSign, ySign):

    # If both xIndex and yIndex are even numbers
    if (xIndex % 2 == 0) and yIndex % 2 == 0:
        goto(((cell_width*xIndex)/2,
              ((cell_height*yIndex/2))))
    # If xIndex is an odd number and yIndex is an even number
    elif (xIndex % 2 != 0 and yIndex % 2 == 0):
        goto(((cell_width*xIndex)/2 + (cell_width/2) * (xSign),
              ((cell_height*yIndex/2))))
    # If xIndex is an even number and yIndex is an odd number
    elif (xIndex % 2 == 0 and yIndex % 2 != 0):
        goto(((cell_width*xIndex)/2,
              ((cell_height*yIndex/2) + (cell_height/2) * (ySign))))
    else:  # If both xIndex and yIndex are odd numbers
        goto(((cell_width*xIndex)/2 + (cell_width/2) * (xSign),
              ((cell_height*yIndex/2) + (cell_height/2) * (ySign))))


# Checking which cell the turtle is in then place the turtle in the middle of that cell
def check_cell_location(location):

    for xIndex in range(1, grid_size + 1):
        for yIndex in range(1, grid_size + 1):

            # Check if turtle is in the bottom left quandrant
            if (((location[-1][0]) >= -((cell_width*xIndex)/2))
                and (location[-1][0] <= -((cell_width*(xIndex-1)/2))
                     and (location[-1][1] >= -((cell_height*yIndex)/2))
                     and (location[-1][1] <= -((cell_height*(yIndex-1)/2))))):
                goto_cell(-xIndex, -yIndex, 1, 1)
                location[-1] = pos()

            # Check if turtle is in the check if turtle is in the top right quadrant
            elif (((location[-1][0]) <= ((cell_width*xIndex)/2))
                  and (location[-1][0] >= ((cell_width*(xIndex-1)/2))
                       and (location[-1][1] <= ((cell_height*yIndex)/2))
                       and (location[-1][1] >= ((cell_height*(yIndex-1)/2))))):
                goto_cell(xIndex, yIndex, -1, -1)
                location[-1] = pos()

            # Check if turtle is in the bottom right quadrant
            elif (((location[-1][0]) <= ((cell_width*xIndex)/2))
                  and (location[-1][0] >= ((cell_width*(xIndex-1)/2))
                       and (location[-1][1] >= -((cell_height*yIndex)/2))
                       and (location[-1][1] <= -((cell_height*(yIndex-1)/2))))):
                goto_cell(xIndex, -yIndex, -1, 1)
                location[-1] = pos()

            # Check if turtle is in the top left quadrant
            elif (((location[-1][0]) >= -((cell_width*xIndex)/2))
                  and (location[-1][0] <= -((cell_width*(xIndex-1)/2))
                       and (location[-1][1] <= ((cell_height*yIndex)/2))
                       and (location[-1][1] >= ((cell_height*(yIndex-1)/2))))):
                goto_cell(-xIndex, yIndex, 1, -1)
                location[-1] = pos()
    return location


# -------------------------Competitor A - Rainy weather competitor drawing components------------------------------


def rainy_colour_background():  # Drawing the background colour for the competitor.

    rainy_background_colour = 'cornflower blue'
    border_colour = 'black'
    border_width = 2

    # Sending turtle to corner of the grid.
    setheading(0)
    forward(cell_width/2)
    setheading(90)
    forward(cell_height/2)

    # Filling in the grid with the 'cornflower blue' colour
    width(border_width)
    pencolor(border_colour)
    fillcolor(rainy_background_colour)
    begin_fill()
    pendown()

    # For each loop to fill in grid colour.
    for background in range(2):
        left(90)
        forward(cell_width)
        left(90)
        forward(cell_height)
    end_fill()
    penup()


def rainy_city_background():  # Drawing buildings in the background

    building_size = 30
    building_colour = 'dark blue'
    pen_colour = 'black'

    # Going to location to start building drawings
    setheading(270)
    forward(cell_height/1.5)
    setheading(180)

    # Filling in buildings with the 'dark blue' colour
    pencolor(pen_colour)
    fillcolor(building_colour)
    begin_fill()
    pendown()

    # Farthest right building
    forward(building_size/2)
    right(90)
    forward(building_size)
    left(90)
    forward(building_size/2)
    left(90)
    forward(building_size/2)
    right(90)

    # Second building from the right
    forward(building_size/4)
    right(90)
    forward(building_size)
    left(90)
    forward(building_size/2)
    left(90)
    forward(building_size*1.5)
    right(90)

    # Third building from the right
    forward(building_size/2)
    right(90)
    forward(building_size)
    left(90)
    forward(building_size/2)
    left(90)
    forward(building_size)
    right(90)

    # Last building from the right
    forward(building_size/4)
    right(90)
    forward(building_size*1.5)
    left(90)
    forward(building_size)
    left(90)
    forward(building_size*2)
    right(90)

    # Going back to the start to fill in the drawings
    setheading(0)
    forward(cell_width)
    end_fill()
    penup()


def random_lights_on():  # Randomises windows to have lights on by being yellow coloured
    random_value = randint(1, 2)
    if (random_value == 1):
        window_colour = 'yellow'
    else:
        window_colour = 'grey'
    return window_colour


def set_window_color(colour):  # Sets the window colours
    pencolor(colour)
    fillcolor(colour)


def building_windows():

    building_size = 30
    window_size = 5
    set_window_color(random_lights_on())

    # Going to window location for the first building on the right
    setheading(180)
    forward(window_size)
    setheading(90)
    penup()
    forward(window_size)
    pendown()

    # Drawing window for the first building from the right
    begin_fill()
    for lines in range(4):
        forward(window_size)
        left(90)
    end_fill()
    penup()

    # Going to window location for the second building on the right
    setheading(180)
    forward(building_size/2)
    setheading(270)
    forward(window_size*1.5)
    setheading(90)

    # Drawing windows for the second building from the right
    for second_building_windows in range(5):
        forward(window_size*1.5)
        set_window_color(random_lights_on())
        pendown()
        begin_fill()
        for lines in range(4):
            forward(window_size/1.5)
            left(90)
        end_fill()
        penup()

    # Going to window location for the third building from the right
    setheading(270)
    forward(building_size)
    setheading(180)
    forward(building_size/1.35)

    # Drawing windows for the third building from the right
    for third_building_windows in range(10):
        setheading(90)
        set_window_color(random_lights_on())
        forward(window_size)
        setheading(180)
        pendown()
        forward(window_size)
        penup()
        setheading(0)
        forward(window_size)
    penup()

    # Going to window location for the fourth building from the right
    setheading(270)
    forward(window_size*11)
    setheading(180)
    forward(building_size)

    # Drawing windows for the fourth building from the right
    for fourth_building_windows in range(8):
        setheading(90)
        set_window_color(random_lights_on())
        forward(window_size)
        setheading(180)
        pendown()
        forward(window_size/4)
        penup()
        forward(window_size/2)
        pendown()
        forward(window_size/4)
        penup()
        setheading(0)
        forward(window_size)
    penup()

    # Going to right window location for the fifth building from the right
    setheading(270)
    forward(building_size*1.4)
    setheading(180)
    forward(window_size*5)

    # Drawing right column of windows for the fifth building from the right
    for fifth_building_windows in range(5):
        setheading(90)
        forward(window_size*2)
        pendown()
        set_window_color(random_lights_on())
        begin_fill()
        for lines in range(4):
            forward(window_size)
            left(90)
        end_fill()
        penup()

    # Going to left window location for the fifth building from the right.
    setheading(270)
    forward(building_size*1.65)
    setheading(180)
    forward(window_size*2)

    # Drawing left column of windows for the fifth building from the right
    for fifth_building_windows in range(5):
        setheading(90)
        forward(window_size*2)
        pendown()
        set_window_color(random_lights_on())
        begin_fill()
        for lines in range(4):
            forward(window_size)
            left(90)
        end_fill()
        penup()


def street_path():  # Drawing a street path

    path_width = 15
    path_length = (cell_width)
    window_size = 5
    path_color = 'dark slate grey'
    pen_colour = 'black'

    # Goes to the location for the street path to be drawn
    penup()
    setheading(0)
    forward(cell_width - (window_size*2.6))
    setheading(270)
    forward(cell_height/1.85)

    # Filling in the road with the 'dark slate grey' colour and 'black' border
    pencolor(pen_colour)
    fillcolor(path_color)
    begin_fill()
    pendown()

    # For each loop to draw the path and fill it in
    for path in range(2):
        forward(path_width)
        right(90)
        forward(path_length)
        right(90)
    end_fill()
    penup()


def lamp_post():  # Draws lamp posts

    lamp_post_size = 15
    lamp_post_head = 4
    lamp_head_colour = 'gold'
    lamp_post_colour = 'dark slate grey'
    post_spacing = 30
    pencolor(lamp_post_colour)

    # Goes to location for the first lamp post
    setheading(180)
    forward(post_spacing)

    # Creating a for each loop so that the lamp post will draw multiple
    # times, evenly spaced.

    for lamps in range(3):
        setheading(270)
        forward(lamp_post_size/3)
        setheading(90)
        pendown()
        forward(lamp_post_size)
        left(90)
        forward(lamp_post_head/2)

        # Creating a for each loop so that the lamp head will draw for
        # every lamp post.

        for head in range(2):
            fillcolor(lamp_head_colour)
            begin_fill()
            right(90)
            forward(lamp_post_head*2)
            right(90)
            forward(lamp_post_head)
            end_fill()
        penup()

        # Ensures lamp posts are on the same level and evenly spaced

        setheading(270)
        forward(lamp_post_size/1.5)
        setheading(180)
        forward(post_spacing)


def park_trees():  # Drawing trees for the street

    tree_spacing = 10
    tree_size = 10
    leave_size = 7
    tree_branch_size = 5
    tree_leaves_colour = 'forest green'
    tree_trunk_colour = 'brown'

    # Going to location for the first tree
    setheading(270)
    forward(tree_spacing/2)
    setheading(0)
    forward(tree_spacing*1.5)

    # Creating multiple trees in a row with a for each loop.
    for trees in range(3):

        # Spacing between trees
        setheading(0)
        forward(tree_spacing*3)

        # Drawing the tree trunk
        pendown()
        setheading(90)
        pencolor(tree_trunk_colour)
        forward(tree_size)

        # Drawing the left tree branch and tree leaves
        setheading(135)
        forward(tree_branch_size)
        dot(leave_size, tree_leaves_colour)
        penup()
        setheading(315)
        forward(tree_branch_size)
        setheading(90)

        # Drawing the middle tree branch and tree leaves
        pendown()
        forward(tree_size)
        dot(leave_size, tree_leaves_colour)
        setheading(270)
        penup()
        forward(tree_size)

        # Drawing the right tree branch and tree leaves
        setheading(45)
        forward(tree_branch_size)
        dot(leave_size, tree_leaves_colour)
        penup()

        # Going back to the base level for the next tree
        setheading(270)
        forward(tree_size+(leave_size/2))


def moon():  # Moon drawing for the sky

    moon_size = 5
    moon_colour = 'white'
    sky_color = 'cornflower blue'

    # Going to the location for the moon
    penup()
    setheading(90)
    forward(cell_height/1.4)

    # First circle with white colour to create moon.
    pendown()
    fillcolor(moon_colour)
    begin_fill()
    pencolor(moon_colour)
    circle(moon_size)
    end_fill()

    # Move forward to draw next circle.
    penup()
    setheading(0)
    forward(moon_size)
    setheading(90)

    # Second circle with background colour to create moon.
    pendown()
    fillcolor(sky_color)
    begin_fill()
    pencolor(sky_color)
    circle(moon_size)
    end_fill()
    penup()


def star_loop():  # Drawing function to call when placing stars in the sky

    star_size = 5
    pensize(1)

    # Loop to draw stars.
    for star in range(5):
        pendown()
        forward(star_size)
        right(144)
    penup()


def stars():  # Placing stars in the sky.

    star_size = 5
    star_colour = 'white'
    pencolor(star_colour)

    # First star from the right.
    star_loop()
    setheading(180)
    forward(star_size*4)
    star_loop()

    # Second star from the right.
    right(25)
    forward(star_size*3)
    star_loop()

    # Third star from the right.
    left(60)
    forward(star_size*4)
    star_loop()

    # Fourth star from the right.
    right(30)
    forward(star_size*5)
    star_loop()

    # Fifth star from the right.
    right(40)
    forward(star_size*4)
    star_loop()


def rain(location):  # Creating random rain
    min_rain_size = 5
    max_rain_size = 7
    rain_colour = 'pale turquoise'
    pencolor(rain_colour)

    # Get the pos of turtle which should be in the direct middle of its current cell
    check_cell_location(location)

    # Let current_cell_x to be equal to the x-pos since competitor_A_location is a vector (x, y)
    current_cell_x = location[-1][0]

    # Let current_cell_y to be equal to the y-pos
    current_cell_y = location[-1][1]

    for rain in range(randint(25, 75)):

        # Randomise the rain size between min size and max size
        rain_size = randint(min_rain_size, max_rain_size)
        # rain_pos_x will be in the range of left edge of the cell + max_rain_size and right edge of the cell - max_rain_size
        rain_pos_x = randint((current_cell_x - cell_width/2) + max_rain_size,
                             (current_cell_x + cell_width/2) - max_rain_size)
        # rain_pos_y will be in the range of bottom edge of the cell + max_rain_size and top edge of the cell - max_rain_size
        rain_pos_y = randint((current_cell_y - cell_height/2) + max_rain_size,
                             (current_cell_y + cell_height/2) - max_rain_size)
        goto(rain_pos_x, rain_pos_y)
        pendown()
        setheading(225)
        forward(rain_size)
        penup()


# ------------------Competitor B - Sunny weather drawing components--------------------------


def sunny_colour_background():  # Drawing the background colour for the competitor.

    sunny_background_colour = 'sky blue'
    border_colour = 'black'
    border_width = 2

    # Sending turtle to corner of the grid.
    setheading(270)
    forward(cell_height/2)
    setheading(180)
    forward(cell_width/2)
    setheading(90)

    # Filling in the grid with the 'sky blue' colour
    pencolor(border_colour)
    width(border_width)
    fillcolor(sunny_background_colour)
    begin_fill()
    pendown()

    # For each loop to fill in grid colour.
    for move in range(2):
        forward(cell_height)
        right(90)
        forward(cell_width)
        right(90)
    penup()
    end_fill()


def sand_shores():  # Drawing a sand shore

    sand_colour = 'Wheat'

    # Going to corner of the grid to draw the shore
    penup()
    setheading(90)
    forward(cell_width/4)
    setheading(0)
    forward(2)

    # Filling in the shore with the 'Wheat' colour
    color(sand_colour)
    fillcolor(sand_colour)
    begin_fill()
    pendown()

    # For each loop to draw the sand shore
    for sandline in range(2):
        forward(cell_width - 4)
        right(90)
        forward((cell_height/3)-2)
        right(90)
    end_fill()
    penup()


def sunny_ocean():  # Ocean for the beach

    ocean_colour = 'blue'
    ocean_size = 20

    # Going to corner of the grid to draw the ocean
    setheading(90)
    forward(ocean_size/2)
    setheading(0)
    forward(cell_width-4)
    setheading(180)

    # Filling in the ocean with the 'blue' colour
    pencolor(ocean_colour)
    fillcolor(ocean_colour)
    begin_fill()
    pendown()

    # For each loop to draw the ocean
    for ocean in range(2):
        forward(cell_width - 4)
        left(90)
        forward(cell_height/5)
        left(90)
    end_fill()
    penup()


def cloud_drawing(cloud_size, cloud_colour, pen_colour):  # Cloud drawing function
    # Function to draw a cloud with a size and colour paramenter required

    pen_width = 1

    # Colour in parameter goes into pen and fillcolor
    pencolor(pen_colour)
    fillcolor(cloud_colour)
    begin_fill()
    pendown()
    width(pen_width)

    # Draws the right edge of the cloud
    setheading(0)
    circle(cloud_size/2, extent=180)
    setheading(135)

    # For each loop to draw the top of the cloud
    for cloud in range(2):
        circle(cloud_size, extent=90)
        setheading(135)

    # Draws the left edge of the cloud
    circle(cloud_size, extent=90)
    setheading(180)
    circle(cloud_size/2, extent=180)

    # Draws the base of the cloud
    setheading(0)
    forward((cloud_size*4)+2)

    end_fill()
    penup()


def sunny_clouds():  # Drawing clouds for the sky

    # Big cloud on the right
    big_cloud_colour = 'white'
    big_cloud_size = 8
    cloud_outline = 'light gray'

    # Going to the location for the cloud
    penup()
    setheading(90)
    forward(big_cloud_size*4)
    setheading(180)
    forward(big_cloud_size)

    # Calling function to draw the cloud
    cloud_drawing(big_cloud_size, big_cloud_colour, cloud_outline)

    # Small cloud on the left
    small_cloud_colour = 'white'
    small_cloud_size = 6

    # Going to the location for the cloud
    setheading(210)
    forward(small_cloud_size*6)

    # Calling function to draw the cloud
    cloud_drawing(small_cloud_size, small_cloud_colour, cloud_outline)


def sun_rays(length, radius):  # Function to draw sun rays

    # For each loop to draw the sunrays
    for sunrays in range(4):
        penup()
        forward(radius)
        pendown()
        forward(length)
        penup()
        backward(length + radius)
        left(90)


def sun():  # Drawing a sun

    sun_size = 10
    sun_colour = 'yellow'

    # Going to location to draw the sun at
    setheading(160)
    forward(50)
    setheading(90)

    # Filling in circle with the 'yellow' colour
    pencolor(sun_colour)
    fillcolor(sun_colour)
    begin_fill()
    pendown()
    circle(sun_size)
    end_fill()

    # Using the sun rays function to draw sunrays
    setheading(180)
    forward(sun_size)
    sun_rays(sun_size/2, sun_size)
    setheading(45)
    sun_rays(sun_size/2, sun_size)
    penup()
    setheading(0)
    forward(sun_size)


def ocean_waves():  # Drawing waves for the ocean

    waves_width = 1
    wave_space = 10
    waves_colour = 'white'

    pencolor(waves_colour)
    width(waves_width)

    # Going to first wave location
    setheading(250)
    forward(wave_space * 4)

    # Drawing the first wave
    pendown()
    setheading(45)
    circle(-wave_space, extent=90)
    circle(wave_space, extent=90)
    penup()

    # For each loop to draw 2 waves
    for waves in range(2):
        setheading(330)
        forward(wave_space)
        pendown()
        circle(wave_space/2, extent=90)
        circle(-wave_space, extent=90)
        penup()


def palm_tree_trunk():  # Drawing trunk of a palm tree

    trunk_height = 80
    trunk_width = 5
    trunk_slope = 25
    trunk_colour = 'saddle brown'

    # Going to location for the palm tree
    setheading(270)
    forward(trunk_width*6)

    # Filling in the trunk with the 'saddle brown' colour
    fillcolor(trunk_colour)
    pencolor(trunk_colour)
    begin_fill()
    pendown()

    # Drawing the tree trunk
    setheading(90)
    circle(trunk_height, extent=trunk_slope)

    setheading(180)
    forward(trunk_width)

    setheading(295)
    circle(- trunk_height, extent=trunk_slope)

    setheading(0)
    forward(trunk_width)

    end_fill()
    penup()


def palm_tree_leaves():  # Palm leaves for the palm tree

    palm_size = 20
    palm_colour = 'green'
    palm_extent = 15

    # Going to start of the palm tree leaves
    setheading(90)
    circle(palm_size * 4, extent=25)

    # Filling in palm tree leaves with the 'green' colour
    pencolor(palm_colour)
    fillcolor(palm_colour)
    begin_fill()
    pendown()

    # Drawing the right palm leaf
    setheading(0)
    circle(palm_size*2, extent=palm_extent)

    setheading(160)
    circle(palm_size, extent=(palm_extent*2))

    # Drawing the middle palm leaf
    setheading(45)
    circle(palm_size*2, extent=palm_extent)

    setheading(200)
    circle(palm_size*1.5, extent=(palm_extent*2))

    # Drawing the left palm leaf
    setheading(130)
    circle(palm_size, extent=(palm_extent*2))

    setheading(300)
    circle(palm_size * 2, extent=palm_extent)

    # Going to the start of the palm leaves to fill it in
    setheading(0)
    forward(palm_size/2)
    end_fill()
    penup()

    # Drawing two coconuts for the palm trees
    coconut_size = 5
    coconut_colour = 'black'

    pencolor(coconut_colour)

    # For each loop to draw two coconuts.
    for coconuts in range(2):
        dot(coconut_size)
        setheading(180)
        forward(coconut_size * 1.5)


def sunny_umbrella():  # Umbrella for the sand shore

    # Choice generates random umbrella colour for each grid
    umbrella_size = 10
    colour_list = 'red', 'dark orange', 'hot pink', 'purple', 'violet red',
    umbrella_colour = choice(colour_list)
    umbrella_handle_colour = 'black'

    # Going to the location for the umbrella handle to be drawn
    setheading(270)
    forward(cell_width/4)
    setheading(180)
    forward(cell_width / 2)
    setheading(60)

    # Filling in umbrella handle with the 'black' colour
    fillcolor(umbrella_handle_colour)
    begin_fill()

    # For each loop to draw the umbrella handle
    for umbrella in range(2):
        forward(umbrella_size)
        left(90)
        forward(umbrella_size/10)
        left(90)
    end_fill()
    penup()

    # Going to location the umbrella head location
    setheading(60)
    forward(umbrella_size)
    right(90)
    forward(umbrella_size)
    setheading(60)

    # Filling in the umbrella head with 'red'
    fillcolor(umbrella_colour)
    pencolor(umbrella_colour)
    begin_fill()
    pendown()
    circle(umbrella_size, extent=180)
    end_fill()
    penup()


# ------------------Competitor C - Snowy weather drawing components--------------------------


def snow_colour_background():  # Drawing the background colour for the competitor

    snow_background_colour = 'steel blue'
    border_colour = 'black'
    border_width = 2

    # Sending turtle to corner of the grid
    setheading(0)
    forward(cell_width/2)
    setheading(90)
    forward(cell_height/2)

    width(border_width)
    pencolor(border_colour)
    fillcolor(snow_background_colour)
    begin_fill()
    pendown()

    # For each loop to fill in grid colour
    for move in range(2):
        left(90)
        forward(cell_width)
        left(90)
        forward(cell_height)
    end_fill()
    penup()


def mountains():

    mountain_colour = 'grey'
    mountain_size = 28
    border_size = 1

    # Going to the starting point of the mountain drawing
    setheading(270)
    forward(cell_height/2)
    setheading(180)
    forward(border_size)
    setheading(135)

    # Filling in the mountain with colour
    pencolor(mountain_colour)
    fillcolor(mountain_colour)
    begin_fill()
    pendown()

    # For each loop to draw two mountains
    for mountains in range(2):
        forward(mountain_size)
        setheading(225)
        forward(mountain_size * 2)
        setheading(135)

    # Going back to the start to fill in the colour.
    setheading(0)
    forward(cell_width - border_size)
    end_fill()
    penup()


def falling_snow(location):  # Draw random snowfall pattern for each snowy competitor

    min_snow_size = 1
    max_snow_size = 3
    pencolor('white')

    # Get the pos of turtle which should be in the direct middle of its current cell
    check_cell_location(location)

    # Let current_cell_x to be equal to the x-pos since comeptitor_c_location is a vector (x, y)
    current_cell_x = location[-1][0]

    # Let current_cell_y to be equal to the y-pos
    current_cell_y = location[-1][1]

    # Get the y-coordinate of the top of the road + 5
    road_from_middle_of_cell = (current_cell_y - cell_height/2) + 15
    for snow in range(randint(100, 200)):
        # Randomise the snow size between min size and max size
        snow_size = randint(min_snow_size, max_snow_size)

        # snow_pos_x will be in the range of left edge of the cell + 2 and right edge of the cell - 2
        snow_pos_x = randint((current_cell_x - cell_width/2) + 2,
                             (current_cell_x + cell_width/2) - 2)

        # snow_pos_y will be in the range of bottom edge of the cell + 2 and top edge of the cell - 2
        snow_pos_y = randint((current_cell_y - cell_height/2) + 2,
                             (current_cell_y + cell_height/2) - 2)

        # Check if the snow_pos_y is above the road y-coordinate if it is then draw the snow else if it is not then pass
        if (snow_pos_y > road_from_middle_of_cell):
            goto(snow_pos_x, snow_pos_y)
            dot(snow_size)
        else:
            pass


def snowy_road():

    road_width = 10
    dash_size = 4
    road_colour = 'black'
    dash_colour = 'white'

    # Going to corner to draw the road
    setheading(180)
    forward(cell_width - 1)
    setheading(270)
    forward(dash_size)

    # Filling in the road with colour black
    pencolor(road_colour)
    fillcolor(road_colour)
    begin_fill()
    pendown()
    setheading(90)

    # For each loop to draw the road
    for road in range(2):
        forward(road_width)
        right(90)
        forward(cell_width - 1)
        right(90)
    end_fill()

    # Creating a dashed line on the road
    penup()
    setheading(90)
    forward(dash_size)
    setheading(0)
    pencolor(dash_colour)
    forward(dash_size/3)

    # For each loop to draw dashed line on the road
    for dash in range(15):
        pendown()
        forward(dash_size)
        penup()
        forward(dash_size)
    penup()


def snow_trees():

    trunk_width = 2
    trunk_height = 6
    tree_height = 10
    tree_trunk_colour = 'saddle brown'
    tree_leaves_colour = 'forest green'

    # Filling in the colour of the tree trunk
    pencolor(tree_trunk_colour)
    fillcolor(tree_trunk_colour)
    begin_fill()
    pendown()
    setheading(90)

    # For each loop to create the tree trunk
    for tree in range(2):
        forward(trunk_height)
        left(90)
        forward(trunk_width)
        left(90)
    end_fill()
    penup()

    # Filling in the colour of the tree crown
    setheading(90)
    forward(trunk_width * 2)
    setheading(0)
    forward(trunk_height//2)
    fillcolor(tree_leaves_colour)
    pencolor(tree_leaves_colour)
    begin_fill()
    pendown()

    # Creating the tree crown
    setheading(115)
    forward(tree_height)
    setheading(250)
    forward(tree_height)
    setheading(0)
    forward(tree_height * 0.75)
    end_fill()
    penup()


def tree_location():
    tree_spacing = 20

    # Going to the starting position of the trees location
    setheading(0)
    forward(cell_width/2)
    setheading(270)
    forward(cell_height/5)

    # Using a for each loop to call the snow trees function to draw multiple trees.
    snow_trees()
    for trees in range(2):
        setheading(200)
        forward(tree_spacing)
        snow_trees()
        setheading(170)
        forward(tree_spacing)
        snow_trees()
    penup()

    # Adding a tree to corner of the smaller mountain
    setheading(225)
    forward(tree_spacing)
    snow_trees()
    penup()

    # Adding two trees to top of the taller mountain
    setheading(15)
    forward(tree_spacing*3)
    snow_trees()
    forward(tree_spacing/2)
    snow_trees()


def mountain_snow():

    peak_size = 20
    snow_cover_size = 2.8
    mountain_size = 28
    small_snow_cover_size = 3.2
    snow_colour = 'white'

    # Going to the peak of the right mountain to draw the snow peak
    width(0)
    setheading(90)
    forward(cell_height/2.2)
    setheading(135)
    forward(peak_size/2)

    # Following the shape of the right mountain peak to fill it in
    fillcolor(snow_colour)
    begin_fill()
    pendown()
    forward(peak_size)
    setheading(225)
    forward(peak_size)
    setheading(270)

    # Using a for each loop to create snow peaks
    for peak in range(5):
        circle(snow_cover_size, extent=180)
        setheading(270)
    end_fill()
    penup()

    # Going to the peak of the left mountain to draw the snow peak
    setheading(135)
    forward(mountain_size - peak_size)
    setheading(225)
    forward(mountain_size * 2)
    setheading(135)
    forward(mountain_size)

    # Following the shape of the left mountain peak to fill it in
    fillcolor(snow_colour)
    begin_fill()
    pendown()
    forward((peak_size/2)+1)
    setheading(225)
    forward(peak_size/1.5)
    setheading(270)

    # Using a for each loop to create snow peaks
    for peak in range(3):
        circle(small_snow_cover_size, extent=180)
        setheading(270)
    end_fill()
    penup()

# ------------------------------------Competitor D - Cloudy weather drawing components------------------------------------


def cloudy_background():  # Drawing the background colour for the competitor.

    cloudy_background_colour = 'light steel blue'
    border_colour = 'black'
    border_width = 2

    # Sending turtle to corner of the grid.
    setheading(270)
    forward(cell_height/2)
    setheading(0)
    forward(cell_width/2)
    setheading(90)

    # Fills grid with the 'light blue' colour
    width(border_width)
    pencolor(border_colour)
    fillcolor(cloudy_background_colour)
    begin_fill()
    pendown()

    # For each loop to fill in grid colour.
    for background in range(2):
        forward(cell_height)
        left(90)
        forward(cell_width)
        left(90)
    end_fill()
    penup()


def large_hill():  # Large hill for the landscape

    hill_colour = 'green'
    border_width = 2

    # Go to starting position for the large hill
    setheading(180)
    forward(cell_width)
    setheading(90)
    forward(cell_height/2)
    setheading(0)
    forward(border_width)
    pendown()

    # Setting the colour for the hill
    fillcolor(hill_colour)
    pencolor(hill_colour)
    begin_fill()
    pendown()

    # Creating a hill and filling it in with the 'green' colour
    circle(-200, extent=35.5)
    setheading(270)
    forward(border_width*3)
    setheading(180)
    forward(cell_width-(border_width*2))
    setheading(90)
    forward(cell_height/2 - (border_width*1.5))
    end_fill()
    penup()


def small_hill():  # Small hill for the landscape

    hill_colour = 'yellow green'
    border_size = 2

    # Go to location of the second hill on the right
    setheading(0)
    forward(cell_width - (border_size*2))
    setheading(180)

    # Fill in the hill with the 'yellow green' colour
    fillcolor(hill_colour)
    pencolor(hill_colour)
    begin_fill()
    pendown()

    # Drawing the hill
    circle(90, extent=58)
    setheading(0)
    forward(cell_width - 44)
    setheading(90)
    forward((cell_height/2) - (border_size*2))
    end_fill()
    penup()


def clouds():  # Drawing clouds for the sky

    cloud_size = 10
    small_cloud_size = 5
    cloud_spacing = 15
    cloud_colour = ('light gray')
    cloud_outline = 'dim grey'

    # Small cloud on the far right
    setheading(110)
    forward(cloud_spacing)
    cloud_drawing(small_cloud_size, cloud_colour, cloud_outline)

    # Big cloud on the right
    setheading(120)
    forward(cloud_spacing)
    cloud_drawing(cloud_size, cloud_colour, cloud_outline)

    # Big cloud on the left
    setheading(200)
    forward(cloud_spacing*2)
    cloud_drawing(cloud_size, cloud_colour, cloud_outline)

    # Small cloud on the far left
    setheading(160)
    forward(cloud_spacing*3)
    cloud_drawing(small_cloud_size, cloud_colour, cloud_outline)

    # Small cloud near the bottom of the hill
    setheading(320)
    forward(cloud_spacing*3)
    cloud_drawing(small_cloud_size, cloud_colour, cloud_outline)


def hilly_road():  # Drawing roads on the hills

    road_colour = 'saddle brown'
    road_size = 10
    border_width = 1

    # Going to the location to start the right road drawing
    setheading(270)
    forward((cell_height/2) - border_width)
    setheading(0)
    forward(road_size*1.5)

    # Filling in the road with the colour 'saddle brown'
    fillcolor(road_colour)
    pencolor(road_colour)
    begin_fill()
    pendown()

    # Drawing the right road
    forward(road_size)
    setheading(90)
    circle(80, extent=28)
    setheading(200)
    circle(80, extent=6)
    setheading(296)
    circle(-80, extent=25)
    end_fill()
    penup()

    # Going to second location for the left road
    setheading(180)
    forward(cell_width/4)
    setheading(90)
    forward(cell_height/5 + (border_width*1.5))

    # Filling in the road with the colour 'saddle brown'
    fillcolor(road_colour)
    pencolor(road_colour)
    begin_fill()
    pendown()

    # Drawing the left road
    setheading(90)
    circle(-20, extent=44)
    setheading(150)
    forward(road_size/2)
    setheading(225)
    circle(20, extent=60)
    setheading(40)
    forward(road_size/2)
    end_fill()
    penup()


def Rectangle(width, height, colour):  # Function draws a rectangle
    fillcolor(colour)
    begin_fill()
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()


def Triangle(length, colour):  # Function draws a triangle
    fillcolor(colour)
    begin_fill()
    forward(length)
    left(135)
    forward(length / sqrt(2))
    left(90)
    forward(length / sqrt(2))
    left(135)
    end_fill()


def Parallelogram(width, height, colour):  # Function draws a parallelogram
    fillcolor(colour)
    begin_fill()
    left(30)
    forward(width)
    left(60)
    forward(height)
    left(120)
    forward(width)
    left(60)
    forward(height)
    left(90)
    end_fill()


def house_on_the_hill():  # Draws a house on the hill with random colours

    house_width = 15
    house_length = 20
    window_size = 5

    # Creating a choice list so random colours are chosen each time for the house

    colour_roof_list = 'blue violet', 'black', 'deep sky blue', 'indian red', 'maroon'

    colour_house_list = 'pale Goldenrod',
    'wheat', 'white', 'light gray', 'cornsilk'

    colour_door_window_list = 'light yellow', 'plum', 'sandy brown', 'dim grey', 'slate gray'

    house_colour = choice(colour_house_list)
    door_colour = choice(colour_door_window_list)
    roof_colour = choice(colour_roof_list)
    window_colour = choice(colour_door_window_list)
    pencolor('black')

    # Drawing the front of the house
    setheading(170)
    forward(cell_height/2.5)
    setheading(0)
    pendown()
    Rectangle(house_width, house_length, house_colour)
    penup()

    # Draw and fill the front door
    setheading(0)
    forward(house_width/3)
    pendown()
    Rectangle(house_width/3, house_length/2, door_colour)
    penup()

    # Drawing the front roof
    setheading(180)
    forward(house_width/3)
    setheading(90)
    forward(house_length)
    setheading(0)
    pendown()
    Triangle(house_width, roof_colour)
    penup()

    # Drawing the side of the house
    setheading(270)
    forward(house_length)
    setheading(0)
    forward(house_width)
    pendown()
    Parallelogram(house_width, house_length, house_colour)
    penup()

    # Draw window on the side of the house
    setheading(90)
    forward(house_width/1.5)
    setheading(0)
    forward(house_width/2.5)
    pendown()
    Parallelogram(window_size / 1.5, window_size, window_colour)
    penup()

    # Going to the location to start drawing the side roof
    setheading(180)
    forward(house_width/2.5)
    setheading(90)
    forward(house_width/1.5)
    setheading(0)

    # Drawing and filling in the side roof
    pendown()
    fillcolor(roof_colour)
    begin_fill()

    left(30)
    forward(house_width)
    left(105)
    forward(house_width / sqrt(2))
    left(75)
    forward(house_width)
    left(105)
    forward(house_width / sqrt(2))
    left(45)
    end_fill()
    penup()


def tree_on_the_hill():  # Drawing a tree on the hill

    tree_top_colour = 'dark green'
    tree_trunk_colour = 'saddle brown'
    pencolor(tree_trunk_colour)
    trunk_size = 10
    tree_top_size = 20

    # Going to the location of the tree
    setheading(0)
    forward(cell_width/1.8)
    setheading(270)
    forward(trunk_size*2)
    setheading(0)

    # Drawing the tree base
    pendown()
    Rectangle(trunk_size/2, trunk_size, tree_trunk_colour)
    penup()

    # Drawing the three triangles to make a tree top
    setheading(90)
    forward(trunk_size)
    setheading(180)
    forward(tree_top_size/3)
    setheading(0)
    Triangle(tree_top_size, tree_top_colour)
    penup()

    # For each loop for the last two triangles
    for tree_top in range(2):
        setheading(90)
        forward(tree_top_size/3)
        setheading(0)
        Triangle(tree_top_size, tree_top_colour)
        penup()

# -------------Putting all the drawing components of each competitor into a draw competitor function---------------------


def draw_rainy_competitor(competitor_A_location):  # Draw rainy competitor
    rainy_colour_background()
    rainy_city_background()
    building_windows()
    street_path()
    lamp_post()
    park_trees()
    moon()
    stars()
    rain(competitor_A_location)


# Functions needed to draw the sunny competitor
def draw_sunny_competitor():
    sunny_colour_background()
    sand_shores()
    sunny_ocean()
    sunny_clouds()
    sun()
    ocean_waves()
    palm_tree_trunk()
    palm_tree_leaves()
    sunny_umbrella()


def draw_snow_competitor(competitor_C_location):  # Snow competitor
    snow_colour_background()
    mountains()
    snowy_road()
    mountain_snow()
    tree_location()
    falling_snow(competitor_C_location)


def draw_cloudy_competitor():  # Functions needed to draw the cloudy competitor
    cloudy_background()
    large_hill()
    small_hill()
    clouds()
    hilly_road()
    house_on_the_hill()
    tree_on_the_hill()


def process_moves(temp_moves):

    # Creating all the required lists
    competitor_A_location = []
    competitor_B_location = []
    competitor_C_location = []
    competitor_D_location = []
    home_location = []  # List of competitors who made it to the home square

    # Go to the middle of the top left hand corner cell - Competitor A
    goto(((-cell_width*7)/2 + (cell_width/2)),
         (((cell_height*7)/2) - (cell_height/2)))
    competitor_A_location.append(pos())
    draw_rainy_competitor(competitor_A_location)
    check_cell_location(competitor_A_location)

    # Go to the middle of the bottom left hand corner cell - Competitor B
    goto(((cell_width*7)/2 - (cell_width/2)),
         (((cell_height*7)/2) - (cell_height/2)))
    competitor_B_location.append(pos())
    draw_snow_competitor(competitor_B_location)

    check_cell_location(competitor_B_location)

    # Go to the middle of the top right hand corner cell - Competitor C
    goto(((-cell_width*7)/2 + (cell_width/2)),
         (((-cell_height*7)/2) + (cell_height/2)))

    competitor_C_location.append(pos())

    check_cell_location(competitor_C_location)
    draw_sunny_competitor()
    # Go to the middle of the bottom right hand corner cell - Competitor D
    goto(((cell_width*7)/2 - (cell_width/2)),
         (((-cell_height*7)/2) + (cell_height/2)))

    competitor_D_location.append(pos())
    draw_cloudy_competitor()
    check_cell_location(competitor_D_location)

    # Length of array temp_moves
    for i in range(len(temp_moves)):
        # print("Move number", i)
        pendown()
        pencolor('black')
        # print(temp_moves[i][0])
        if (temp_moves[i][0] == 'Competitor A'):
            penup()
            goto(competitor_A_location[-1])
            check_cell_location(competitor_A_location)
            if (temp_moves[i][1] == 'Down'):
                if ((competitor_A_location[-1][1] - cell_height) < -((cell_height*grid_size)/2)):
                    pass

                else:
                    check_cell_location(competitor_A_location)
                    setheading(270)
                    forward(cell_height)
                    competitor_A_location[-1] = pos()
                    draw_rainy_competitor(competitor_A_location)
                    competitor_A_location[-1] = pos()
                    check_if_home(competitor_A_location,
                                  home_location, "Competitor A")

            elif temp_moves[i][1] == 'Left':
                if ((competitor_A_location[-1][0] - cell_width) < -((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_A_location)
                    setheading(180)
                    forward(cell_width)
                    competitor_A_location[-1] = pos()
                    draw_rainy_competitor(competitor_A_location)
                    competitor_A_location[-1] = pos()
                    check_if_home(competitor_A_location,
                                  home_location, "Competitor A")

            elif temp_moves[i][1] == 'Right':
                if (competitor_A_location[-1][0] + cell_width > ((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_A_location)
                    setheading(0)
                    forward(cell_width)
                    competitor_A_location[-1] = pos()
                    draw_rainy_competitor(competitor_A_location)
                    competitor_A_location[-1] = pos()
                    check_if_home(competitor_A_location,
                                  home_location, "Competitor A")

            elif temp_moves[i][1] == 'Up':
                if (competitor_A_location[-1][1] + cell_height > ((cell_height * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_A_location)
                    setheading(90)
                    forward(cell_height)
                    competitor_A_location[-1] = pos()
                    draw_rainy_competitor(competitor_A_location)
                    competitor_A_location[-1] = pos()
                    check_if_home(competitor_A_location,
                                  home_location, "Competitor A")

        elif (temp_moves[i][0] == 'Competitor B'):
            penup()
            goto(competitor_B_location[-1])
            check_cell_location(competitor_B_location)
            if (temp_moves[i][1] == 'Down'):
                if ((competitor_B_location[-1][1] - cell_height) < -((cell_height*grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_B_location)
                    setheading(270)
                    forward(cell_height)
                    competitor_B_location[-1] = pos()
                    draw_snow_competitor(competitor_B_location)
                    competitor_B_location[-1] = pos()
                    check_if_home(competitor_B_location,
                                  home_location, "Competitor B")

            elif temp_moves[i][1] == 'Left':
                if ((competitor_B_location[-1][0] - cell_width) < -((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_B_location)
                    setheading(180)
                    forward(cell_width)
                    competitor_B_location[-1] = pos()
                    draw_snow_competitor(competitor_B_location)
                    competitor_B_location[-1] = pos()
                    check_if_home(competitor_B_location,
                                  home_location, "Competitor B")

            elif temp_moves[i][1] == 'Right':
                if (competitor_B_location[-1][0] + cell_width > ((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_B_location)
                    setheading(0)
                    forward(cell_width)
                    competitor_B_location[-1] = pos()
                    draw_snow_competitor(competitor_B_location)
                    competitor_B_location[-1] = pos()
                    check_if_home(competitor_B_location,
                                  home_location, "Competitor B")

            elif temp_moves[i][1] == 'Up':
                if (competitor_B_location[-1][1] + cell_height > ((cell_height * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_B_location)
                    setheading(90)
                    forward(cell_height)
                    competitor_B_location[-1] = pos()
                    draw_snow_competitor(competitor_B_location)
                    competitor_B_location[-1] = pos()
                    check_if_home(competitor_B_location,
                                  home_location, "Competitor B")

        elif (temp_moves[i][0] == 'Competitor C'):
            penup()
            goto(competitor_C_location[-1])
            check_cell_location(competitor_C_location)
            if (temp_moves[i][1] == 'Down'):
                if ((competitor_C_location[-1][1] - cell_height) < -((cell_height*grid_size)/2)):
                    pass

                else:
                    check_cell_location(competitor_C_location)
                    setheading(270)
                    forward(cell_height)
                    competitor_C_location[-1] = pos()
                    draw_sunny_competitor()
                    competitor_C_location[-1] = pos()
                    check_if_home(competitor_C_location,
                                  home_location, "Competitor C")

            elif temp_moves[i][1] == 'Left':
                if ((competitor_C_location[-1][0] - cell_width) < -((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_C_location)
                    setheading(180)
                    forward(cell_width)
                    competitor_C_location[-1] = pos()
                    draw_sunny_competitor()
                    competitor_C_location[-1] = pos()
                    check_if_home(competitor_C_location,
                                  home_location, "Competitor C")

            elif temp_moves[i][1] == 'Right':
                if (competitor_C_location[-1][0] + cell_width > ((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_C_location)
                    setheading(0)
                    forward(cell_width)
                    competitor_C_location[-1] = pos()
                    draw_sunny_competitor()
                    competitor_C_location[-1] = pos()
                    check_if_home(competitor_C_location,
                                  home_location, "Competitor C")

            elif temp_moves[i][1] == 'Up':
                if (competitor_C_location[-1][1] + cell_height > ((cell_height * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_C_location)
                    setheading(90)
                    forward(cell_height)
                    competitor_C_location[-1] = pos()
                    draw_sunny_competitor()
                    competitor_C_location[-1] = pos()
                    check_if_home(competitor_C_location,
                                  home_location, "Competitor C")

        elif (temp_moves[i][0] == 'Competitor D'):
            penup()
            goto(competitor_D_location[-1])
            check_cell_location(competitor_D_location)
            if (temp_moves[i][1] == 'Down'):
                if ((competitor_D_location[-1][1] - cell_height) < -((cell_height*grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_D_location)
                    setheading(270)
                    forward(cell_height)
                    competitor_D_location[-1] = pos()
                    draw_cloudy_competitor()
                    competitor_D_location[-1] = pos()
                    check_if_home(competitor_D_location,
                                  home_location, "Competitor D")

            elif temp_moves[i][1] == 'Left':
                if ((competitor_D_location[-1][0] - cell_width) < -((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_D_location)
                    setheading(180)
                    forward(cell_width)
                    competitor_D_location[-1] = pos()
                    draw_cloudy_competitor()
                    competitor_D_location[-1] = pos()
                    check_if_home(competitor_D_location,
                                  home_location, "Competitor D")

            elif temp_moves[i][1] == 'Right':
                if (competitor_D_location[-1][0] + cell_width > ((cell_width * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_D_location)
                    setheading(0)
                    forward(cell_width)
                    competitor_D_location[-1] = pos()
                    draw_cloudy_competitor()
                    competitor_D_location[-1] = pos()
                    check_if_home(competitor_D_location,
                                  home_location, "Competitor D")

            elif temp_moves[i][1] == 'Up':
                if (competitor_D_location[-1][1] + cell_height > ((cell_height * grid_size)/2)):
                    pass
                else:
                    check_cell_location(competitor_D_location)
                    setheading(90)
                    forward(cell_height)
                    competitor_D_location[-1] = pos()
                    draw_cloudy_competitor()
                    competitor_D_location[-1] = pos()
                    check_if_home(competitor_D_location,
                                  home_location, "Competitor D")

    penup()
    pencolor('black')
    big_font = ('Arial', (12 * cell_width) // 100, 'normal')
    if home_location:
        goto(cell_width*4, 50)
        write('First competitor\nto reach home:', align='left', font=big_font)
        pendown()
        goto(cell_width*4.5, 0)
        if (home_location[0] == "Competitor A"):
            competitor_A_location[-1] = pos()
            draw_rainy_competitor(competitor_A_location)
        elif (home_location[0] == "Competitor B"):
            competitor_B_location[-1] = pos()
            draw_snow_competitor(competitor_B_location)
        elif (home_location[0] == "Competitor C"):
            competitor_C_location[-1] = pos()
            draw_sunny_competitor()
        elif (home_location[0] == "Competitor D"):
            competitor_D_location[-1] = pos()
            draw_cloudy_competitor()
    else:
        goto((cell_width*4)-20, -30)
        pendown()
        write('No competitor\nreached the\nhome square',
              align='left', font=big_font)


def check_if_home(competitor_location, home_location, competitor_name):
    if (-(cell_width/2) <= competitor_location[0][0] <= (cell_width/2)
            and (-(cell_height/2) <= competitor_location[0][1] <= (cell_height/2))):
        home_location.append(competitor_name)
        return home_location

    else:
        pass


        #
        #--------------------------------------------------------------------#
        #-----Main Program---------------------------------------------------#
        #
        # This main program sets up the canvas, ready for you to start
        # drawing your solution, and calls your solution.  Do not change
        # any of this code except as indicated by the comments marked '*****'.
        #
        # Set up the drawing canvas
        # ***** You can change the background and line colours, choose
        # ***** whether or not to label the axes, etc, by providing
        # ***** arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its competitors
title('Competing Weathers - Rain, Snow, Sun, Cloud')

# Call the student's function to process the moves
# ***** While developing your program you can call the
# ***** "random_moves" function with a fixed seed for the random
# ***** number generator, but your final solution must work with
# ***** "random_moves()" as the argument to "process_moves", i.e.,
# ***** for any data set that can be returned by calling
# ***** "random_moves" with no seed.
process_moves(random_moves)  # <-- this will be used for assessment

# Alternative function call to help debug your code
# ***** The following function call can be used instead of
# ***** the one above while debugging your code, but will
# ***** not be used for assessment. Comment out the call
# ***** above and uncomment the one below if you want to
# ***** call your "process_moves" function with one of the
# ***** "fixed" data sets above, so that you know in advance
# ***** what the moves are.
# process_moves(fixed_data_set_00) # <-- not used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid.
release_drawing_canvas()

#
#--------------------------------------------------------------------#
