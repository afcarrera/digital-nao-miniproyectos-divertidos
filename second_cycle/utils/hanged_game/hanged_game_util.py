def refill_phrase(_wl, idx_list, letter):
    goods = 0
    for idx in idx_list:
        _wl[idx] = letter
        goods += 1
    return goods
        
def get_letter_selected(request):
    if request.form.get('A') == 'A':
        return 'A'
    elif  request.form.get('B') == 'B':
        return 'B'
    elif  request.form.get('C') == 'C':
        return 'C'
    elif  request.form.get('D') == 'D':
        return 'D'
    elif  request.form.get('E') == 'E':
        return 'E'
    elif  request.form.get('F') == 'F':
        return 'F'
    elif  request.form.get('G') == 'G':
        return 'G'
    elif  request.form.get('H') == 'H':
        return 'H'
    elif  request.form.get('I') == 'I':
        return 'I'
    elif  request.form.get('J') == 'J':
        return 'J'
    elif  request.form.get('K') == 'K':
        return 'K'
    return _get_letter_selected_part_two(request)
        
def _get_letter_selected_part_two(request):
    if  request.form.get('L') == 'L':
        return 'L'
    elif  request.form.get('M') == 'M':
        return 'M'
    elif  request.form.get('N') == 'N':
        return 'N'
    elif  request.form.get('O') == 'O':
        return 'O'
    elif  request.form.get('P') == 'P':
        return 'P'
    elif  request.form.get('Q') == 'Q':
        return 'Q'
    elif  request.form.get('R') == 'R':
        return 'R'
    elif  request.form.get('S') == 'S':
        return 'S'
    elif  request.form.get('T') == 'T':
        return 'T'
    elif  request.form.get('U') == 'U':
        return 'U'
    elif  request.form.get('V') == 'V':
        return 'V'
    elif  request.form.get('W') == 'W':
        return 'W'
    elif  request.form.get('X') == 'X':
        return 'X'
    elif  request.form.get('Y') == 'Y':
        return 'Y'
    elif  request.form.get('Z') == 'Z':
        return 'Z'