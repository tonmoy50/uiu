import numpy
first_line_input = input()
n,x,y = first_line_input.split(" ")

n = int(n)
x = int(x)
y = int(y)

second_line = input()
array_list = second_line.split(" ")

for i in range(x):

    if y == 0:
        temp = array_list.pop(0)
        array_list.append(temp)
    else:
        temp = array_list.pop()
        array_list.insert(0, temp)

array_list = [int(i) for i in array_list]

print(numpy.array(array_list))
