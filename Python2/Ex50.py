from math import sqrt

a = float(input('what will be the value of a '))
b = float(input('what will be the value of b '))
c = float(input('what will be the value of c '))

no_roots = (b**2)-(4*a*c)
if no_roots < 0:
    print('there are no intersections with the x axis')

elif no_roots == 0:
    print('there is a repeated intersection / one intersection with the x axis')
    print(f'{(-b+sqrt(no_roots))/2*a:.3f}')

elif no_roots > 0:
    print('there are two intersections with the x axis')
    print(f'{(-b+sqrt(no_roots))/2*a:.3f}')
    print(f'{(-b-sqrt(no_roots))/2*a:.3f}')

