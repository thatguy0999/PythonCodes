pi = 0

for i in range(15):
    if i == 0:
        pi = 3

    else:
        pi += (4/((2 + 2*(i-1))*(3 + 2*(i-1))*(4 + 2*(i-1)))*((-1)**(i%2 + 1)))
    
    print(f'{pi}')