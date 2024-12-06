# Based on a User's order, work out the final bill. Use the input function to get a user's preferences and then add up the total of their order and tell them how much they have to pay.
# small pizza = $15, medium pizza = $20, large pizza = $25
# pepperoni for small = $2, medium and large peperroni = $3
# Add extra cheese for any size pizza = $3

print('Welcome to Pizza shop')
pizza = input('What size Pizza do you want? s, m or l:')
pepperoni = input('Do you want pepperoni on your pizza? y or n: ')
extra_cheese = input('Do you want extra cheese? y or n: ')
if pizza == 's':
    bill = 15
    if pepperoni == 'y':
         bill += 2
    if extra_cheese == 'y':
         bill += 1
    print(f'Your total bill is ${bill}')
elif pizza == 'm':
    bill = 20
    if pepperoni == 'y':
         bill += 3
    if extra_cheese == 'y':
         bill += 1
    print(f'Your total bill is ${bill}')
elif pizza == 'l':
    bill = 25
    if pepperoni == 'y':
         bill += 3
    if extra_cheese == 'y':
         bill += 1
    print(f'Your total bill is ${bill}')
else: 
     print('You typed the wrong input')

