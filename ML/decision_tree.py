# Importing python libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
import math as math

#dataframe = datasets.load_iris()


#X = dataframe.data[:,:2]
#Y = dataframe.target

local_data = np.genfromtxt("data.csv", delimiter=",")

X_local = local_data[:, :19]
Y_local = local_data[:, 19]

train_x, test_x, train_y, test_y = train_test_split(X_local, Y_local, test_size=0.20)

train_size = train_x.shape[0]
test_size = test_x.shape[0]

root = 0

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.80, random_state=42)

#train_size = X_train.shape[0]
#test_size  = X_test.shape[0]

#print(X_local)
#print(test_x.shape[0])


def computing_entropy_for_dataset(): 
    yes = np.count_nonzero(train_x[:, 18] )
    no = train_size - yes
    #print(yes)
    #print(no)

    entropy_S = -( (yes/train_size) * math.log2(yes/train_size) ) - ( (no/train_size) * math.log2(no/train_size) )
    return entropy_S 

def count_yes_for_nodes(i):
    count_zero, count_one = 0, 0
    for iter in range ( train_x.shape[0] ):
        if( train_x[:, i] == 0 and train_y[:, iter] == 0):
            count_zero = count_zero + 1

def choose_root(entropy_S):

    entropy_nodes = list
    for i in range( train_x.shape[1] ):
        unique, counts = np.unique(train_x[: , i], return_counts=True)
        #print(unique,counts)
        save = dict ( zip (unique, counts) )
        entropy_weight = 0
        count_yes_for_nodes(i)
        count_no_for_nodes(i)
        for i in range( len(save) ):
            local_node_entropy = - ( /save[0] ) #CONTINUE FROM HERE




def main():
    #print(local_data)
    #print(type(local_data))

    entropy_all_datas = computing_entropy_for_dataset()
    
    #print(entropy_all_datas)
    choose_root(entropy_all_datas)



if __name__ == "__main__":
    main()