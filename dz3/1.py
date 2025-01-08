number = input()

if len(number) == 5 :
    print(number[0] + number[3:0:-1] + number[4])
else :
    print('wrong numbers count: ', len(number))