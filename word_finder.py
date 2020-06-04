import string as alpha
import random

alphabet = alpha.ascii_lowercase
alphabet = tuple(alphabet)
print("welcome in hangman \nwe have a hidden word.\nyou have to guess letters present in word")

name = input("enter your name: ")

i = 15
# modification word and chance
print("if you want to modify the game press 'M' otherwise just enter ")
while True:
    modify = input()
    if modify:
        modify = modify.strip().lower()
        if 'm' == modify:
            i = int(input("no. of chance: "))
            break
        else:
            print("type again 'M' for modification or 'enter' for continue")
            continue
    else:
        pass
        break
# chose random word according to list
w = ['car','park','wood','table','toy']
word = random.choice(w)

word1 = ['_' for k in word]
double_letter = []
print("let's start")
word2 = " ".join(word1)
print(f"here is the {len(word1)} letter hidden word {word2}")
print(f"you have only {i} chances")

while i >= 0:
    # end code
    if i == 0:
        print()
        print(f"YOU LOOSE {name}")
        print(f"Word is {word}")
        break
    # calling input values
    print()
    a = input("enter letter: ")
    # quit game
    if 'quit' == a:
        print("game is closed")
        break
    # check weather input is empty or not
    a = a.strip()
    if a:
        pass
    else:
        print("you have entered Nothing")
        continue
    # check weather input is one or more than one values
    if len(a) == 1:
        pass
    else:
        print("WRONG INPUT")
        print("please enter single letter")
        continue

    # check weather input in alphabet or number
    a = a.lower()
    if a in alphabet:
        pass
    else:
        print("WRONG INPUT")
        print("please enter alphabet")
        continue

    if a in word:
        # right guess
        if a not in word1:
            index = word.index(a)
            word1.pop(index)
            word1.insert(index, a)
            count1 = word.count(a)
            for k in range(word.count(a) - 1):
                index = word.index(a, index + 1)
                word1.pop(index)
                word1.insert(index, a)
            print("RIGHT GUESS")
            print(" ".join(word1))
            i -= 1
            print(f"you have left only: {i} chance")
            # winner
            if word == "".join(word1):
                print(f"congratulation {name} \nwin! win!\nwin! win!")
                break
            continue
        # repeat right guess
        else:
            print(f"you have already entered: {a}")
            print(" ".join(word1))
            print(f"you have left only: {i} chance")
            continue

    else:
        # wrong guess
        if a not in double_letter:
            double_letter.append(a)
            string = ", ".join(double_letter)
            print("WRONG GUESS ")
            print(f"letter entered: {string} ")
            print(" ".join(word1))
            i -= 1
            print(f"you have left only: {i} chance")
            continue
        # repeat wrong guess
        else:
            print(f"you have already entered: {a}")
            print(f"letter entered: {string} ")
            print(" ".join(word1))
            print(f"you have left only: {i} chance")
            continue
