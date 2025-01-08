line = str(input())

vec = line.split(',')

string = vec[0]
key = int(vec[1])

result = ''

for sym in string :
    if ord('A') <= ord(sym) <= ord('Z') :
        new_sym = chr(ord(sym) + key)
        if ord(new_sym) > ord('Z') :
            new_sym = chr(ord(new_sym) - ord('Z') + ord('A') - 1)
        result += new_sym
    elif ord('a') <= ord(sym) <= ord('z') :
        new_sym = chr(ord(sym) + key)
        if ord(new_sym) > ord('z') :
            new_sym = chr(ord(new_sym) - ord('z') + ord('a') - 1)
        result += new_sym
    else :
        result += sym

print(string, ',', key, '->', result)