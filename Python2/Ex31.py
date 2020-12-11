# no = int(input('please enter a four digit integer'))

# ones = no%10
# no -= ones
# tens = (no%100)/10
# no -= tens*10
# hundreds = (no%1000)/100
# no -= hundreds*100
# thousands = (no%10000)/1000

# print(f'the sum of these numbers are {ones + tens + hundreds + thousands}')

no_sum = 0

number = input('please enter a four digit integer')

for i in range(4):
    no_sum += int(number[i])

print(f'{no_sum}')