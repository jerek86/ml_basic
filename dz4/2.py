vec = [[0,1,1,0], [1, 0, 0, 0], [0,1,0,1]]
count = 2

result = -1

for row_num in range(len(vec)) :
    free_places = 0
    for place in vec[row_num] :
        if place == 0 :
            free_places += 1
            if free_places >= count :
                result = row_num
                break
        else :
            free_places = 0
    if result >= 0 :
        break
else :
    result = False

print(vec, ', ', count, ' -> ', result)