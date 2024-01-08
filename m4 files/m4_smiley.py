'''
    Project
    Milestone 4
    Game Behavior: Smiley
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

def load_smiley(puzzle_state):
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

    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(350, 200)
    p.showturtle()
    p.shape('Images/smiley/smiley_thumbnail.gif')

    lst = [(-250, 150), (-150, 150), (-50, 150), (50, 150),
               (-250, 50), (-150, 50), (-50, 50), (50, 50),
               (-250, -50), (-150, -50), (-50, -50), (50, -50),
               (-250, -150), (-150, -150), (-50, -150), (50, -150),]

    if puzzle_state == 'original':
        for block in range(len(lst)):
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block])
                t.showturtle()
                t.shape('Images/smiley/16.gif')
                t.onclick(swap_tile)
            elif block == 1:
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
                l.onlick(swap_tile_l)
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

    if puzzle_state == 'play':
        random.shuffle(lst)
        for block in range(len(lst)):
            if block == 0:
                t.hideturtle()
                t.penup()
                t.goto(lst[block])
                t.showturtle()
                t.shape('Images/smiley/16.gif')
                t.onclick(swap_tile)
            elif block == 1:
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

def swap_tile_h(x, y):
    o_point = o.pos()
    h_point = h.pos()

    if h_point == o.pos() + (100, 0):
        o.goto(h_point)
        h.goto(o_point)
    elif h_point == o.pos() - (100, 0):
        o.goto(h_point)
        h.goto(o_point)
    elif h_point == o.pos() + (0, 100):
        o.goto(h_point)
        h.goto(o_point)
    elif h_point == o.pos() - (0, 100):
        o.goto(h_point)
        h.goto(o_point)
    else:
        pass

def swap_tile_i(x, y):
    i_point = i.pos()
    o_point = o.pos()

    if i_point == o.pos() + (100, 0):
        o.goto(i_point)
        i.goto(o_point)
    elif i_point == o.pos() - (100, 0):
        o.goto(i_point)
        i.goto(o_point)
    elif i_point == o.pos() + (0, 100):
        o.goto(i_point)
        i.goto(o_point)
    elif i_point == o.pos() - (0, 100):
        o.goto(i_point)
        i.goto(o_point)
    else:
        pass

def swap_tile_j(x, y):
    o_point = o.pos()
    j_point = j.pos()

    if j_point == o.pos() + (100, 0):
        o.goto(j_point)
        j.goto(o_point)
    elif j_point == o.pos() - (100, 0):
        o.goto(j_point)
        j.goto(o_point)
    elif j_point == o.pos() + (0, 100):
        o.goto(j_point)
        j.goto(o_point)
    elif j_point == o.pos() - (0, 100):
        o.goto(j_point)
        j.goto(o_point)
    else:
        pass

def swap_tile_k(x, y):
    o_point = o.pos()
    k_point = k.pos()

    if k_point == o.pos() + (100, 0):
        o.goto(k_point)
        k.goto(o_point)
    elif k_point == o.pos() - (100, 0):
        o.goto(k_point)
        k.goto(o_point)
    elif k_point == o.pos() + (0, 100):
        o.goto(k_point)
        k.goto(o_point)
    elif k_point == o.pos() - (0, 100):
        o.goto(k_point)
        k.goto(o_point)
    else:
        pass

def swap_tile_l(x, y):
    l_point = l.pos()
    o_point = o.pos()

    if l_point == o.pos() + (100, 0):
        o.goto(l_point)
        l.goto(o_point)
    elif l_point == o.pos() - (100, 0):
        o.goto(l_point)
        l.goto(o_point)
    elif l_point == o.pos() + (0, 100):
        o.goto(l_point)
        l.goto(o_point)
    elif l_point == o.pos() - (0, 100):
        o.goto(l_point)
        l.goto(o_point)
    else:
        pass

def swap_tile_m(x, y):
    o_point = o.pos()
    m_point = m.pos()

    if m_point == o.pos() + (100, 0):
        o.goto(m_point)
        m.goto(o_point)
    elif m_point == o.pos() - (100, 0):
        o.goto(m_point)
        m.goto(o_point)
    elif m_point == o.pos() + (0, 100):
        o.goto(m_point)
        m.goto(o_point)
    elif m_point == o.pos() - (0, 100):
        o.goto(m_point)
        m.goto(o_point)
    else:
        pass

def swap_tile_n(x, y):
    o_point = o.pos()
    n_point = n.pos()

    if n_point == o.pos() + (100, 0):
        o.goto(n_point)
        n.goto(o_point)
    elif n_point == o.pos() - (100, 0):
        o.goto(n_point)
        n.goto(o_point)
    elif n_point == o.pos() + (0, 100):
        o.goto(n_point)
        n.goto(o_point)
    elif n_point == o.pos() - (0, 100):
        o.goto(n_point)
        n.goto(o_point)
    else:
        pass
