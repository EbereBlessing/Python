#Task:
# You ask the user for their height (in cm) and age. If the height is less than or equal to 120 cm, output “Can’t ride.”
# If they can ride, charge: $5 if they are under 12 years old, $7 if they are between 12 and 18 years old, free ride if they are between 45 and 55 years old and $12 if they are older than 18 years.
# After determining if the person can ride and calculating the base ticket price, ask if they want a photo, which adds $3 to the price
print('Welcome To Rollercoaster Succession')
Height = int(input('what is your height in cm?'))
if Height > 120:
    age = int(input('How old are you?'))
    if age < 12:
       bill = 5
       print ('Your adult bill is $5')
    elif  age <= 17:
        bill = 7
        print ('Your adult bill is $7')  
    elif age == 45 and age <= 55:
        bill = 0 
        print ('It is a free ride') 
    else:
        bill = 12
        print('Your adult bill is $12')
    photo = input('Do you want a photo?, y or n\n')
    if photo == "y":
        bill += 3
    print (f'Your total bill is {bill}')
else:
    print('You cannot ride')


