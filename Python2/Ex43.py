# while True:
#     note = int(input('please enter the value of a banknote '))
#     if note == 1: 
#         print('George Washington')
#         break
    
#     elif note == 2:
#         print('Thomas Jefferson')
#         break

#     elif note == 5:
#         print('Abraham Lincoln')
#         break

#     elif note == 10:
#         print('Alexander Hamilton')
#         break

#     elif note == 20:
#         print('Andrew Jackson')
#         break

#     elif note == 50:
#         print('Ulysses S. Grant')
#         break

#     elif note == 100:
#         print('Benjamin Franklin')
#         break

#     else:
#         print('there is no banknote of that value')

banknote = {
    1:'George Washington',
    2:'Thomas Jefferson',
    5:'Abraham Lincoln',
    10:'Alexander Hamilton',
    20:'Andrew Jackson',
    50:'Ulysses S. Grant',
    100:'Benjamin Franklin',
}
while True:
    note = int(input('enter the value of a banknote'))
    try:
        print(f'the person on that banknote is {banknote[note]}')
        break

    except:
        print('there is no banknote with that value')