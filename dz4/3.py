line = 'aaabbbbccccc'

result = str()

last_symbol = line[0]
symbol_count = 0

for current_symbol in line :
    if last_symbol == current_symbol :
        symbol_count += 1
    else :
        result += str(symbol_count)
        result += last_symbol
        last_symbol = current_symbol
        symbol_count = 1

result += str(symbol_count)
result += last_symbol

print(line, '->', result)