interest_rate = 4

account = float(input('how much are you depositing?'))

for i in range(1,4):
    print(f'year {i} - {account*(1 + interest_rate/100)**(i):.2f}')