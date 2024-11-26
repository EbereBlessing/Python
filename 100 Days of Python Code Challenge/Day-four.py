# Python Randomization and List
# ROCK PAPER SCISSOR GAME
import random
rock = [ ("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """), ("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
    """), ("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---._ _(___)
    """) ]
computer = random.randint(0, 2)
  #computer = rock[index]
player = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: '))
if 0 <= player <= 2:
    # Print the player's choice
    print(f"You chose: {rock[player]}")
    print("The computer chose:")
    print(rock[computer])
    if player == computer:
        print("It's a draw!")
    elif (player == 0 and computer == 2) or \
         (player == 1 and computer == 0) or \
         (player == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
else:
      print('Choose a valid number between 0-2')
       
       





