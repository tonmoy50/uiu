
def main():
    test_case = int(input())

    for i in range(test_case):
        vals = input()
        x, y = vals.split(" ")

        x = int(x)
        y = int(y)

        x_list = []
        y_list = []
        sett = x if x>y else y

        for i in range(1, sett+1):

            if x >= i:
                if x % i == 0:
                    x_list.append(i)
            
            if y >= i:
                if y % i == 0:
                    y_list.append(i)
        if ( y == abs(x - sum(x_list)) and x == abs(y - sum(y_list)) ):
            print("Friendship is ideal")
        else:
            print("Friendship is ideal")

    #print(x_list)
    #print(y_list)


if __name__ == "__main__":
    main()