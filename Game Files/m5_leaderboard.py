'''
    Project
    Hasan Khwaja
    Milestone 5: Leaderboard
'''

import turtle

def leader_tracker():
    '''
    Function: writes to the in game leader board

    Text file is written line by line 
    '''
    try:
        with open('leader_data.txt', 'r') as fd: # open fiile
            lines = [line.strip() for line in fd]
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile: # if txt file not found
            infile.write('Could not open file, leader_data.txt not found')
            
    arrange_leader(lines) # send lines to be sorted

def arrange_leader(lines):
    '''
    Function: takes in player data from leader_data.txt

    Sorts player list for leaderboard
    '''

    v = turtle.Turtle()
    y_coordinate = 100 # initialize y coordinate
    line_number = 0 # initalize line number
    
    lst = [] # create empty list
    for i in lines:
        lst.append(i) # append each line

    lst.sort(key=sort_key) # sort list

    for i in range(len(lst)):
        v.hideturtle()
        v.penup()
        v.goto(160, y_coordinate) # send turtle to initial coordinate
        v.write(lst[i], font = ('Ariel',
                13, 'normal')) # write top line
        y_coordinate = y_coordinate - 20
        line_number += 1 # continue writing top ten
        if line_number == 10:
            break
            
    return

def sort_key(text: str):
    '''
    Function: takes in number of moves and
        name of player from text file

    Returns key based on moves for sorting
    '''
    
    digits = text[0:3] # define characters
    letter = text[4:] # define rest of string

    return (int(digits), letter)
