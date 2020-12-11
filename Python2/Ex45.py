odd = {'a','c','e','g'}

column, row = input('please enter a position on the chess board ')
row = int(row)

if column in odd:
    if row%2 == 1:
        print('black')
    
    else:
        print('white')

else: 
    if row%2 == 1:
        print('white')

    else:
        print('black')