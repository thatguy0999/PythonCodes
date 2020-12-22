# while True:
#     sum = 0
#     parity = input('please enter an 8 bit number  ')
#     if parity == '':
#         print('thanks for using the parity bit generator')

#     elif len(parity) != 8:
#         print('invalid number')

#     else:
#         for i in range(8):
#             sum += int(parity[i])
        
#         if sum%2 == 0:
#             print('1')

#         else:
#             print('0')

while True:
    parity = input('please enter an 8 bit number  ')
    if parity == '':
        print('thanks for using the parity bit generator')

    elif len(parity) != 8:
        print('invalid number')

    else:
        if parity.count('1')%2:
            print(0)

        else:
            print(1)