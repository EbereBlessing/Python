# Simple Interest Calculator
# Task - Write a Python script that calculates the simple interest using the formula SI = P ×R×T/100 , where P is principal amount, R is rate per annum, and T is time in years. 
# The script should ask the user to input P, R, and T and then print the calculated interest.
print('Simple Interest Calculator')
principal = float(input('What Is The Principal Amount?\n$'))
rate = float(input('What is the rate per Annum?\n'))
time = int(input('What time in year'))
SI = principal * rate * time
percentage_SI = SI/100
print(f'Your simple interest is: ${percentage_SI}')
