# L-system for algae growth using regular CFG-type definition

# variable A
def algae_a(n):
    if n == 0:
        print('A', end="")
    else:
        algae_a(n-1)
        algae_b(n-1)

# variable B
def algae_b(n):
    if n == 0:
        print('B', end="")
    else:
        algae_a(n-1)

iterations = 8 # how many rounds of substitutions to make
for i in range(iterations):
    print('n =', i, end=" ")
    algae_a(i) # enters axiom state
    print('')
