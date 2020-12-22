re = 0 

no = int(input('please enter a number  '))
guess = no/2
while abs(guess*guess - no) > 10**(-12):
    guess = (guess + no/guess)/2

print(guess)
