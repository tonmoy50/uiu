import numpy as np
import math

import random 


if __name__ == '__main__':
    counter = 0 
    size = 5
    gen  = 20

    gen1 = [[0,1,0,0,0],
            [0,0,1,0,0],
            [0,1,1,0,1],
            [0,1,0,0,1],
            [0,0,0,0,0]]
    
    gen1 = np.array(gen1)
    print("Time 0")
    print(gen1)

    gen_n = np.zeros((size,size))
    #print(gen_n)
    k1 = 0
    k2 = 0

    for it in range(gen):

        for i in range(size):
            for j in range(size):
                k1 = i
                k2 = j
                flag = 0
                counter = 0

                for l in range(8):
                    if l == 1:
                        k1 = i - 1
                        k2 = j - 1                                      
                    elif l <= 3:
                        k2 = k2+1
                    elif l > 3 and l <= 5:
                        k1 = k1 + 1
                    elif l < 8:
                        k2 = k2 - 1
                    else:
                        k1 = k1 - 1 
                    
                    if (k1 > 0 and k1 < size) and (k2 > 0 and k2 < size):
                        
                        if gen1[k1][k2] == 1:
                            counter = counter + 1

                if gen1[i][j] == 0:

                    
                    if counter == 3:
                        gen_n[i][j] = 1

                else:
                    if counter < 2:
                        gen_n[i][j] = 0
                    elif counter == 2 or counter == 3:
                        gen_n[i][j] = 1
                    elif counter > 3:
                        gen_n[i][j] = 0

        print("Time: ", it+1)     
        print(gen_n)
        gen1 = gen_n


   


