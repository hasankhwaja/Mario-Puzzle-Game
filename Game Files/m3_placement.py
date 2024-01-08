'''
    Project
    Milestone 3
    Tile placement
'''

import m1_prework
import random
import time
import turtle
win = turtle.Screen()
win.setup(width = 800, height = 600)

clicks = 0 # initialize number of clicks
moves = 0 # initialize number of player moves
player = None # initialize player name 

# define turtles

t = turtle.Turtle()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()
i = turtle.Turtle()
j = turtle.Turtle()
k = turtle.Turtle()
l = turtle.Turtle()
m = turtle.Turtle()
n = turtle.Turtle()
o = turtle.Turtle()
q = turtle.Turtle()

def load_yoshi(puzzle_state):
    '''
    Function: takes in the state of the puzzle and
        uses coordinates to create a gameboard

    Returns a puzzle in its playable and solved state
    '''

    # track player clicks
    
    global clicks
    clicks = 0
    click_tracker()

    # add yoshi images
    try:
        win.addshape('Images/yoshi/4.gif')
        win.addshape('Images/yoshi/3.gif')
        win.addshape('Images/yoshi/2.gif')
        win.addshape('Images/yoshi/blank.gif')
        win.addshape('Images/yoshi/yoshi_thumbnail.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Yoshi image not found') # if image missing

    # create thumbnail

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/yoshi/yoshi_thumbnail.gif')

    # gameboard coordinates
    
    lst = [(-250, 150), (-250, 50), (-150, 150), (-150, 50)]

    # unused coordinates for blank tiles
    
    lst2 = [(-50, 150), (50, 150), (-50, 50), (50, 50),
               (-250, -50), (-150, -50), (-50, -50), (50, -50),
               (-250, -150), (-150, -150), (-50, -150), (50, -150),]

    # load solved puzzle

    if puzzle_state == 'original':
        for block in range(len(lst)): # use gameboard coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to coordinate
                t.showturtle()
                t.shape('Images/yoshi/4.gif') # define image
                t.onclick(swap_tile) # provide click function
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/yoshi/2.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/yoshi/3.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/yoshi/blank.gif')

    # load unsolved puzzle
    
    if puzzle_state == 'play':
        random.shuffle(lst) # shuffle coordinates
        for block in range(len(lst)): # use gameboard coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to random coordinate
                t.showturtle()
                t.shape('Images/yoshi/4.gif') # define image
                t.onclick(swap_tile) # provide click function
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/yoshi/2.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/yoshi/3.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/yoshi/blank.gif')

    # fill rest of gameboard

    if puzzle_state == 'play': # use state that is loaded first
        for block in range(len(lst2)): # use list of unused coordinates
            if block == 0:
                c.hideturtle() # keep turtle hidden
                c.penup()
                c.goto(lst2[block]) # occupy coordinate with unused turtle
            elif block == 1: # continue for rest of turtles
                d.hideturtle()
                d.penup()
                d.goto(lst2[block])
            elif block == 2:
                n.hideturtle()
                n.penup()
                n.goto(lst2[block])
            elif block == 3:
                e.hideturtle()
                e.penup()
                e.goto(lst2[block])
            if block == 4:
                f.hideturtle()
                f.penup()
                f.goto(lst2[block])
            elif block == 5:
                g.hideturtle()
                g.penup()
                g.goto(lst2[block])
            elif block == 6:
                h.hideturtle()
                h.penup()
                h.goto(lst2[block])
            elif block == 7:
                i.hideturtle()
                i.penup()
                i.goto(lst2[block])
            elif block == 8:
                j.hideturtle()
                j.penup()
                j.goto(lst2[block])
            elif block == 9:
                k.hideturtle()
                k.penup()
                k.goto(lst2[block])
            elif block == 10:
                l.hideturtle()
                l.penup()
                l.goto(lst2[block])
            elif block == 11:
                m.hideturtle()
                m.penup()
                m.goto(lst2[block])
    turtle.done()

def load_mario(puzzle_state):
    '''
    Function: takes in the state of the puzzle and
        uses coordinates to create a gameboard

    Returns a puzzle in its playable and solved state
    '''

    # track player moves
    
    global clicks
    clicks = 0
    click_tracker()

    # add mario images
    try:
        win.addshape('Images/mario/16.gif')
        win.addshape('Images/mario/15.gif')
        win.addshape('Images/mario/14.gif')
        win.addshape('Images/mario/13.gif')
        win.addshape('Images/mario/12.gif')
        win.addshape('Images/mario/11.gif')
        win.addshape('Images/mario/10.gif')
        win.addshape('Images/mario/9.gif')
        win.addshape('Images/mario/8.gif')
        win.addshape('Images/mario/7.gif')
        win.addshape('Images/mario/6.gif')
        win.addshape('Images/mario/5.gif')
        win.addshape('Images/mario/4.gif')
        win.addshape('Images/mario/3.gif')
        win.addshape('Images/mario/2.gif')
        win.addshape('Images/mario/blank.gif')
        win.addshape('Images/mario/mario_thumbnail.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Mario image not found') # if image missing

    # create thumbnail

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/mario/mario_thumbnail.gif')

    # use one list for all turtles being used

    lst = [(-250, 150), (-150, 150), (-50, 150), (50, 150),
               (-250, 50), (-150, 50), (-50, 50), (50, 50),
               (-250, -50), (-150, -50), (-50, -50), (50, -50),
               (-250, -150), (-150, -150), (-50, -150), (50, -150),]

    # load solved puzzle

    if puzzle_state == 'original':
        for block in range(len(lst)): # take in coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # move to set coordinate
                t.showturtle()
                t.shape('Images/mario/16.gif') # define image
                t.onclick(swap_tile) # provide click function
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/mario/15.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/mario/14.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/mario/13.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/mario/12.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/mario/11.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/mario/10.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/mario/9.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                h.hideturtle()
                h.penup()
                h.goto(lst[block])
                h.showturtle()
                h.shape('Images/mario/8.gif')
                h.onclick(swap_tile_h)
            elif block == 9:
                i.hideturtle()
                i.penup()
                i.goto(lst[block])
                i.showturtle()
                i.shape('Images/mario/7.gif')
                i.onclick(swap_tile_i)
            elif block == 10:
                j.hideturtle()
                j.penup()
                j.goto(lst[block])
                j.showturtle()
                j.shape('Images/mario/6.gif')
                j.onclick(swap_tile_j)
            elif block == 11:
                k.hideturtle()
                k.penup()
                k.goto(lst[block])
                k.showturtle()
                k.shape('Images/mario/5.gif')
                k.onclick(swap_tile_k)
            elif block == 12:
                l.hideturtle()
                l.penup()
                l.goto(lst[block])
                l.showturtle()
                l.shape('Images/mario/4.gif')
                l.onclick(swap_tile_l)
            elif block == 13:
                m.hideturtle()
                m.penup()
                m.goto(lst[block])
                m.showturtle()
                m.shape('Images/mario/3.gif')
                m.onclick(swap_tile_m)
            elif block == 14:
                n.hideturtle()
                n.penup()
                n.goto(lst[block])
                n.showturtle()
                n.shape('Images/mario/2.gif')
                n.onclick(swap_tile_n)
            elif block == 15:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/mario/blank.gif')

    if puzzle_state == 'play': # load unsolved puzzle
        random.shuffle(lst) # randomize coordinates
        for block in range(len(lst)): # take in random coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to random coordinate
                t.showturtle()
                t.shape('Images/mario/16.gif') # define turtle as image
                t.onclick(swap_tile) # provide click function
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/mario/15.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/mario/14.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/mario/13.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/mario/12.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/mario/11.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/mario/10.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/mario/9.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                h.hideturtle()
                h.penup()
                h.goto(lst[block])
                h.showturtle()
                h.shape('Images/mario/8.gif')
                h.onclick(swap_tile_h)
            elif block == 9:
                i.hideturtle()
                i.penup()
                i.goto(lst[block])
                i.showturtle()
                i.shape('Images/mario/7.gif')
                i.onclick(swap_tile_i)
            elif block == 10:
                j.hideturtle()
                j.penup()
                j.goto(lst[block])
                j.showturtle()
                j.shape('Images/mario/6.gif')
                j.onclick(swap_tile_j)
            elif block == 11:
                k.hideturtle()
                k.penup()
                k.goto(lst[block])
                k.showturtle()
                k.shape('Images/mario/5.gif')
                k.onclick(swap_tile_k)
            elif block == 12:
                l.hideturtle()
                l.penup()
                l.goto(lst[block])
                l.showturtle()
                l.shape('Images/mario/4.gif')
                l.onclick(swap_tile_l)
            elif block == 13:
                m.hideturtle()
                m.penup()
                m.goto(lst[block])
                m.showturtle()
                m.shape('Images/mario/3.gif')
                m.onclick(swap_tile_m)
            elif block == 14:
                n.hideturtle()
                n.penup()
                n.goto(lst[block])
                n.showturtle()
                n.shape('Images/mario/2.gif')
                n.onclick(swap_tile_n)
            elif block == 15:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/mario/blank.gif')
    turtle.done()

def load_luigi(puzzle_state):
    '''
    Function: takes in the state of the puzzle and
        uses coordinates to create a gameboard

    Returns a puzzle in its playable and solved state
    '''

    # track player moves
    
    global clicks
    clicks = 0
    click_tracker()

    # add luigi images
    try:
        win.addshape('Images/luigi/9.gif')
        win.addshape('Images/luigi/8.gif')
        win.addshape('Images/luigi/7.gif')
        win.addshape('Images/luigi/6.gif')
        win.addshape('Images/luigi/5.gif')
        win.addshape('Images/luigi/4.gif')
        win.addshape('Images/luigi/3.gif')
        win.addshape('Images/luigi/2.gif')
        win.addshape('Images/luigi/blank.gif')
        win.addshape('Images/luigi/luigi_thumbnail.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Luigi image not found') # if image missing

    # create thumbnail

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/luigi/luigi_thumbnail.gif')

    # list of used coordinates

    lst = [(-250, 150), (-150, 150), (-50, 150),
               (-250, 50), (-150, 50), (-50, 50),
               (-250, -50), (-150, -50), (-50, -50)]

    # list of unused coordinates

    lst2 = [(50, 150), (50, 50), (50, -50),
               (-250, -150), (-150, -150), (-50, -150), (50, -150),]

    # load solved puzzle

    if puzzle_state == 'original':
        for block in range(len(lst)): # take in list of used coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # move turtle to set position
                t.showturtle()
                t.shape('Images/luigi/9.gif') # define image 
                t.onclick(swap_tile) # provide click function
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/luigi/8.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/luigi/7.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/luigi/6.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/luigi/5.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/luigi/4.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/luigi/3.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/luigi/2.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/luigi/blank.gif')

    # load unsolved puzzle 

    if puzzle_state == 'play':
        random.shuffle(lst) # randomize coordinates
        for block in range(len(lst)): # take in coordinates in random order
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # move turtle to random coordinate 
                t.showturtle()
                t.shape('Images/luigi/9.gif') # # define turtle as image 
                t.onclick(swap_tile) # provide click function 
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/luigi/8.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/luigi/7.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/luigi/6.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/luigi/5.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/luigi/4.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/luigi/3.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/luigi/2.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/luigi/blank.gif')

    # take care of unused tiles

    if puzzle_state == 'play': # used puzzle state that is loaded first 
        for block in range(len(lst2)): # take in list of unused cooridinates
            if block == 0:
                h.hideturtle() # keep turtle hidden 
                h.penup()
                h.goto(lst2[block]) # occupy coordinate
            elif block == 1: # continue for rest of turtles
                i.hideturtle()
                i.penup()
                i.goto(lst2[block])
            elif block == 2:
                j.hideturtle()
                j.penup()
                j.goto(lst2[block])
            elif block == 3:
                k.hideturtle()
                k.penup()
                k.goto(lst2[block])
            elif block == 4:
                l.hideturtle()
                l.penup()
                l.goto(lst2[block])
            elif block == 5:
                m.hideturtle()
                m.penup()
                m.goto(lst2[block])
            elif block == 6:
                n.hideturtle()
                n.penup()
                n.goto(lst2[block])
    turtle.done()

def load_fifteen(puzzle_state):
    '''
    Function: takes in the state of the puzzle and
        uses coordinates to create a gameboard

    Returns a puzzle in its playable and solved state
    '''

    # keep track of player moves
    
    global clicks
    clicks = 0
    click_tracker()

    # add fifteen images

    try:
        win.addshape('Images/fifteen/16.gif')
        win.addshape('Images/fifteen/15.gif')
        win.addshape('Images/fifteen/14.gif')
        win.addshape('Images/fifteen/13.gif')
        win.addshape('Images/fifteen/12.gif')
        win.addshape('Images/fifteen/11.gif')
        win.addshape('Images/fifteen/10.gif')
        win.addshape('Images/fifteen/9.gif')
        win.addshape('Images/fifteen/8.gif')
        win.addshape('Images/fifteen/7.gif')
        win.addshape('Images/fifteen/6.gif')
        win.addshape('Images/fifteen/5.gif')
        win.addshape('Images/fifteen/4.gif')
        win.addshape('Images/fifteen/3.gif')
        win.addshape('Images/fifteen/2.gif')
        win.addshape('Images/fifteen/blank.gif')
        win.addshape('Images/fifteen/fifteen_thumbnail.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Fifteen image not found') # if image missing

    # create thumbnail

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/fifteen/fifteen_thumbnail.gif')

    # create list of coordinates

    lst = [(-250, 150), (-150, 150), (-50, 150), (50, 150),
               (-250, 50), (-150, 50), (-50, 50), (50, 50),
               (-250, -50), (-150, -50), (-50, -50), (50, -50),
               (-250, -150), (-150, -150), (-50, -150), (50, -150),]

    # load solved puzzle for reset

    if puzzle_state == 'original':
        for block in range(len(lst)): # take in list 
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to coordinates in order
                t.showturtle()
                t.shape('Images/fifteen/16.gif') # define turtle as image
                t.onclick(swap_tile) # provide click function 
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/fifteen/15.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/fifteen/14.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/fifteen/13.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/fifteen/12.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/fifteen/11.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/fifteen/10.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/fifteen/9.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                h.hideturtle()
                h.penup()
                h.goto(lst[block])
                h.showturtle()
                h.shape('Images/fifteen/8.gif')
                h.onclick(swap_tile_h)
            elif block == 9:
                i.hideturtle()
                i.penup()
                i.goto(lst[block])
                i.showturtle()
                i.shape('Images/fifteen/7.gif')
                i.onclick(swap_tile_i)
            elif block == 10:
                j.hideturtle()
                j.penup()
                j.goto(lst[block])
                j.showturtle()
                j.shape('Images/fifteen/6.gif')
                j.onclick(swap_tile_j)
            elif block == 11:
                k.hideturtle()
                k.penup()
                k.goto(lst[block])
                k.showturtle()
                k.shape('Images/fifteen/5.gif')
                k.onclick(swap_tile_k)
            elif block == 12:
                l.hideturtle()
                l.penup()
                l.goto(lst[block])
                l.showturtle()
                l.shape('Images/fifteen/4.gif')
                l.onclick(swap_tile_l)
            elif block == 13:
                m.hideturtle()
                m.penup()
                m.goto(lst[block])
                m.showturtle()
                m.shape('Images/fifteen/3.gif')
                m.onclick(swap_tile_m)
            elif block == 14:
                n.hideturtle()
                n.penup()
                n.goto(lst[block])
                n.showturtle()
                n.shape('Images/fifteen/2.gif')
                n.onclick(swap_tile_n)
            elif block == 15:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/fifteen/blank.gif')

    # load unsolved puzzle 

    if puzzle_state == 'play':
        random.shuffle(lst) # randomize list of coordinates
        for block in range(len(lst)): # take in randomized list of coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to random coordinate
                t.showturtle()
                t.shape('Images/fifteen/16.gif') # define turtle as an image
                t.onclick(swap_tile) # provide click function 
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/fifteen/15.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/fifteen/14.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/fifteen/13.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/fifteen/12.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/fifteen/11.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/fifteen/10.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/fifteen/9.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                h.hideturtle()
                h.penup()
                h.goto(lst[block])
                h.showturtle()
                h.shape('Images/fifteen/8.gif')
                h.onclick(swap_tile_h)
            elif block == 9:
                i.hideturtle()
                i.penup()
                i.goto(lst[block])
                i.showturtle()
                i.shape('Images/fifteen/7.gif')
                i.onclick(swap_tile_i)
            elif block == 10:
                j.hideturtle()
                j.penup()
                j.goto(lst[block])
                j.showturtle()
                j.shape('Images/fifteen/6.gif')
                j.onclick(swap_tile_j)
            elif block == 11:
                k.hideturtle()
                k.penup()
                k.goto(lst[block])
                k.showturtle()
                k.shape('Images/fifteen/5.gif')
                k.onclick(swap_tile_k)
            elif block == 12:
                l.hideturtle()
                l.penup()
                l.goto(lst[block])
                l.showturtle()
                l.shape('Images/fifteen/4.gif')
                l.onclick(swap_tile_l)
            elif block == 13:
                m.hideturtle()
                m.penup()
                m.goto(lst[block])
                m.showturtle()
                m.shape('Images/fifteen/3.gif')
                m.onclick(swap_tile_m)
            elif block == 14:
                n.hideturtle()
                n.penup()
                n.goto(lst[block])
                n.showturtle()
                n.shape('Images/fifteen/2.gif')
                n.onclick(swap_tile_n)
            elif block == 15:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/fifteen/blank.gif')
    turtle.done

def load_smiley(puzzle_state):
    '''
    Function: takes in the state of the puzzle and
        uses coordinates to create a gameboard

    Returns a puzzle in its playable and solved state
    '''

    # track player moves 
    global clicks
    clicks = 0
    click_tracker()

    # add smiley images

    try:
        win.addshape('Images/smiley/16.gif')
        win.addshape('Images/smiley/15.gif')
        win.addshape('Images/smiley/14.gif')
        win.addshape('Images/smiley/13.gif')
        win.addshape('Images/smiley/12.gif')
        win.addshape('Images/smiley/11.gif')
        win.addshape('Images/smiley/10.gif')
        win.addshape('Images/smiley/9.gif')
        win.addshape('Images/smiley/8.gif')
        win.addshape('Images/smiley/7.gif')
        win.addshape('Images/smiley/6.gif')
        win.addshape('Images/smiley/5.gif')
        win.addshape('Images/smiley/4.gif')
        win.addshape('Images/smiley/3.gif')
        win.addshape('Images/smiley/2.gif')
        win.addshape('Images/smiley/blank.gif')
        win.addshape('Images/smiley/smiley_thumbnail.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Smiley image not found') # if image missing
            
    # create thumbnail 

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/smiley/smiley_thumbnail.gif')

    # create list of coordinates

    lst = [(-250, 150), (-150, 150), (-50, 150), (50, 150),
               (-250, 50), (-150, 50), (-50, 50), (50, 50),
               (-250, -50), (-150, -50), (-50, -50), (50, -50),
               (-250, -150), (-150, -150), (-50, -150), (50, -150),]

    # load solved puzzle for reset

    if puzzle_state == 'original':
        for block in range(len(lst)): # take in list of coordinates
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to set coordinate
                t.showturtle()
                t.shape('Images/smiley/16.gif') # define turtle as image
                t.onclick(swap_tile) # provide swap function 
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/smiley/15.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/smiley/14.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/smiley/13.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/smiley/12.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/smiley/11.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/smiley/10.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/smiley/9.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                h.hideturtle()
                h.penup()
                h.goto(lst[block])
                h.showturtle()
                h.shape('Images/smiley/8.gif')
                h.onclick(swap_tile_h)
            elif block == 9:
                i.hideturtle()
                i.penup()
                i.goto(lst[block])
                i.showturtle()
                i.shape('Images/smiley/7.gif')
                i.onclick(swap_tile_i)
            elif block == 10:
                j.hideturtle()
                j.penup()
                j.goto(lst[block])
                j.showturtle()
                j.shape('Images/smiley/6.gif')
                j.onclick(swap_tile_j)
            elif block == 11:
                k.hideturtle()
                k.penup()
                k.goto(lst[block])
                k.showturtle()
                k.shape('Images/smiley/5.gif')
                k.onclick(swap_tile_k)
            elif block == 12:
                l.hideturtle()
                l.penup()
                l.goto(lst[block])
                l.showturtle()
                l.shape('Images/smiley/4.gif')
                l.onclick(swap_tile_l)
            elif block == 13:
                m.hideturtle()
                m.penup()
                m.goto(lst[block])
                m.showturtle()
                m.shape('Images/smiley/3.gif')
                m.onclick(swap_tile_m)
            elif block == 14:
                n.hideturtle()
                n.penup()
                n.goto(lst[block])
                n.showturtle()
                n.shape('Images/smiley/2.gif')
                n.onclick(swap_tile_n)
            elif block == 15:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/smiley/blank.gif')

    # load unsolved puzzle 

    if puzzle_state == 'play':
        random.shuffle(lst) # randomize list of coordinates
        for block in range(len(lst)): # take in randomized list 
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block]) # send turtle to random cooridinate
                t.showturtle()
                t.shape('Images/smiley/16.gif') # define turtle as image 
                t.onclick(swap_tile) # provide click function 
            elif block == 1: # continue for rest of tiles
                a.hideturtle()
                a.penup()
                a.goto(lst[block])
                a.showturtle()
                a.shape('Images/smiley/15.gif')
                a.onclick(swap_tile_a)
            elif block == 2:
                b.hideturtle()
                b.penup()
                b.goto(lst[block])
                b.showturtle()
                b.shape('Images/smiley/14.gif')
                b.onclick(swap_tile_b)
            elif block == 3:
                c.hideturtle()
                c.penup()
                c.goto(lst[block])
                c.showturtle()
                c.shape('Images/smiley/13.gif')
                c.onclick(swap_tile_c)
            elif block == 4:
                d.hideturtle()
                d.penup()
                d.goto(lst[block])
                d.showturtle()
                d.shape('Images/smiley/12.gif')
                d.onclick(swap_tile_d)
            elif block == 5:
                e.hideturtle()
                e.penup()
                e.goto(lst[block])
                e.showturtle()
                e.shape('Images/smiley/11.gif')
                e.onclick(swap_tile_e)
            elif block == 6:
                f.hideturtle()
                f.penup()
                f.goto(lst[block])
                f.showturtle()
                f.shape('Images/smiley/10.gif')
                f.onclick(swap_tile_f)
            elif block == 7:
                g.hideturtle()
                g.penup()
                g.goto(lst[block])
                g.showturtle()
                g.shape('Images/smiley/9.gif')
                g.onclick(swap_tile_g)
            elif block == 8:
                h.hideturtle()
                h.penup()
                h.goto(lst[block])
                h.showturtle()
                h.shape('Images/smiley/8.gif')
                h.onclick(swap_tile_h)
            elif block == 9:
                i.hideturtle()
                i.penup()
                i.goto(lst[block])
                i.showturtle()
                i.shape('Images/smiley/7.gif')
                i.onclick(swap_tile_i)
            elif block == 10:
                j.hideturtle()
                j.penup()
                j.goto(lst[block])
                j.showturtle()
                j.shape('Images/smiley/6.gif')
                j.onclick(swap_tile_j)
            elif block == 11:
                k.hideturtle()
                k.penup()
                k.goto(lst[block])
                k.showturtle()
                k.shape('Images/smiley/5.gif')
                k.onclick(swap_tile_k)
            elif block == 12:
                l.hideturtle()
                l.penup()
                l.goto(lst[block])
                l.showturtle()
                l.shape('Images/smiley/4.gif')
                l.onclick(swap_tile_l)
            elif block == 13:
                m.hideturtle()
                m.penup()
                m.goto(lst[block])
                m.showturtle()
                m.shape('Images/smiley/3.gif')
                m.onclick(swap_tile_m)
            elif block == 14:
                n.hideturtle()
                n.penup()
                n.goto(lst[block])
                n.showturtle()
                n.shape('Images/smiley/2.gif')
                n.onclick(swap_tile_n)
            elif block == 15:
                o.hideturtle()
                o.penup()
                o.goto(lst[block])
                o.showturtle()
                o.shape('Images/smiley/blank.gif')
    turtle.done()

def swap_tile(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # take player clicks

    # get turtle position 
    
    t_point = t.pos()
    o_point = o.pos()

    # move turtle with respect to position of blank tile

    if t_point == o.pos() + (100, 0): # track turtles to the right blank
        o.goto(t_point) # move turtle
        t.goto(o_point)
        clicks += 1 # update click tracker 
    elif t_point == o.pos() - (100, 0): # track to the left of blank 
        o.goto(t_point)
        t.goto(o_point)
        clicks += 1
    elif t_point == o.pos() + (0, 100): # track above blank 
        o.goto(t_point)
        t.goto(o_point)
        clicks += 1
    elif t_point == o.pos() - (0, 100): # track below blank 
        o.goto(t_point)
        t.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker display onscreen 
    win_tracker() # check if game was won

def swap_tile_a(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # take player clicks 

    # get turtle position 
    
    o_point = o.pos()
    a_point = a.pos()

    # move turtles with respect to blank tiles

    if a_point == o.pos() + (100, 0): # track turtle to the right of blank 
        o.goto(a_point) # move turtles 
        a.goto(o_point)
        clicks += 1 # update for click tracker 
    elif a_point == o.pos() - (100, 0): # track turtle to the left of blank 
        o.goto(a_point)
        a.goto(o_point)
        clicks += 1
    elif a_point == o.pos() + (0, 100): # track turtle above blank  
        o.goto(a_point)
        a.goto(o_point)
        clicks += 1
    elif a_point == o.pos() - (0, 100): # track turtle below blank  
        o.goto(a_point)
        a.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update tracker onscreen 
    win_tracker() # check if game was won 

def swap_tile_b(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # take player clicks

    # get turtle position 
    
    o_point = o.pos()
    b_point = b.pos()

    # track turtle with respect for blank 

    if b_point == o.pos() + (100, 0): # above blank tile 
        o.goto(b_point) # move turtles 
        b.goto(o_point)
        clicks += 1 # update clicks for tracker 
    elif b_point == o.pos() - (100, 0): # below blank 
        o.goto(b_point)
        b.goto(o_point)
        clicks += 1
    elif b_point == o.pos() + (0, 100): # to the right of blank 
        o.goto(b_point)
        b.goto(o_point)
        clicks += 1
    elif b_point == o.pos() - (0, 100): # to the left of blank 
        o.goto(b_point)
        b.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker onscreen
    win_tracker() # check if game was won

def swap_tile_c(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get turtle position
    
    c_point = c.pos()
    o_point = o.pos()

    # move turtle with respect to position of blank 

    if c_point == o.pos() + (100, 0): # track to the right of blank
        o.goto(c_point) # swap turtles 
        c.goto(o_point)
        clicks += 1 # update click tracker 
    elif c_point == o.pos() - (100, 0): # track the left of blank 
        o.goto(c_point)
        c.goto(o_point)
        clicks += 1
    elif c_point == o.pos() + (0, 100): # track the right of blank 
        o.goto(c_point)
        c.goto(o_point)
        clicks += 1
    elif c_point == o.pos() - (0, 100): # track the left of blank 
        o.goto(c_point)
        c.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker onscreen 
    win_tracker() # check if game won 

def swap_tile_d(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    o_point = o.pos()
    d_point = d.pos()

    # move turtles with respect to position 

    if d_point == o.pos() + (100, 0): # move turtle to the right 
        o.goto(d_point) 
        d.goto(o_point)
        clicks += 1
    elif d_point == o.pos() - (100, 0): # move turtle to the left 
        o.goto(d_point)
        d.goto(o_point)
        clicks += 1
    elif d_point == o.pos() + (0, 100): # move turtle above 
        o.goto(d_point)
        d.goto(o_point)
        clicks += 1
    elif d_point == o.pos() - (0, 100): # move turtle below 
        o.goto(d_point)
        d.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won 

def swap_tile_e(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get postion 
    
    o_point = o.pos()
    e_point = e.pos()

    # move turtles with respect to blank 

    if e_point == o.pos() + (100, 0): # move turtle to the right 
        o.goto(e_point)
        e.goto(o_point)
        clicks += 1
    elif e_point == o.pos() - (100, 0): # move turtle to the left 
        o.goto(e_point)
        e.goto(o_point)
        clicks += 1
    elif e_point == o.pos() + (0, 100): # move turtle above 
        o.goto(e_point)
        e.goto(o_point)
        clicks += 1
    elif e_point == o.pos() - (0, 100): # move turtle below 
        o.goto(e_point)
        e.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker
    win_tracker() # check if game was won

def swap_tile_f(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    f_point = f.pos()
    o_point = o.pos()

    # move with respect to blank tile

    if f_point == o.pos() + (100, 0): # move tile to the right of blank 
        o.goto(f_point)
        f.goto(o_point)
        clicks += 1
    elif f_point == o.pos() - (100, 0): # move tile to the left 
        o.goto(f_point)
        f.goto(o_point)
        clicks += 1
    elif f_point == o.pos() + (0, 100): # move tile above 
        o.goto(f_point)
        f.goto(o_point)
        clicks += 1
    elif f_point == o.pos() - (0, 100): # move tile below 
        o.goto(f_point)
        f.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won  

def swap_tile_g(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position
    
    o_point = o.pos()
    g_point = g.pos()

    # track position with respect to blank 

    if g_point == o.pos() + (100, 0): # track to the right 
        o.goto(g_point)
        g.goto(o_point)
        clicks += 1
    elif g_point == o.pos() - (100, 0): # track to the left 
        o.goto(g_point)
        g.goto(o_point)
        clicks += 1
    elif g_point == o.pos() + (0, 100): # track above 
        o.goto(g_point)
        g.goto(o_point)
        clicks += 1
    elif g_point == o.pos() - (0, 100): # track below 
        o.goto(g_point)
        g.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update clic tracker 
    win_tracker() # check if game won 

def swap_tile_h(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    o_point = o.pos()
    h_point = h.pos()

    # track with respect to blank 

    if h_point == o.pos() + (100, 0): # track the right 
        o.goto(h_point)
        h.goto(o_point)
        clicks += 1
    elif h_point == o.pos() - (100, 0): # track the left 
        o.goto(h_point)
        h.goto(o_point)
        clicks += 1
    elif h_point == o.pos() + (0, 100): # track above 
        o.goto(h_point)
        h.goto(o_point)
        clicks += 1
    elif h_point == o.pos() - (0, 100): # track below 
        o.goto(h_point)
        h.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won 

def swap_tile_i(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    i_point = i.pos()
    o_point = o.pos()

    # track position with repect to blank 

    if i_point == o.pos() + (100, 0): # track right 
        o.goto(i_point)
        i.goto(o_point)
        clicks += 1
    elif i_point == o.pos() - (100, 0): # track left 
        o.goto(i_point)
        i.goto(o_point)
        clicks += 1
    elif i_point == o.pos() + (0, 100): # track above 
        o.goto(i_point)
        i.goto(o_point)
        clicks += 1
    elif i_point == o.pos() - (0, 100): # track below 
        o.goto(i_point)
        i.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update tracker 
    win_tracker() # check if game won 

def swap_tile_j(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    o_point = o.pos()
    j_point = j.pos()

    # track and swap turtles with repect to blank tile 

    if j_point == o.pos() + (100, 0):
        o.goto(j_point)
        j.goto(o_point)
        clicks += 1
    elif j_point == o.pos() - (100, 0):
        o.goto(j_point)
        j.goto(o_point)
        clicks += 1
    elif j_point == o.pos() + (0, 100):
        o.goto(j_point)
        j.goto(o_point)
        clicks += 1
    elif j_point == o.pos() - (0, 100):
        o.goto(j_point)
        j.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won 

def swap_tile_k(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    o_point = o.pos()
    k_point = k.pos()

    # track and swap turtles with respect to blank tile 

    if k_point == o.pos() + (100, 0):
        o.goto(k_point)
        k.goto(o_point)
        clicks += 1
    elif k_point == o.pos() - (100, 0):
        o.goto(k_point)
        k.goto(o_point)
        clicks += 1
    elif k_point == o.pos() + (0, 100):
        o.goto(k_point)
        k.goto(o_point)
        clicks += 1
    elif k_point == o.pos() - (0, 100):
        o.goto(k_point)
        k.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won 

def swap_tile_l(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    l_point = l.pos()
    o_point = o.pos()

    # track and swap turtles with respect to blank

    if l_point == o.pos() + (100, 0):
        o.goto(l_point)
        l.goto(o_point)
        clicks += 1
    elif l_point == o.pos() - (100, 0):
        o.goto(l_point)
        l.goto(o_point)
        clicks += 1
    elif l_point == o.pos() + (0, 100):
        o.goto(l_point)
        l.goto(o_point)
        clicks += 1
    elif l_point == o.pos() - (0, 100):
        o.goto(l_point)
        l.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won 

def swap_tile_m(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position
    
    o_point = o.pos()
    m_point = m.pos()

    # swap and track turtles with respect to blank tiles 

    if m_point == o.pos() + (100, 0):
        o.goto(m_point)
        m.goto(o_point)
        clicks += 1
    elif m_point == o.pos() - (100, 0):
        o.goto(m_point)
        m.goto(o_point)
        clicks += 1
    elif m_point == o.pos() + (0, 100):
        o.goto(m_point)
        m.goto(o_point)
        clicks += 1
    elif m_point == o.pos() - (0, 100):
        o.goto(m_point)
        m.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won 

def swap_tile_n(x, y):
    '''
    Function: Takes in coordinates from player clicks
        moves turtles accordingly with respect to position of blank tile

    Swaps game tiles to provide playability
    '''
    
    global clicks # get clicks

    # get position 
    
    o_point = o.pos()
    n_point = n.pos()

    # track and swap turtles with respect to blank tile 

    if n_point == o.pos() + (100, 0):
        o.goto(n_point)
        n.goto(o_point)
        clicks += 1
    elif n_point == o.pos() - (100, 0):
        o.goto(n_point)
        n.goto(o_point)
        clicks += 1
    elif n_point == o.pos() + (0, 100):
        o.goto(n_point)
        n.goto(o_point)
        clicks += 1
    elif n_point == o.pos() - (0, 100):
        o.goto(n_point)
        n.goto(o_point)
        clicks += 1
    else:
        pass

    click_tracker() # update click tracker 
    win_tracker() # check if game won

def click_tracker():
    '''
    Function: takes in clicks from all swap_tile functions when legal moves are made 

    Displays number of clicks onscreen in real time
        game ends if number of clicks equals total player moves 
    '''
    
    global clicks # get clicks

    # display tracker

    clear_tracker() # erase previous tracker number
    q.hideturtle()
    q.penup()
    q.goto(-120, -311) # move tracker in front of player moves heading 
    q.write(clicks, font = ('Ariel',
                            17, 'normal')) # write number of clicks

    # end game in losing scenario

    try:
        win.addshape('Resources/credits.gif')
        win.addshape('Resources/Lose.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Resource image not found') # if image missing

    if moves == clicks: # see if player moves is equal to player clicks 
        r = turtle.Turtle() # define new turtle
        u = turtle.Turtle()
        r.shape('Resources/Lose.gif') # show loss icon
        time.sleep(3) # display for 5 seconds 
        r.hideturtle() # remove loss icon
        u.shape('Resources/credits.gif') # show credits
        time.sleep(3)
        u.hideturtle()
    
    return clicks 

def win_tracker():
    '''
    Function: takes in coordinates of all turtle position then
        matches them to the winning coordinates of all turtles

    Game is won if turtle positions are all correctly
        allocated on the game board 
    '''

    # create winning scenario for yoshi puzzle
    
    yoshi_orig = [(-250.00, 150.00), (-250.00, 50.00),
                  (-150.00, 150.00), (-150.00, 50.00)]

    # track coordinates of turtles used in the yoshi puzzle

    yoshi_lst = [t.pos(), a.pos(), b.pos(), o.pos()]

    # create winning scenario for the smiley, mario, and fifteen puzzles

    smiley_mario_15_orig = [(-250.00, 150.00), (-150.00, 150.00),
                            (-50.00, 150.00), (50.00, 150.00),
                            (-250.00, 50.00), (-150.00, 50.00),
                            (-50.00, 50.00), (50.00, 50.00),
                            (-250.00, -50.00), (-150.00, -50.00),
                            (-50.00, -50.00), (50.00, -50.00),
                            (-250.00, -150.00), (-150.00, -150.00),
                            (-50.00, -150.00), (50.00, -150.00)]

    # track coordinates used in the smiley, mario, and fifteen puzzles 
    
    smiley_mario_15_lst = [t.pos(), a.pos(), b.pos(), c.pos(), d.pos(),
                           e.pos(), f.pos(), g.pos(), h.pos(), i.pos(),
                           j.pos(), k.pos(), l.pos(), m.pos(), n.pos(),
                           o.pos()]

    # create winning scenario of luigi puzzle 

    luigi_orig = [(-250.00, 150.00), (-150.00, 150.00), (-50.00, 150.00),
                  (-250.00, 50.00), (-150.00, 50.00), (-50.00, 50.00),
                  (-250.00, -50.00), (-150.00, -50.00), (-50.00, -50.00)]

    # track coordinates of turtles used in luigi puzzle 

    luigi_lst = [t.pos(), a.pos(), b.pos(),
                 c.pos(), d.pos(), e.pos(),
                 f.pos(), g.pos(), o.pos()]
    try:
        win.addshape('Resources/winner.gif')
        win.addshape('Resources/credits.gif')
    except FileNotFoundError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('Resource image not found') # if image missing

    s = turtle.Turtle() # define new turtles 
    u = turtle.Turtle()

    if yoshi_orig == yoshi_lst: # check if both lists of coordinates are equal
        s.shape('Resources/winner.gif') # show win screen 
        time.sleep(3) # show win screen for 3 seconds
        s.hideturtle
        u.shape('Resources/credits.gif') # roll credits
        time.sleep(3)
        u.hideturtle()

    # display to leaderboard

    global player # get player

    if yoshi_orig == yoshi_lst:
        with open('leader_data.txt', 'a') as fd: # open text file 
            fd.write(str(clicks) + '  -- ' + player + '\n') # append name

    # check if both lists of coordinates are equal 

    if smiley_mario_15_orig == smiley_mario_15_lst:
        s.shape('Resources/winner.gif') # display win screen 
        time.sleep(3)
        s.hideturtle() # hide after 3 seconds
        u.shape('Resources/credits.gif') # roll credits
        time.sleep(3)
        u.hideturtle()

    # display to leaderboard

    if smiley_mario_15_orig == smiley_mario_15_lst:
        with open('leader_data.txt', 'a') as fd: # open text file 
            fd.write(str(clicks) + '  -- ' + player + '\n') # append name

    if luigi_orig == luigi_lst: # check if both lists of coordinates are equal
        s.shape('Resources/winner.gif') # show win screen 
        time.sleep(3) 
        s.hideturtle() # hide after 3 seconds
        u.shape('Resources/credits.gif') # roll credits
        time.sleep(3)
        u.hideturtle()

    # display to leaderboard

    if luigi_orig == luigi_lst:
        with open('leader_data.txt', 'a') as fd: # open text file 
            fd.write(str(clicks) + '  -- ' + player + '\n') # append name

def dialog_box():
    '''
    Function: takes in the name of player and number of moves per game
        via pop up text boxes

    '''
    
    global moves # get moves
    global player # get player

    # create text box for player name 
    try:
        player = turtle.textinput("Puzzle Slider",
                                "Enter your name: ")
    except TypeError:
        with open('5001_puzzle.err', 'a') as infile:
            infile.write('No name given')

    moves = turtle.numinput("Puzzle Slider - Moves",
                    "Enter number of moves (5 - 200): ",
                    minval=5,
                    maxval=200) # create text box for player moves

    moves = int(moves) # convert moves to integer value

def clear_tracker():
    '''
    Function: Erases the player moves number

    Resets the screen such that a new number can be
        displayed after every click
    '''
    
    q.clear()
    
def get_yoshi_play():
    '''
    Function: loads yoshi puzzle in its play state
    '''
    
    load_yoshi('play')

def get_yoshi_original(x, y):
    '''
    Function: loads yoshi in its solved state
    '''
    
    load_yoshi('original')

def get_mario_play():
    '''
    Function: loads unsolved mario puzzle
    '''
    
    load_mario('play')

def get_mario_original(x, y):
    '''
    Function: loads solved mario puzzle
    '''
    
    load_mario('original')

def get_luigi_play():
    '''
    Function: loads unsolved luigi puzzle
    '''
    
    load_luigi('play')

def get_luigi_original(x, y):
    '''
    Function: loads solved luigi puzzle
    '''
    
    load_luigi('original')

def get_fifteen_play():
    '''
    Function: loads unsolved fifteen puzzle
    '''
    
    load_fifteen('play')

def get_fifteen_original(x, y):
    '''
    Function: loads solved fifteen puzzle
    '''
    
    load_fifteen('original')

def get_smiley_play():
    '''
    Function: loads unsolved smiley puzzle
    '''
    
    load_smiley('play')

def get_smiley_original(x, y):
    '''
    Function: loads solved smiley puzzle
    '''
    
    load_smiley('original')
    
