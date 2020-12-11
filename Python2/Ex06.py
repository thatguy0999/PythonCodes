cost_meal = float(input('what is the cost of the meal'))
cost_tax = cost_meal*(7/100)
cost_tip = cost_meal*(18/100)
cost_total = cost_meal + cost_tax + cost_tip

print(f'{"receipt":-^22s}')
print(f'{"Meal":.<17s}${cost_meal:>.2f}')
print(f'{"Tax":.<18s}${cost_tax:>.2f}')
print(f'{"Tip":.<18s}${cost_tip:>.2f}')
print(f'{"Total cost":.<17s}${cost_total:>.2f}')