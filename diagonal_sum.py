import numpy as numpy
import pandas as pd

def make_sum(a, size_of_mat):
    iter,jter = 0,size_of_mat - 1
    total1,total2 = 0,0

    for i in range(size_of_mat):
        if(iter == jter):
            total1 += a[i][iter]
            #total2 += a[i][jter]
            iter += 1
            jter -= 1  
        else:
            total1 += a[i][iter]
            total2 += a[i][jter]
            iter += 1
            jter -= 1
        

    
    return (total1 + total2)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
size_of_mat = len(mat)
print( make_sum(mat, size_of_mat) )
