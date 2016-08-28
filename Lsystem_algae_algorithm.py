# L-system for algae growth using G(n) = G(n-1)G(n-2) concatenation algorithm

def algae(n):
    if n == 0:
        print('A', end="")
    elif n == 1:
        print('AB', end="")
    else:
        algae(n-1)
        algae(n-2)

iterations = 8 # how many rounds of substitutions to make
for i in range(iterations):
    print('n =', i, end=" ")
    algae(i)
    print('')
