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

def display_logo():
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

def display_code_group(code_group):
    print("\nCode Group: ", end='')
    [print(x + ", ", end='') for x in code_group]
import game
pattern = game.generate_code_sequence(code_group, board_size)
#colors = ['R', 'G', 'B', 'Y'] ### Uncomment to use Test Data ###
#print(colors) ### Uncomment if debugging ###

turn = 0 #The number of guesses
has_won = False #The win state of the game

display_logo()
print("Welcome to Mastermind, Friendo. Good luck!")


while(not has_won and turn < number_of_turns):
    turn += 1 #Increase the attempts by 1 at start of attempt
    invalid = True #Start invalid and if you pass all validations switch to false
    while(invalid):
        display_code_group(code_group)
        print("Turn #" + str(turn))
        guess = input("\nEnter your guess (4 valid symbols):").upper()
        #Validate size of guess is 4 characters, each color in guess is valid and no colors in guess are repeating:
        if len(guess) != board_size:
            print("\nSorry that guess is not " + board_size + " characters!")
            continue
        elif not is_valid_guess(guess):
            print("\nSorry that guess has at least one invalid character!")
            continue
        elif has_repeats(guess):
            print("\nSorry that guess has repeats")
            continue
        else:
            invalid = False
        
    #Calculate the results of this guess
    pegs = game.get_pegs(guess, pattern)

    if pegs == "R" * board_size:
        has_won = True
    elif turn < number_of_turns:
        print("\nKeep trying! Your hints are " + pegs)
    

if(has_won):
    for i in range(1000):
        print(("Holy smokes you did it in " + str(turn) + " turns!               ") * 3) 
else:
    print("\nHey, don't feel bad, Friendo; barely anyone can beat THE MASTERMIND!!!!!1111")
