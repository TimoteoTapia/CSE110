from colorama import *
init()
from time import sleep

print(Fore.GREEN + 'Hi Eric,' + Fore.WHITE + '\nWelcome to  my project \nHelp me to get to know you better')

#input, Prompt the user to enter her data.
color = input(Back.YELLOW + 'Please, tell me what is your favorite color? (type now the answer) → ' + Back.BLACK)
animal = input('what is now your favorite animal → ')
place = input('finally, where is your favorite place to spend your time → ')

# Print the numbers 3, 2, 1.
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5) 

#output
print(Fore.BLUE + f'Now I know what you like, you like a {color} {animal} that lives at {place}')