freq = float(input('name the frequency you want to find the note of (Hertz)'))

if 260.63 <= freq <= 262.63:
    print('C4')

elif 292.66 <= freq <= 294.66:
    print('D4')

elif 328.63 <= freq <= 330.63:
    print('E4')

elif 348.23 <= freq <= 350.23:
    print('F4')

elif 391 <= freq <= 393:
    print('G4')

elif 439 <= freq <= 441:
    print('A4')

elif 492.88 <= freq <= 494.88:
    print('B4')

else:
    print('there is no frequency like that corresponding to a known note')