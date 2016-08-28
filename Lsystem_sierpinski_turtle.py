# L-system for Sierpinski triangle using turtle graphics

import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.goto(-250, -250)
t.pendown()

def sierpinski_a(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        t.left(60)                  # +
        sierpinski_b(t, n-1, size)  # B
        t.right(60)                 # -
        sierpinski_a(t, n-1, size)  # A
        t.right(60)                 # -
        sierpinski_b(t, n-1, size)  # B
        t.left(60)                  # +
    
def sierpinski_b(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        t.right(60)                 # -
        sierpinski_a(t, n-1, size)  # A
        t.left(60)                  # +
        sierpinski_b(t, n-1, size)  # B
        t.left(60)                  # +
        sierpinski_a(t, n-1, size)  # A
        t.right(60)                 # -

size = 10      # how long for turtle.forward() command
iterations = 4 # how many rounds of substitutions to make
sierpinski_a(t, iterations, size) # enters axiom state
wn.exitonclick()
