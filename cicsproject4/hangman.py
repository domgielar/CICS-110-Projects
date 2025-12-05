# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500

import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(answer, guess):
    for i in range(len(answer)):
        if answer[i].isalpha()==False:
            print(answer[i], end="")
        elif answer[i] in guess:
            print(answer[i].upper(), end="")
        else:
            print("_",end="")




def get_letter(guessed):
    valid=True
    while valid:
        temp = input("Please enter a letter: ").upper()
        if (temp.isalpha()==False) or (len(temp)!=1):
            print(f'\n"{temp}" is not a letter!')
        elif temp in guessed:
            print(f'\n"{temp}" has already been guessed!')
        else:
            return temp
            valid = False

def won(answer,guessed):
    winner =True
    for i in answer:
        if not i.isalpha():
            continue
        if i not in guessed:
            winner = False
            break
    return winner
    



def play_game():
    phrase=make_phrase()
    misses=0
    guess=[]
    print(f"*** Welcome to Hangman ***")
    print_gallows(misses)
    print("")

    while True:
        if misses==6:
            print(f"Game Over!\nSolution was: {phrase}")
            break
        print_revealed_phrase(phrase,guess)
        print(f"\nLetters guessed: {guess}")
        letter=get_letter(guess)
        guess.append(letter)
        guess.sort()
        if letter not in phrase:
            misses+=1
            print_gallows(misses)
        else:
            winner = won(phrase,guess)
            if winner==True:
                print_revealed_phrase(phrase,guess)
                print(f"\nCongratulations!")
                break
            continue


play_game()
