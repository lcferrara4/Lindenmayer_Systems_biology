# L-system for fractal plant using turtle graphics

import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.goto(-250, -250)
t.pendown()

def plant_X(t, n, size):
    if n != 0:
        plant_F(t, n-1, size)                            # F
        
        t.left(25)                                       # -
        
        stack.append([t.xcor(), t.ycor(), t.heading()])  # [
        stack.append([t.xcor(), t.ycor(), t.heading()])  # [
        
        plant_X(t, n-1, size)                            # X
        
        pos_list = stack.pop()                           # ]
        t.penup()
        t.goto(pos_list[0], pos_list[1])
        t.pendown()
        t.setheading(pos_list[2])
        
        t.right(25)                                      # +
        
        plant_X(t, n-1, size)                            # X
        
        pos_list = stack.pop()                           # ]
        t.penup()
        t.goto(pos_list[0], pos_list[1])
        t.pendown()
        t.setheading(pos_list[2])
        
        t.right(25)                                      # +
        
        plant_F(t, n-1, size)                            # F
        
        stack.append([t.xcor(), t.ycor(), t.heading()])  # [
 
        t.right(25)                                      # +

        plant_F(t, n-1, size)                            # F
        plant_X(t, n-1, size)                            # X
        
        pos_list = stack.pop()                           # ]
        t.penup()
        t.goto(pos_list[0], pos_list[1])
        t.pendown()
        t.setheading(pos_list[2])
        
        t.left(25)                                       # -

        plant_X(t, n-1, size)                            # X
    
def plant_F(t, n, size):
    if n == 0:
        t.forward(size)
    else:
        plant_F(t, n-1, size)                            # F
        plant_F(t, n-1, size)                            # F

stack =[] # stack for storing positions [x, y, angle]

size = 20      # how long for turtle.forward() command
iterations = 4 # how many rounds of substitutions to make

t.pencolor("green") # change color to green for plant
t.setheading(60)    # initial angle to 60 degrees
plant_X(t, iterations, size)    # enters axiom state
wn.exitonclick()


