old_bread = int(input('how many pieces of old bread'))

print(f'''
The regular price would be ${old_bread*3.49}
The discount is ${old_bread*3.49*0.4:.2f}
The new price is ${old_bread*3.49*0.6:.2f}
''')

