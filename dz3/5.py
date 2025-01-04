line = input()

vec = line.split()

symbols_count = len(line)
numeral_count = (line.count('0') + line.count('1') + line.count('2') + line.count('3') + line.count('4') + line.count('5') +
                 line.count('6') + line.count('7')) + line.count('8') + line.count('9')

if symbols_count == numeral_count :
    print('True')
elif symbols_count == numeral_count + 1 :
    dot_count = line.count('.')
    print(dot_count == 1)
else :
    print('False')
