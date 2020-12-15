call_time = int(input('how many minutes have been used in calls '))
message_no = int(input('how many messages have been sent '))

print(f' ')
print(f'{"CELLPHONE BILL":~^30s}')
print(f'Base Plan{"$15.00":->21s}')
if call_time > 50:
    print(f'{"Additional Calltime":-<25s}${(call_time - 50)*0.25:.2f}')
if message_no > 50:
    print(f'{"Additional Messages":-<25s}${(message_no - 50)*0.15:.2f}')
print(f'911 Call Support{"$0.44":->14s}')
if message_no < 50:
    message_no = 50
if call_time < 50:
    call_time = 50
print(f'{"Sales Tax":-<25s}${(0.44 + 15 + (call_time - 50)*0.25 + (message_no - 50)*0.15)*0.05:.2f}')
print(f'{"Total Cost":-<24s}${(0.44 + 15 + (call_time - 50)*0.25 + (message_no - 50)*0.15)*1.05:.2f}')
print(f'{"~":~^30s}')