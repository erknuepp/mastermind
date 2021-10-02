### Mastermind Game
# Adapted by NutrinoLabs
# Author edward.knueppel.jr@gmail.com
# YMD Started: 2021-10-01

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
board_size = 4
turn_size = 5

def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), board_size)
    return [legal_colors[i] for i in sequence]

#If the color is vaild return true otherwise return false
#Return type Boolean
def legal_color(color):
    if color in legal_colors:
        return True
    else: 
        return False

#A loop to check that all colors are valid by calling legal_color() def
#Return type Boolean
def is_valid(guess):
    for i in range(len(guess)):
        if legal_color(guess[i]): #This is accessing the ith index of guess. Strings are treated as arrays of characters in Python
            continue #If it is valid, continue to check the next color
        else:
            return False #If a color is invalid return false
    return True #If they are all valid retrn true

#A loop to check if any color is repeated
#Return type Boolean   
def has_repeats(guess):
    for i in range(len(guess)):
        if guess.count(guess[i]) > 1: #Checks the ith index of guess to see if guess contains that color more than once using count()
            return True #if it does return true
        else:
            return False #else return false

#Takes in the letter and index to compare it to the key
#Returns "R" for correct color and position
#Returns "W" for correct color and wrong position
#Returns "_" for incorrect color
#Return type str
def get_peg_for_letter(solution_letter, solution_index, key):
    if solution_letter in key:
        if key.index(solution_letter) == solution_index:
            return "R"
        else:
            return "W"
    else:
        return "_"

def get_pegs(solution, key):
    pegs = ""
    for i in range(len(solution)):
        pegs += get_peg_for_letter(solution[i], i, key)
    return pegs

colors = generate_color_sequence()
#colors = ['R', 'G', 'B', 'Y'] ### Uncomment to use Test Data ###
#print(colors) ### Uncomment if debugging ###

attempts = 0
has_won = False
while(not has_won and attempts < turn_size): #Game loop 5 chances to guess the correct colors and order
    attempts += 1
    flag = True
    while(flag):
        print("Options: 'R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V'")
        guess = input("Enter your guess (4 letters):").upper()
        #Validate size of guess is 4 characters, each color in guess is valid and no colors in guess are repeating:
        if len(guess) != 4:
            print(len(guess))
            print("Sorry that choice is not 4 characters!")
            continue
        elif not is_valid(guess):
            print("Sorry that choice has at least one invalid character!")
            continue
        elif has_repeats(guess):
            print("Sorry that guess has repeats")
            continue
        else:
            flag = False
        

    pegs = get_pegs(guess, colors)

    if pegs == "RRRR":
        has_won = True
    else:
        print("Keep trying! Your current solution results are " + pegs)
    

if(has_won):
    print("Holy smokes you did it in " + str(attempts) + " attempts!")
else:
    print("Hey, don't feel bad, friend; barely anyone can beat THE MASTERMIND!!!!!1111")
