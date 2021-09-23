import numpy as np

del_xx = 2.0
del_x_ = -1.0
del_xy = -2.0






def optimal_score(mat, s, t):

    score = 0
    align_s = []
    align_t = []
    i = mat.shape[0] - 1
    j = mat.shape[1] - 1
    iter = 0

    while (i >0 ):
        
        #print(score)
        if (i==0 and j > 0):
            index = 1
            val = mat[i][j]
            #j = j - 1
        elif j==0:
            index = 2
            val = mat[i][j]
            #i = i - 1
        else:

            index = max_val(mat, s, t, i, j)[1]
            val = max_val(mat, s, t, i, j)[0]

        #print("i {} j {}".format(i, j))
        #print("Index {} Val {} Iter {}".format(index, val, iter))
        score = score + val
        
        iter = iter + 1

        if val == mat[i][j]:

            if index == 0:
                #score = score + mat[i-1][j-1]
                align_s.append(s[i-1])
                align_t.append(t[j-1])
                i = i-1
                j = j-1
                #print("In diag")
                
            elif index == 1:
                #score = score + mat[i-1][j]
                align_s.append('_')
                align_t.append(t[j-1])
                j = j-1
                #print("In left")
            else:
                #score = score + mat[i][j]
                align_s.append(s[i-1])
                align_t.append('_')
                i = i-1
               

            
    
    align_s.reverse()
    align_t.reverse()
    
    print(*align_s)
    print(*align_t)
    print(score)





def max_val(mat, s, t, i, j):
    
    

    temp_list = []

    
    temp_list.append( mat[i-1][j-1] + (del_xx if (s[i-1] == t[j-1]) else del_xy) )
    temp_list.append( mat[i-1][j] + del_x_ )
    temp_list.append( mat[i][j-1] + del_x_ )

    
    
    sender = [max(temp_list),  temp_list.index(max(temp_list) ) ]
    
    return sender
           


def create_mat(s, t, mat):

    
    for j in range(1, mat.shape[1]):
        mat[0][j] = mat[0][j-1]+del_x_
    
    for i in range(1, mat.shape[0]):
        mat[i][0] = mat[0][i-1]+del_x_

    for i in range(1, mat.shape[0] ):
        for j in range(1, mat.shape[1] ):
            
            mat[i][j] = max_val(mat, s, t, i, j)[0]
            


def main():
    #s = ['A', 'A', 'A', 'C']
    #t = ['A', 'G', 'C']
    
    s = input("Enter String s: ")
    t = input("Enter String t: ")

    s = list(s)
    t = list(t)


    mat = np.zeros( ( len(s)+1, len(t)+1 ) )
    
    
    
    

    create_mat(s, t, mat)
    print(mat)
    
    optimal_score(mat, s, t)



if __name__ == "__main__":
    main()