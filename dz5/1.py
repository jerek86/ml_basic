def is_capital_letter(letter):
    return ord('A') <= ord(letter) <= ord('Z')

def get_lowercase_letter(letter):
    return chr(ord(letter) - ord('A') + ord('a'))

def get_capital_letter(letter):
    return chr(ord(letter) - ord('a') + ord('A'))

def convert_to_case(string, need_snake_case):
    is_snake_case = None
    result = ''

    need_convert_to_capital = False
    is_first_letter = True
    for letter in string :
        if is_capital_letter(letter) :
            if is_snake_case is True :
                print('error, wrong input case')
                return None
            is_snake_case = False
            if not need_snake_case :
                return string
            if not is_first_letter :
                result += '_'
            result += get_lowercase_letter(letter)
        elif letter == '_' :
            if is_snake_case is False :
                print('error, wrong input case')
                return None
            is_snake_case = True
            if need_snake_case :
                return string
            need_convert_to_capital = True
        else :
            if need_convert_to_capital :
                result += get_capital_letter(letter)
                need_convert_to_capital = False
            else :
                result += letter
        is_first_letter = False

    return result

print('otus_course -> ', convert_to_case('otus_course', True))
print('otus_course -> ', convert_to_case('otus_course', False))
print('PythonIsTheBest -> ', convert_to_case('PythonIsTheBest', True))
print('PythonIsTheBest -> ', convert_to_case('PythonIsTheBest', False))
print('Python_isTheBest -> ', convert_to_case('Python_isTheBest', True))