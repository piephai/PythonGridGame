
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: PUT YOUR STUDENT NUMBER HERE
#    Student name: PUT YOUR NAME HERE
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
    setheading(90)  # face north
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
        big_font = ('Arial', (24 * cell_width) // 100, 'normal')
        # Text to the right of the grid
        penup()
        goto((grid_size * cell_width) // 2 + 50, -cell_height // 3)
        write('This space\nreserved for\nPart B', align='left', font=big_font)

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

def set_moves(the_seed=None, max_rounds=30):
    competitors = ['Competitor A', 'Competitor B']
    # Decide how many rounds of moves to make
    num_rounds = randint(0, max_rounds)
    # For each round generate a random move for each competitor
    # and save and print it
    moves = []
    for round_no in range(num_rounds):
        print()
        for competitor in competitors:
            # Create a random move
            move = [competitor,
                    choice(['Left', 'Right', 'Up', 'Down'])]
            # Print it to the shell and remember it
            print(move)
            moves.append(move)

    return moves


temp_moves = set_moves(the_seed=None, max_rounds=30)


# def check_out_of_bound(temp_moves)


def process_moves(temp_moves):

    # competitor_A_location = []
    # heading = 0
    # forward(90)
    # competitor_A_location.append(pos())
    # setheading(heading + 90)
    # forward(90)
    # competitor_A_location.append(pos())
    # forward(90)

    # for element in competitor_A_location:
    #     print(element)
    competitor_A_location = []
    competitor_B_location = []
    pendown()
    goto((-420 + (cell_width/2)), (-315 + (cell_height/2)))
    dot(10, 'red')
    competitor_A_location.append(pos())
    goto((-420 + (cell_width/2)), (315 - (cell_height/2)))
    dot(10, 'green')
    competitor_B_location.append(pos())
    # for i in competitor_A_location:
    #     print(i)

    for i in range(len(temp_moves)):
        print("Move number", i)
        pendown()
        pencolor('black')
        print(temp_moves[i][0])
        if (temp_moves[i][0] == 'Competitor A'):
            penup()
            goto(competitor_A_location[-1])
            pendown()
            if (temp_moves[i][1] == 'Down'):
                if ((competitor_A_location[-1][1] - cell_height) < -((cell_height*grid_size)/2)):
                    print("Out of range down")
                    competitor_A_location.append(pos())
                    print(competitor_A_location[-1])
                else:
                    setheading(270)
                    forward(cell_height)
                    dot(10, 'red')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_A_location.append(pos())
                    print(competitor_A_location[-1])

            elif temp_moves[i][1] == 'Left':
                if ((competitor_A_location[-1][0] - cell_width) < -((cell_width * grid_size)/2)):
                    print("Out of range left")
                else:
                    setheading(180)
                    forward(cell_width)
                    dot(10, 'red')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_A_location.append(pos())
                    print(competitor_A_location[-1])

            elif temp_moves[i][1] == 'Right':
                if (competitor_A_location[-1][0] + cell_width > ((cell_width * grid_size)/2)):
                    print("Out of range right")
                else:
                    setheading(0)
                    forward(cell_width)
                    dot(10, 'red')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_A_location.append(pos())
                    print(competitor_A_location[-1])

            elif temp_moves[i][1] == 'Up':
                if (competitor_A_location[-1][1] + cell_height > ((cell_height * grid_size)/2)):
                    print("Out of range top")
                else:
                    setheading(90)
                    forward(cell_height)
                    dot(10, 'red')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_A_location.append(pos())
                    print(competitor_A_location[-1])

        elif (temp_moves[i][0] == 'Competitor B'):
            penup()
            goto(competitor_B_location[-1])
            pendown()
            if (temp_moves[i][1] == 'Down'):
                if ((competitor_B_location[-1][1] - cell_height) < -((cell_height*grid_size)/2)):
                    print("Out of range down")
                    competitor_B_location.append(pos())
                    print(competitor_B_location[-1])
                else:
                    setheading(270)
                    forward(cell_height)
                    dot(10, 'green')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_B_location.append(pos())
                    print(competitor_B_location[-1])

            elif temp_moves[i][1] == 'Left':
                if ((competitor_B_location[-1][0] - cell_width) < -((cell_width * grid_size)/2)):
                    print("Out of range left")
                else:
                    setheading(180)
                    forward(cell_width)
                    dot(10, 'green')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_B_location.append(pos())
                    print(competitor_B_location[-1])

            elif temp_moves[i][1] == 'Right':
                if (competitor_B_location[-1][0] + cell_width > ((cell_width * grid_size)/2)):
                    print("Out of range right")
                else:
                    setheading(0)
                    forward(cell_width)
                    dot(10, 'green')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_B_location.append(pos())
                    print(competitor_B_location[-1])

            elif temp_moves[i][1] == 'Up':
                if (competitor_B_location[-1][1] + cell_height > ((cell_height * grid_size)/2)):
                    print("Out of range top")
                else:
                    setheading(90)
                    forward(cell_height)
                    dot(10, 'green')
                    # setheading(0)
                    # forward(cell_width)
                    # setheading(90)
                    # forward(cell_height//2)
                    competitor_B_location.append(pos())
                    print(competitor_B_location[-1])


# def draw_snow():

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
speed('normal')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its competitors
title('Describe your theme and competitors here')

# Call the student's function to process the moves
# ***** While developing your program you can call the
# ***** "random_moves" function with a fixed seed for the random
# ***** number generator, but your final solution must work with
# ***** "random_moves()" as the argument to "process_moves", i.e.,
# ***** for any data set that can be returned by calling
# ***** "random_moves" with no seed.
process_moves(temp_moves)  # <-- this will be used for assessment

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
