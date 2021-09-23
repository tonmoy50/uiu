import numpy as np 



def main():
    m = int( input("Enter value of m: ") )
    a = int ( input("Enter value of a: ") )
    c = int ( input("Enter value of c: ") )
    seed = int ( input("Enter value of seed: ") )
    n = int( input("Enter value of number of random numbers: ") )
    u_of_i = '_'

    temp = seed

    print("i\t Zi\t Ui")
    #temp = ( (a*temp)+c ) % m 
    #u_of_i = temp / m

    print("{}\t {}\t {}".format(0, temp, u_of_i) )


    for i in range(n):
        temp = ( (a*temp)+c ) % m 
        u_of_i = temp / m
        print("{}\t {}\t {}".format(0, temp, u_of_i) )



if __name__ == "__main__":
    main()