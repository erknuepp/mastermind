import game as g

def test_generate_code_sequence():
    board_size = 1
    code_group = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
    thing = g.generate_code_sequence(code_group, board_size)
    for c in thing:
        assert c in code_group

def test_generate_code_sequence_zero_board_size():
    board_size = 0
    code_group = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
    thing = g.generate_code_sequence(code_group, board_size)
    for c in thing:
        assert c in code_group

def test_generate_code_sequence_large_board_size():
    board_size = 30
    code_group = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
    thing = g.generate_code_sequence(code_group, board_size)
    for c in thing:
        assert c in code_group

def test_get_peg_for_char():
    guess_char = "A"
    guess_index = 0
    pattern = "ABCD"
    assert "R" == g.get_peg_for_char(guess_char, guess_index, pattern)