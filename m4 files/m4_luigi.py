'''
    Project
    Milestone 4
    Game Behavior: Luigi
'''

import m1_prework
import m2_gameboard
import random
import turtle
import m4_yoshi
import m4_mario
win = turtle.Screen()
win.setup(width = 800, height = 600)

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

def load_luigi(puzzle_state):
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

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/luigi/luigi_thumbnail.gif')

    lst = [(-250, 150), (-150, 150), (-50, 150),
               (-250, 50), (-150, 50), (-50, 50),
               (-250, -50), (-150, -50), (-50, -50)]

    if puzzle_state == 'original':
        for block in range(len(lst)):
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block])
                t.showturtle()
                t.shape('Images/luigi/9.gif')
                t.onclick(swap_tile)
            elif block == 1:
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

    if puzzle_state == 'play':
        random.shuffle(lst)
        for block in range(len(lst)):
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block])
                t.showturtle()
                t.shape('Images/luigi/9.gif')
                t.onclick(swap_tile)
            elif block == 1:
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

def swap_tile_d(x, y):
    o_point = o.pos()
    d_point = d.pos()

    if d_point == o.pos() + (100, 0):
        o.goto(d_point)
        d.goto(o_point)
    elif d_point == o.pos() - (100, 0):
        o.goto(d_point)
        d.goto(o_point)
    elif d_point == o.pos() + (0, 100):
        o.goto(d_point)
        d.goto(o_point)
    elif d_point == o.pos() - (0, 100):
        o.goto(d_point)
        d.goto(o_point)
    else:
        pass

def swap_tile_e(x, y):
    o_point = o.pos()
    e_point = e.pos()

    if e_point == o.pos() + (100, 0):
        o.goto(e_point)
        e.goto(o_point)
    elif e_point == o.pos() - (100, 0):
        o.goto(e_point)
        e.goto(o_point)
    elif e_point == o.pos() + (0, 100):
        o.goto(e_point)
        e.goto(o_point)
    elif e_point == o.pos() - (0, 100):
        o.goto(e_point)
        e.goto(o_point)
    else:
        pass

def swap_tile_f(x, y):
    f_point = f.pos()
    o_point = o.pos()

    if f_point == o.pos() + (100, 0):
        o.goto(f_point)
        f.goto(o_point)
    elif f_point == o.pos() - (100, 0):
        o.goto(f_point)
        f.goto(o_point)
    elif f_point == o.pos() + (0, 100):
        o.goto(f_point)
        f.goto(o_point)
    elif f_point == o.pos() - (0, 100):
        o.goto(f_point)
        f.goto(o_point)
    else:
        pass

def swap_tile_g(x, y):
    o_point = o.pos()
    g_point = g.pos()

    if g_point == o.pos() + (100, 0):
        o.goto(g_point)
        g.goto(o_point)
    elif g_point == o.pos() - (100, 0):
        o.goto(g_point)
        g.goto(o_point)
    elif g_point == o.pos() + (0, 100):
        o.goto(g_point)
        g.goto(o_point)
    elif g_point == o.pos() - (0, 100):
        o.goto(g_point)
        g.goto(o_point)
    else:
        pass
