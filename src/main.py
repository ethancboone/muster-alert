from inbox_check import daily_inbox_check

response = daily_inbox_check()

if response != True: 
    print('You still need to muster')
else:
    print('Muster completed')