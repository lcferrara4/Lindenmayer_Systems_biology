# L-system for Koch Curve with 90 degree angles using turtle graphics

import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.goto(-250, -250)
t.pendown()

def koch_curve(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        koch_curve(t, n-1, size)  # F
        t.left(90)                # +
        koch_curve(t, n-1, size)  # F
        t.right(90)               # -
        koch_curve(t, n-1, size)  # F
        t.right(90)               # -
        koch_curve(t, n-1, size)  # F
        t.left(90)                # +
        koch_curve(t, n-1, size)  # F

size = 15      # how long for turtle.forward() command
iterations = 3 # how many rounds of substitutions to make
koch_curve(t, iterations, size) # enters axiom state
wn.exitonclick()
