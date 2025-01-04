line = int(input())

rim = ''

Ms = line // 1000
rim = rim + Ms * 'M'
line = line % 1000

if line >= 900 :
    rim += 'CM'
    line = line - 900

if line >= 500 :
    rim += 'D'
    line = line - 500

if line >= 400 :
    rim += 'CD'
    line = line - 400


Cs = line // 100
rim = rim + Cs * 'C'
line = line % 100

if line >= 90 :
    rim += 'XC'
    line = line - 90

if line >= 50 :
    rim += 'L'
    line = line - 50

if line >= 40 :
    rim += 'XL'
    line = line - 40


Xs = line // 10
rim = rim + Xs * 'X'
line = line % 10

if line >= 9 :
    rim += 'IX'
    line = line - 9

if line >= 5 :
    rim += 'V'
    line = line - 5

if line >= 4 :
    rim += 'IV'
    line = line - 4

rim = rim + line * 'I'

print(rim)