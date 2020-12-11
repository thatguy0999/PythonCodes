n = input('how many drink containers do you have')
refund = 0

for i in range(int(n)):
    volume = float(input('what is the volume of the drink container you wish to return (litres)'))
    if volume <= 1:
        refund += 0.1
    
    else:
        refund += 0.25

print(f'cashback is ${refund:.2f}')