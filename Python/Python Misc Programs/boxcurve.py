# Shivali Dalmia
# boxcurve.py -> alternate version of L9-4

import turtle
import math

def drawBox(t, d, len):

    if d==0:
        return # nothing to do: "bottomed out"

    t.right(90)
    t.penup()
    t.forward(len/math.sqrt(2))
    t.pendown()
    t.left(90)

    drawBox(t,d-1,len/2)

    t.left(45)
    t.forward(len)
    t.right(45)

    drawBox(t,d-1,len/2)

    t.right(45)
    t.backward(len)
    t.left(45)

    drawBox(t,d-1,len/2)

    t.left(45)
    t.backward(len)
    t.right(45)

    drawBox(t,d-1,len/2)

    t.right(45)
    t.forward(len)
    t.left(135)
    t.penup()
    t.forward(len/math.sqrt(2))
    t.right(90)

    t.pendown()

def main():

    t = turtle.Turtle()
    wn = turtle.Screen()

    d = int(input('enter depth d: '))
    len = float(input('enter box side length: '))


    # finish this main(), along with above function

    t.speed(0)

    t.left(90)
    drawBox(t,d,len)

    wn.exitonclick()

main()
