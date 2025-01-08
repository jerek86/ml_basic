num = int(input())

while num > 10 :
    temp = num
    new_num = 0
    while temp :
        new_num += temp % 10
        temp //= 10
    num = new_num

print(num)