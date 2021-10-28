#
#   hcurve.py -> L9-4
#

import turtle

def drawH(t, d, len):

    if d==0:
       return

    t.right(90)
    t.forward(len/2)
    t.left(90)
    t.forward(len/2)

    drawH(t,d-1,len/2)

    t.backward(len)

    drawH(t,d-1,len/2)

    t.forward(len/2)
    t.left(90)
    t.forward(len)
    t.right(90)
    t.forward(len/2)

    drawH(t,d-1,len/2)

    t.backward(len)

    drawH(t,d-1,len/2)

    t.forward(len/2)
    t.right(90)
    t.forward(len/2)
    t.left(90)


def main():

    t = turtle.Turtle()
    wn = turtle.Screen()

    d = int(input('enter depth d: '))
    len = float(input('enter H side length: '))

    # finish the above function

    t.speed(0) # go fast!

    t.left(90)
    drawH(t,d,len)

    wn.exitonclick()

main()
