# L-system for Pythagoras tree using turtle graphics

import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.goto(0, -250)
t.pendown()

def py_tree_0(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        py_tree_1(t, n-1, size)                          #1
        
        stack.append([t.xcor(), t.ycor(), t.heading()])  #[ 
        t.left(45)                                       
        
        py_tree_0(t, n-1, size)                          #0
        
        pos_list = stack.pop()                           #]
        t.penup()
        t.goto(pos_list[0], pos_list[1])
        t.pendown()
        t.setheading(pos_list[2])
        t.right(45)
        
        py_tree_0(t, n-1, size)                          #0
    
def py_tree_1(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        py_tree_1(t, n-1, size)                           #1
        py_tree_1(t, n-1, size)                           #1

stack =[] # stack for storing positions [x, y, angle]


size = 5      # how long for turtle.forward() command
iterations = 6 # how many rounds of substitutions to make

t.left(90)         # start with turtle facing up
py_tree_0(t, iterations, size) # enters axiom state
wn.exitonclick()