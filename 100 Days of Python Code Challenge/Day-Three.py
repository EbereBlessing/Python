# 100 Days of Python Challenge - Day 3 Treasure island
# Create a Python program where the player makes decisions to find the treasure:
# First, prompt the player to choose left or right, left = Game Over and right = continue. Then, prompt the player to choose swim or wait: swim = Game Over and wait = continue. Finally, prompt the player to choose a door: Red, Blue, or Yellow: Red or Blue = Game Over and Yellow = You Win!
beast = """
     ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
"""
print(beast)
print('Welcome to Treasure Island. \nYour mission is to find the treasure.')
a = input('You are a cross road. Where do you want to go.?\n    Type "left" or "right"?\n').lower()
if a == 'left':
    b = input('You have come to a lake. There is an island in the middle of the lake.\n    Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if b == 'wait':
       c = input('You arrive at the island unharmed. There is a house with 3 doors.\n  One red, One yellow and one blue. Which colour do you choose?\n').lower()
       if c == 'blue':
           print('Eaten by Beasts. Game Over')
       elif c == 'red':
           print('Burned by Fire. Game Over')
       elif c == 'yellow':
           print('Congratulations! You found the treasure! You Win!') 
       elif c != 'red' or c != 'blue' or c != 'yellow':
          print('Game Over losser') 
    else:
        print('Attacked by trout.\n Game Over.') 
else: 
    print('Fall into a hole. Game Over !!')
