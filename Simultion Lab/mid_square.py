import numpy as np 
from decimal import Decimal



def main():
    gen_num = input("Enter how many random number you want: ")
    seed = input("Enter 4digit Seed number: ")
    gen_num = int(gen_num)
    seed = int(seed)

    temp = seed

    print("i\t Zi\t Ui\t Zi2")
    u_of_i = '_'
    for i in range(gen_num+1):
        
        temp_square = pow(temp, 2)
        temp_val1 = list(map(int, str(temp_square)))
        
        

        if len(temp_val1)<8:
            for j in range( 8-len(temp_val1) ):
                temp_val1.insert(0, '0')

        temp_val1_show = map(str, temp_val1 )
        temp_val1_show = ''.join(temp_val1_show)

        print("{}\t {}\t {}\t {}".format(i, temp, u_of_i, temp_val1_show ) )

        u_of_i = [temp_val1[k] for k in range(2, 6)] #middle 4number from here
        u_of_i.insert(0, '.')
        u_of_i.insert(0, '0')
        u_of_i = map(str, u_of_i)
        u_of_i = ''.join(u_of_i)
        temp = Decimal(u_of_i)
        temp = temp*10000
        temp = int(temp)

        
        
        
        

        


        
        


if __name__ == "__main__":
    main()