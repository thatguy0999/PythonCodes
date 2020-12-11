from math import *

a = int(input('Give an integer value to a'))
b = int(input('Give an integer value to b'))

print(f'''
The sum is {a + b}
The difference when b is subtracted from a is {a - b}
The product is {a*b}
The quotient when a is divided by b is {a//b}
The remainder when a is divided by b is {a%b}
The result of log(a) is {log10(a)}
The result of a^b is {a**b}
''')