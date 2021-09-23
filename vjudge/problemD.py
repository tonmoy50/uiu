

def check_prime(vals):
    
    for j in vals:
        if j == 1:
            return 1
        elif j == 2:
            return 1
        
        for i in range(2, j):
            if j % i == 0:
                return 0
        
        return 1
        
            

def main():
    t = int(input())

    for i in range(t):
        name_num = input()
        name, num = name_num.split(" ")
        name = list(name)
        num = int(num)
        #print(name)

        vals = [ ord(i)+num for i in name]
        flag = check_prime(vals)

        if flag == 1:
            print("Yes")
        else:
            print("No")

        
        
    #print(vals)



if __name__ == "__main__":
    main()