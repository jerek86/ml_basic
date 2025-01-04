line = input()

inp_vec = line.split(',')

width = int(inp_vec[0])
height = int(inp_vec[1])
count = int(inp_vec[2])

print((count % width == 0) | (count % height == 0))