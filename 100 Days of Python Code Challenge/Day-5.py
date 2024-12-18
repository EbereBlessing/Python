# CODE CHALLENGE - Create a Password Generator 
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
if nr_symbols <= 0 or nr_letters  <= 0 or nr_numbers  <= 0 :
     print("Please enter a positive number.")
elif nr_symbols > len(symbols) or nr_letters > len(letters) or nr_numbers > len(numbers):
        print(f"You requested more letters than available. Please enter a number between 1 and {len(letters)} for Letters and between 1 and {len(symbols)} for symbols and between 1 and {len(numbers)} for numbers.")
else:
           selected_symbols = random.sample(symbols, nr_symbols)
           selected_numbers = random.sample(numbers, nr_numbers)
           selected_letters = random.sample(letters, nr_letters)
           password_list = selected_letters + selected_symbols + selected_numbers
           random.shuffle(password_list)
           password = ''.join(password_list)
           print(f"Your generated password is: {password}")

