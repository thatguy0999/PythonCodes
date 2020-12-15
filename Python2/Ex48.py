animal = {
    8:'dragon',
    9:'snake',
    10:'horse',
    11:'sheep',
    0:'monkey',
    1:'rooster',
    2:'dog',
    3:'pig',
    4:'rat',
    5:'ox',
    6:'tiger',
    7:'hare',
}

year = int(input('please enter a year'))

# year_r stands for year remainder after division w/ 11
year_r = year%12

print(f'{animal[year_r]}')
