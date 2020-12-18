total_sum = 0

while True:
    prices = input('please enter the price of the product  ')
    if prices == '':
        break

    else:
        total_sum += float(prices)

print(f'Actual Total Price - ${total_sum}')

total_sum = total_sum*100

if total_sum%5 <= 2:
    while total_sum%5 != 0:
            total_sum -= 1

else:
    while total_sum%5 != 0:
            total_sum += 1

print(f'Estimated Total Price - ${total_sum/100:.2f}')


    