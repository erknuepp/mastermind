def generate_code_sequence(code_group, board_size):
    import random
    random.seed()
    sequence = random.sample(range(len(code_group)), board_size)
    return [code_group[i] for i in sequence]

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