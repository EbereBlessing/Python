# 100 Days of Python Challenge - Day 2 Tip Calculator
# This challenge is about building a Tip Calculator.The program asks for the total bill, tip amount the user wants to give, and the number of people. It then calculates how much each person should pay, including the tip.
print('Welcome to Tip calculator')
# Get inputs from the user
total_bill = float(input('What was the total bill?\n $'))
tip = int(input('How much tip would you like to give? 10, 12 or 15\n'))
people = int(input('How many people to split the bill?\n'))
# Calculate the tip amount and the total bill and then Split the bill among people
tip_total = (tip / 100) * total_bill
Bill = (total_bill + tip_total) / people
# Display the amount each person should pay
print(f'Each Person should Pay: ${round(Bill, 2)}')