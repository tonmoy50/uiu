test_case = int(input())

final_array_container = []

for i in range(test_case):
    
    first_line_input = input()
    n,x = first_line_input.split(" ")
    n = int(n)
    x = int(x)
    x = x - 1

    list_to_reverser = input()
    list_to_reverse = list_to_reverser.split(" ")
    
    popped_val = list_to_reverse.pop(x)
    list_to_reverse.reverse()
    list_to_reverse.insert(x, popped_val)
    
    final_array_container.append(list_to_reverse)
    #del list_to_reverse

for item in final_array_container:
    print(*item)