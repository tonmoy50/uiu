test_case = int(input())

final_brackets = []

for i in range(test_case):

    brackets = input()
    brackets = list(brackets)
    counter = 0
    
    temp_brackets = []
    left = []
    
    i = 0
    flag = 0
    for j in brackets:
        

        if len(left) != 0:
            if j == ")":
                left.pop()
                counter = counter + 1
                flag = 0
            elif j == "(":
                left.append(j)
                flag = 0
        elif len(left) == 0:
            if j == ")":
                brackets.pop(i)
                if flag == 1:
                    counter = 0
            else:
                left.append(j)
    
    final_brackets.append(counter*2)
    i = i + 1

for item in final_brackets:
    print(item)

            

    