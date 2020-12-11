WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

no_widgets = int(input('how many widgets?'))
no_gizmos = int(input('how many gizmos?'))

total_weight = (WIDGET_WEIGHT*no_widgets) + (GIZMO_WEIGHT*no_gizmos)

print(f'The total weight of your order is {total_weight}g')