# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500

import random

def get_guess():
    guess = input("What word is this?: ").upper()
    return guess

def print_word(guess):
    spaced = " ".join(guess)
    print(spaced)

def exact_match_compare(sol, guess):
    solution = list(sol)
    prompt = list(guess)
    feedback =[]
    for i in range(len(solution)):
        if (len(solution)>i and len(prompt)>i):
            if(solution[i]==prompt[i]):
                feedback.append("🟢")
            else:
                feedback.append("🔴")
        else:
            break
    return ''.join(feedback)


def make_solution():
    rando = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
    sol = random.choice(rando)
    return sol


def one_turn(sol):
    guess = get_guess()
    print_word(guess)
    feedback = exact_match_compare(sol, guess)
    print(feedback)
    if feedback == "🟢🟢🟢🟢🟢":
        print("Congratulations!")
        exit()



sol = make_solution()
one_turn(sol)
one_turn(sol)
one_turn(sol)
one_turn(sol)
one_turn(sol)
one_turn(sol)
print(f"Word was \"{sol}\", better luck next time.")
    


