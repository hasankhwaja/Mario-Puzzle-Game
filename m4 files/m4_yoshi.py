'''
    Project
    Mileston 4
    Game behavior: Yoshi
'''

import m1_prework
import m2_gameboard
import random
import turtle
win = turtle.Screen()
win.setup(width = 800, height = 600)

t = turtle.Turtle()
a = turtle.Turtle()
b = turtle.Turtle()
o = turtle.Turtle()

def load_yoshi(puzzle_state):
    win.addshape('Images/yoshi/4.gif')
    win.addshape('Images/yoshi/3.gif')
    win.addshape('Images/yoshi/2.gif')
    win.addshape('Images/yoshi/blank.gif')
    win.addshape('Images/yoshi/yoshi_thumbnail.gif')

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/yoshi/yoshi_thumbnail.gif')
    
    lst = [(-250, 150), (-250, 50), (-150, 150), (-150, 50)] 

    if puzzle_state == 'original':
        for block in range(len(lst)):
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block])
                t.showturtle()
                t.shape('Images/yoshi/4.gif')
                t.onclick(swap_tile)
            elif block == 1:
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
    
    if puzzle_state == 'play':
        random.shuffle(lst)
        for block in range(len(lst)):
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block])
                t.showturtle()
                t.shape('Images/yoshi/4.gif')
                t.onclick(swap_tile)
            elif block == 1:
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
    turtle.done()

def swap_tile(x, y):
    t_point = t.pos()
    o_point = o.pos()

    if t_point == o.pos() + (100, 0):
        o.goto(t_point)
        t.goto(o_point)
    elif t_point == o.pos() - (100, 0):
        o.goto(t_point)
        t.goto(o_point)
    elif t_point == o.pos() + (0, 100):
        o.goto(t_point)
        t.goto(o_point)
    elif t_point == o.pos() - (0, 100):
        o.goto(t_point)
        t.goto(o_point)
    else:
        pass

def swap_tile_a(x, y):
    o_point = o.pos()
    a_point = a.pos()

    if a_point == o.pos() + (100, 0):
        o.goto(a_point)
        a.goto(o_point)
    elif a_point == o.pos() - (100, 0):
        o.goto(a_point)
        a.goto(o_point)
    elif a_point == o.pos() + (0, 100):
        o.goto(a_point)
        a.goto(o_point)
    elif a_point == o.pos() - (0, 100):
        o.goto(a_point)
        a.goto(o_point)
    else:
        pass

def swap_tile_b(x, y):
    o_point = o.pos()
    b_point = b.pos()

    if b_point == o.pos() + (100, 0):
        o.goto(b_point)
        b.goto(o_point)
    elif b_point == o.pos() - (100, 0):
        o.goto(b_point)
        b.goto(o_point)
    elif b_point == o.pos() + (0, 100):
        o.goto(b_point)
        b.goto(o_point)
    elif b_point == o.pos() - (0, 100):
        o.goto(b_point)
        b.goto(o_point)
    else:
        pass

def swap_tile_c(x, y):
    c_point = c.pos()
    o_point = o.pos()

    if c_point == o.pos() + (100, 0):
        o.goto(c_point)
        c.goto(o_point)
    elif c_point == o.pos() - (100, 0):
        o.goto(c_point)
        c.goto(o_point)
    elif c_point == o.pos() + (0, 100):
        o.goto(c_point)
        c.goto(o_point)
    elif c_point == o.pos() - (0, 100):
        o.goto(c_point)
        c.goto(o_point)
    else:
        pass
