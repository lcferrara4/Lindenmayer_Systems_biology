# L-system for Sierpinski triangle in text

def sierpinski_a_text(n):
    if n == 0:
        print('A', end="")
    else:
        print('+', end="")
        sierpinski_b_text(n-1)
        print('-', end="")
        sierpinski_a_text(n-1)
        print('-', end="")
        sierpinski_b_text(n-1)
        print('+', end="")
    
def sierpinski_b_text(n):
    if n == 0:
        print('B', end="")
    else:
        print('-', end="")
        sierpinski_a_text(n-1)
        print('+', end="")
        sierpinski_b_text(n-1)
        print('+', end="")
        sierpinski_a_text(n-1)
        print('-', end="")

iterations = 4 # how many rounds of substitutions to make
for i in range(iterations): 
    print('n =', i, end=" ")
    sierpinski_a_text(i) # enters axiom state
    print('')
