'''
    Project
    Milestone 1
    Turtle Pre-work
'''

import turtle
import m5_leaderboard
t = turtle.Turtle()
win = turtle.Screen()
win.setup(width = 800, height = 600)

def draw_square(side):
    '''
    Function: draws a square
        takes in a side

    Returns a square with chosen length of sides
    '''
    
    t.forward(side) # move forward
    t.left(90) # rotate turtle 90 degrees

    t.forward(side)
    t.left(90)

    t.forward(side)
    t.left(90)

    t.forward(side)
    t.left(90)

def draw_tile():
    '''
    Function: draws tiles indicating the play space for the player

    Draws a grid with a slot for each tile to be placed in
    '''

    # create list of cooridinates
    
    lst = [(-300, 100), (-200, 100), (-100, 100), (0, 100),
               (-300, 0), (-200, 0), (-100, 0), (0, 0),
               (-300, -100), (-200, -100), (-100, -100), (0, -100),
               (-300, -200), (-200, -200), (-100, -200), (0, -200),]

    t.width(3) # set thickness 
    t.hideturtle()
    t.speed(100) # decrease player wait time

    # draw grid based on coordinates from list
    
    for block in range(len(lst)):
        if block == 0: # draw first outline
            t.penup() # stop drawing
            t.goto(lst[block]) # move to coordinate
            t.pendown() # continue drawing
            draw_square(100) # draw square to fit tile
        elif block == 1:
            t.goto(lst[block]) # draw adjacent squares
            draw_square(100) 
        elif block == 2:
            t.goto(lst[block])
            draw_square(100)
        elif block == 3:
            t.goto(lst[block])
            draw_square(100)
        elif block == 4:
            t.penup() # finish drawing row
            t.goto(lst[block])
            t.pendown() # start new row
            draw_square(100)
        elif block == 5:
            t.goto(lst[block]) # draw adjacent squares
            draw_square(100)
        elif block == 6:
            t.goto(lst[block])
            draw_square(100)
        elif block == 7:
            t.goto(lst[block])
            draw_square(100)
        elif block == 8:
            t.penup() # finish row
            t.goto(lst[block])
            t.pendown() # start new row
            draw_square(100)
        elif block == 9:
            t.goto(lst[block]) # draw adjacent squares
            draw_square(100)
        elif block == 10:
            t.goto(lst[block])
            draw_square(100)
        elif block == 11:
            t.goto(lst[block])
            draw_square(100)
        elif block == 12:
            t.penup() # finish row
            t.goto(lst[block])
            t.pendown() # start new row
            draw_square(100)
        elif block == 13:
            t.goto(lst[block]) # draw adjacent squares
            draw_square(100)
        elif block == 14:
            t.goto(lst[block])
            draw_square(100)
        elif block == 15:
            t.goto(lst[block])
            draw_square(100)

def draw_rectangle(length, width):
    '''
    Function: draws a rectangle
        takes in length and width

    Returns a rectangle of any size with chosen length and width
    '''
    
    t.forward(length) # draw side
    t.left(90) # rotate turtle 90 degrees

    t.forward(width)
    t.left(90)

    t.forward(length)
    t.left(90)

    t.forward(width)

def draw_user_interface():
    '''
    Function: draws the space for the UI

    Returns area for the interactable buttons and
        player moves tracker
    '''
    
    t.hideturtle()
    t.width(3) # increase thickness
    t.penup()
    t.goto(-300, -350) # go to starting coordinate
    t.pendown()
    draw_rectangle(650, 100) # draw appropriately sized rectangle

    t.penup()
    t.goto(-280, -310) # move inside rectangle
    t.pendown()
    t.write("Player Moves: ",
            font = ('Ariel',
                    17, 'normal')) # display player moves tracker heading

    m5_leaderboard.leader_tracker() # display leaderboard information

def draw_leaderboard():
    '''
    Function: draws the leaderboard space

    Returns the area in which leaderboard
        information is displayed
    '''
    t.hideturtle()
    t.width(3) # increase thickness
    t.penup()
    t.goto(150, 200) # move to starting coordinate
    t.pendown()
    draw_rectangle(400, 200) # draw appropriately sized rectangle
    
    t.penup()
    t.goto(160, 160) # move inside rectangle
    t.pendown()
    t.write("Leaderboard:",
            font = ('Ariel',
                    17, 'normal')) # display leaderboard heading
    t.penup()
    t.goto(160, 130)
    t.pendown()
    t.write("Moves -- Player",
            font = ('Ariel',
                    15, 'normal')) # make heading

