def invalid():
    print('please enter a valid license plate')

while True:
    lic_plate = input('please enter a license plate ')
    if len(lic_plate) == 6:
        if lic_plate[:3].isupper() and lic_plate[3:6].isnumeric():
            print('Older License Plate')
            break

        else:
            invalid()

    elif len (lic_plate) == 7:
        if lic_plate[:4].isnumeric() and lic_plate[4:7].isupper():
            print('Newer License Plate')
            break

        else: 
            invalid()
    
    else:
        invalid()