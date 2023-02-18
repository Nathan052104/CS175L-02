#CS175L
#Nathan Tunnessen
#Turtle.py

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s/math.sqrt(2)
diameter = s + (2 * x)



t = turtle.Turtle()

t.shape('turtle')

t.penup()
t.goto(-50, 100)
t.pendown()
t.color('white', 'red')
t.begin_fill()
for i in range (NUM_SIDES):
    t.forward(LENGTH)
    t.right(ANGLE)

t.end_fill()
t.hideturtle()

t.penup()
t.right(90)
t.forward(140)
t.color('white')
t.write('STOP', font = ('Arial', 30, 'normal'))
                    
