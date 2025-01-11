total_table = dict()

def print_total_table() :
    for key, value in total_table.items() :
        print("%08d"%key, ':', value)

def is_capital_letter(letter):
    return ord('A') <= ord(letter) <= ord('Z')

def is_symbol(letter):
    return is_capital_letter(letter) or ord('a') <= ord(letter) <= ord('z')

def get_capital_letter(letter):
    return chr(ord(letter) - ord('a') + ord('A'))

def is_age_correct(age) :
    return 18 <= age <= 60

def correct_name(name) :
    result = ''

    first_letter_found = False

    for letter in name :
        if not is_symbol(letter) :
            continue

        if first_letter_found is False :
            if not is_capital_letter(letter) :
                result += get_capital_letter(letter)
            else :
                result += letter
            first_letter_found = True
        else :
            result += letter

    return result


while True :
    print('Name:')
    name = correct_name(input())
    if name == '' :
        break

    print('Surname:')
    surname = correct_name(input())
    if surname == '' :
        break

    print('Age:')
    age_str = input()
    if age_str == '' :
        break
    age = int(age_str)
    if not is_age_correct(age) :
        print('age %d not correct'%age)
        continue

    print('ID:')
    id_str = input()
    if id_str == '' :
        break
    id = int(id_str)

    if id in total_table :
        print('user with %d already exist'%(id))
    else :
        total_table[id] = (name, surname, age)

print_total_table()