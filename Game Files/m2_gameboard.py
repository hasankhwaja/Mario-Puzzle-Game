'''
    Project
    Milestone 2
    Drawing the gameboard
'''

import m3_placement
import m1_prework
import random
import turtle
import time
win = turtle.Screen()
win.setup(width = 800, height = 600)
game = 'mario' # set default puzzle

def user_choice():
    '''
    Function: creates a text box that loads a puzzle

    Returns the puzzle of the player's choice
    '''

    # create text box
    
    puzzle_choice = turtle.textinput("Puzzle Slider",
                        """Enter the name of the puzzle you wish to load:
    mario
    luigi
    yoshi
    fifteen
    smiley""")

    return puzzle_choice

def load_menu(x, y):
    '''
    Function: clears the board from the current puzzle then
        loads the puzzle chosen by the player

    Puzzle is loaded in its playable state
    '''

    # set puzzle_choice, user_choice and game to be equal

    global game
    puzzle_choice = user_choice() 
    game = puzzle_choice
    puzzle_choice = puzzle_choice.lower() # convert input to lowercase

    if puzzle_choice == 'mario': # take in chosen puzzle
        m3_placement.get_mario_play() # load new puzzle
    elif puzzle_choice == 'luigi':
        m3_placement.get_luigi_play()
    elif puzzle_choice == 'yoshi':
        m3_placement.get_yoshi_play()
    elif puzzle_choice == 'fifteen':
        m3_placement.get_fifteen_play()
    elif puzzle_choice == 'smiley':
        m3_placement.get_smiley_play()
    else:
        win.addshape('Resources/file_error.gif')
        t = turtle.Turtle()
        t.shape('Resources/file_error.gif') # show error if file does not exist
        time.sleep(5)
        t.hideturtle()
        raise FileNotFoundError
        with open('5001_puzzle.err', 'w') as infile: # log error
            infile.write('Puzzle file not found')
            

def reset_puzzle(x, y):
    '''
    Function: Resets the puzzle to its solved state
        Takes in a click from the player via the onscreen reset button

    Returns the puzzle such that the game is easier to win
    '''
    puzzle_choice = game # set puzzle equal to current game
    puzzle_choice = puzzle_choice.lower() # convert player input to lowercase
    
    if puzzle_choice == 'mario': # take in chosen puzzle
        m3_placement.get_mario_original(x, y) # solve puzzle
    elif puzzle_choice == 'luigi':
        m3_placement.get_luigi_original(x, y)
    elif puzzle_choice == 'yoshi':
        m3_placement.get_yoshi_original(x, y)
    elif puzzle_choice == 'fifteen':
        m3_placement.get_fifteen_original(x, y)
    elif puzzle_choice == 'smiley':
        m3_placement.get_smiley_original(x, y)

def exit_puzzle(x, y):
    '''
    Function: Exits puzzle

    Shows exit message to player upon clicking exit button
    '''
    
    win.addshape('Resources/quitmsg.gif') # add shape
    turtle.shape('Resources/quitmsg.gif') # show message
    time.sleep(2)
    turtle.bye() # close screen

def load_asset():
    '''
    Function: creates interactable buttons
        loads in exit, menu, and reset buttons to the game

    Returns the function of whichever button is clicked by the player
    '''
    
    win.addshape('Resources/quitbutton.gif') # add button
    z = turtle.Turtle()
    z.hideturtle()
    z.penup()
    z.goto(250, -300) # move turtle
    z.showturtle()
    z.shape('Resources/quitbutton.gif')
    z.onclick(exit_puzzle) # add exit function

    win.addshape('Resources/loadbutton.gif') # add button
    y = turtle.Turtle()
    y.hideturtle()
    y.penup()
    y.goto(150, -300) # move turtle
    y.showturtle()
    y.shape('Resources/loadbutton.gif')
    y.onclick(load_menu) # add load function
    
    win.addshape('Resources/resetbutton.gif') # add button
    x = turtle.Turtle()
    x.hideturtle()
    x.penup()
    x.goto(50, -300) # move turtle
    x.showturtle()
    x.shape('Resources/resetbutton.gif')
    x.onclick(reset_puzzle) # add reset function

def get_hud():
    '''
    Function: draws the UI and leaderboard areas of the screen
        and calls creation of buttons for player 

    Areas drawn are distinguished from the play space
    '''
    
    m1_prework.draw_user_interface() # draw UI
    m1_prework.draw_leaderboard() # draw leaderboard 
    load_asset() # load buttons

def splash_screen():
    '''
    Function: Shows splash screen to player

    Splash screen is shown shortly before the start of the game
    '''
    
    win.bgpic('Resources/splash_screen.gif') # set splash screen as background
    win.update() 
    time.sleep(2) # show for a few seconds
    win.bgpic('nopic') # remove splash screen
