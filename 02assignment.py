""""
Madlib: It is a funny story to enjoy adding words
Author: Timoteo Tapia
"""
#import colorama to use colors
from colorama import *

#This is my main() function
def main():
    print("please enter the following: \n".capitalize())
    words = list_inputs()
    story(words)
    if next_story():
        words = []
        second_list(words)
        prompt_user_two(words)
        story_two(words)

#it is the display of the second story with the words prompted before
def story_two(words):
    print()
    print("dear {},\n".capitalize().format(words[0]))
    print(f"You are extremly {words[1]} and I {words[2]} you!")
    print(f"I want kiss your {words[3]} {words[4]} times.")
    print("You make my {} burn with desire".format(words[5]))
    print("When I first saw you, I looked at you and fell in love")
    print("Will you {} out with me? Don`t let your parents discourage you.".format(words[6]))
    print()
    print(f"Yours forever, {words[7]}")
    print("        __  __  ")
    print("       /  \/  \ ")
    print("       \      / ")
    print("        \    /  ")
    print("         \  /   ")
    print("          \/  \n")

#it prompts to the user by second time a list of words
#adds the color blue and capitalize person names
def prompt_user_two(words):
    for number in range(8):
        check_user = True
        while check_user:
            if words[number] == "Friend's name: ":
                words[number] = input(f"{words[number]}")
                words[number] = Fore.BLUE + words[number].capitalize() + Fore.WHITE
                check_user = False
            else:    
                words[number] = input(f"{words[number]}")
                words[number] = Fore.BLUE + words[number] + Fore.WHITE
                check_user = False

#saves the second words in a list
def second_list(words):
    for prompts in prompt_words():
        words.append(prompts)
    return words

# it saves the string will be ask to the user
def prompt_words():
    person = "Friend's name: "
    adjective = "Adjective: "
    verb = "Verb: "
    body = "Part of body: "
    number = "Number: "
    noun = "Noun: "
    verb2 = "Verb: "
    person2 = "Friend's name: "
    return person,adjective,verb,body,number,noun,verb2,person2

#it asks the user if he/she wants to continue with a second story
def next_story():
    check_answer = True
    while check_answer:
        user_answer = input("Would you like to participate in a second story? (yes/no): ")
        if user_answer.isalpha():    
            if user_answer == "yes" or user_answer == "Yes" or user_answer == "no" or user_answer == "No":
                check_answer = False
                if user_answer == "yes" or user_answer == "Yes":
                    print ("\nExcelent, enter de following: \n")
                    return True
                return False
            else:
                print("\nInsert a valid value\n")
        else:
            print("\nInsert a valid value\n")

#creates the first list
def list_inputs():
    words = []
    for prompts in prompt_user():
        words.append(prompts)
    return words

#it prompts to the user a list of words
def prompt_user(): 
    adjective_prompt = input("adjective: ")
    animal_prompt = input("animal: ")
    verb1_prompt = input("verb: ")
    exclamation_prompt = input("exclamation: ")
    verb2_prompt = input("verb: ")
    verb3_prompt = input("verb: ")
    return adjective_prompt,animal_prompt,verb1_prompt,exclamation_prompt,verb2_prompt,verb3_prompt

#it is the display of the first story with the words prompted before
def story(words):
    print()
    print("your story is: ".capitalize())  
    print()
    print(f"The other day, I was really in trouble. It all started when I saw a very") 
    print(f'{words[0]} {words[1]} {words[2]} down the hallway. "{words[3]}!" I yelled. But all')
    print("I could think to do was to {} over and over. Miraculousy,".format(words[4]))
    print("that caused it to stop, but not before it tried to {}".format(words[5]))
    print("right in front of my family.\n\n")

main()