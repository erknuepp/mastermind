### Mastermind Game
# Adapted by NutrinoLabs
# Author edward.knueppel.jr@gmail.com
# YMD Started: 2021-10-01
# https://en.wikipedia.org/wiki/Mastermind_(board_game)

# Future enhancements

## Allow blanks
allow_blanks = False

## Allow repeats
allow_repeats = False

### BEGIN
code_group = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
board_size = 4 
number_of_turns = 5

def generate_code_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(code_group)), board_size)
    return [code_group[i] for i in sequence]

#If the color is vaild return true otherwise return false
#Return type Boolean
def is_legal_symbol(color):
    if color in code_group:
        return True
    else: 
        return False

#A loop to check that all colors are valid by calling legal_color() def
#Return type Boolean
def is_valid_guess(guess):
    for i in range(len(guess)):
        if is_legal_symbol(guess[i]): #This is accessing the ith index of guess. Strings are treated as arrays of characters in Python
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
def get_peg_for_char(guess_char, guess_index, pattern):
    if guess_char in pattern:
        if pattern.index(guess_char) == guess_index:
            return "R"
        else:
            return "W"
    else:
        return "_"

#Checks each position in the solution against the key and returns a combination of pegs
#Return type str
def get_pegs(guess, pattern):
    pegs = ""
    for i in range(len(guess)):
        pegs += get_peg_for_char(guess[i], i, pattern)
    return pegs

pattern = generate_code_sequence()
#colors = ['R', 'G', 'B', 'Y'] ### Uncomment to use Test Data ###
#print(colors) ### Uncomment if debugging ###

turn = 0 #The number of guesses
has_won = False #The win state of the game

print("""
                                                ,----,                                                                       
          ____                                ,/   .`|                              ____                   ,--.              
        ,'  , `.   ,---,       .--.--.      ,`   .'  :   ,---,.,-.----.           ,'  , `.   ,---,       ,--.'|    ,---,     
     ,-+-,.' _ |  '  .' \     /  /    '.  ;    ;     / ,'  .' |\    /  \       ,-+-,.' _ |,`--.' |   ,--,:  : |  .'  .' `\   
  ,-+-. ;   , || /  ;    '.  |  :  /`. /.'___,/    ,',---.'   |;   :    \   ,-+-. ;   , |||   :  :,`--.'`|  ' :,---.'     \  
 ,--.'|'   |  ;|:  :       \ ;  |  |--` |    :     | |   |   .'|   | .\ :  ,--.'|'   |  ;|:   |  '|   :  :  | ||   |  .`\  | 
|   |  ,', |  '::  |   /\   \|  :  ;_   ;    |.';  ; :   :  |-,.   : |: | |   |  ,', |  ':|   :  |:   |   \ | ::   : |  '  | 
|   | /  | |  |||  :  ' ;.   :\  \    `.`----'  |  | :   |  ;/||   |  \ : |   | /  | |  ||'   '  ;|   : '  '; ||   ' '  ;  : 
'   | :  | :  |,|  |  ;/  \   \`----.   \   '   :  ; |   :   .'|   : .  / '   | :  | :  |,|   |  |'   ' ;.    ;'   | ;  .  | 
;   . |  ; |--' '  :  | \  \ ,'__ \  \  |   |   |  ' |   |  |-,;   | |  \ ;   . |  ; |--' '   :  ;|   | | \   ||   | :  |  ' 
|   : |  | ,    |  |  '  '--' /  /`--'  /   '   :  | '   :  ;/||   | ;\  \|   : |  | ,    |   |  ''   : |  ; .''   : | /  ;  
|   : '  |/     |  :  :      '--'.     /    ;   |.'  |   |    \:   ' | \.'|   : '  |/     '   :  ||   | '`--'  |   | '` ,/   
;   | |`-'      |  | ,'        `--'---'     '---'    |   :   .':   : :-'  ;   | |`-'      ;   |.' '   : |      ;   :  .'     
|   ;/          `--''                                |   | ,'  |   |.'    |   ;/          '---'   ;   |.'      |   ,.'       
'---'                                                `----'    `---'      '---'                   '---'        '---'         
                                                                                                                             
""")
print("Welcome to Mastermind, Friendo. Good luck!")
while(not has_won and turn < number_of_turns):
    turn += 1 #Increase the attempts by 1 at start of attempt
    invalid = True #Start invalid and if you pass all validations switch to false
    while(invalid):
        print("\nCode Group: ", end='')
        [print(x + ", ", end='') for x in code_group]
        guess = input("\nEnter your guess (4 valid symbols):").upper()
        #Validate size of guess is 4 characters, each color in guess is valid and no colors in guess are repeating:
        if len(guess) != board_size:
            print(len(guess))
            print("\nSorry that guess is not " + board_size + " characters!")
            continue
        elif not is_valid_guess(guess):
            print("Sorry that guess has at least one invalid character!")
            continue
        elif has_repeats(guess):
            print("Sorry that guess has repeats")
            continue
        else:
            invalid = False
        
    #Calculate the results of this guess
    pegs = get_pegs(guess, pattern)

    if pegs == "R" * board_size:
        has_won = True
    elif turn < number_of_turns:
        print("\nKeep trying! Your hints are " + pegs)
    

if(has_won):
    for i in range(100000):
        print(("Holy smokes you did it in " + str(turn) + " turns!") * 10000, end='') 
else:
    print("\nHey, don't feel bad, Friendo; barely anyone can beat THE MASTERMIND!!!!!1111")
