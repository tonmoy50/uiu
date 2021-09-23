import numpy as np
import pandas as pd
import random as rnd
import math as m
from statistics import mean
from sklearn.model_selection import train_test_split
from sklearn import datasets


iris = datasets.load_iris()
x = iris.data[: , :2]

x_size = x.shape[0]
k = 3
center = np.zeros( (k, 2) )
cluster = np.zeros( (k, x_size) )
distance = np.zeros ( k )

cluster1 = np.array([[0.0 ,0.0 ]])
cluster2 = np.array( [[0.0 ,0.0]] )
cluster3 = np.array( [[0.0,0.0]] )
result = [0]
#cluster1 = [[]]
#cluster2 = [[]]
#cluster3 = [[]]

#mega_cluster = [[[]]]

def centering(k):
    for i in range(k):
        center[i] = rnd.choice(x) 


def calculate_distance(center, cluster_loc):
    #result = np.array([0])
    total = 0
    
    for ele in cluster_loc:
        total += np.sqrt ( np.sum ( np.square( center - ele ) ) )

    #print(total)
    return total


def finding_weight_of_k():
    #print(center)

    result.append(calculate_distance(center[0], cluster1))
    result.append(calculate_distance(center[1], cluster2))
    result.append(calculate_distance(center[2], cluster3))
    #result.append(calculate_distance(center[2], cluster3))

    #print(result/k)


def clustering():
    centering(k)
    flag = 1
    cluster1 = np.array([[0.0 ,0.0 ]])
    cluster2 = np.array( [[0.0 ,0.0]] )
    cluster3 = np.array( [[0.0,0.0]] )
    while flag == 1:
        cluster1 = np.array([[0.0 ,0.0 ]])
        cluster2 = np.array( [[0.0 ,0.0]] )
        cluster3 = np.array( [[0.0,0.0]] )
        for ele in x:
            #cntr1_dist = np.sqrt ( np.sum ( np.square( center[0] - ele ) ) )
            #cntr2_dist = np.sqrt ( np.sum ( np.square( center[1] - ele ) ) )
            #cntr3_dist = np.sqrt ( np.sum ( np.square( center[2] - ele ) ) )
            
            for i in range(k):
                distance[i] =  np.sqrt ( np.sum ( np.square( center[i] - ele ) ) )
            
            min_distance = np.where( distance == np.amin(distance) )
            #print (min_distance)
            index_val = min_distance[0][0]
            aa = ele.tolist()

            #mega_cluster[index_val].append(aa)

            #print(type(aa) )
            if index_val == 0:
                #cluster1.append( ele )
                cluster1 = np.append(cluster1, [ele], axis=0)
                #print("1 ", cluster1, ele)
            elif index_val == 1:
                #cluster2.append( ele )
                cluster2 = np.append(cluster2, [ele], axis=0)
                #print("2")
            else:
                #cluster3.append( ele )
                cluster3 = np.append(cluster3, [ele], axis=0)
                #print("3") 

        new_center1_mean = np.mean(cluster1, axis=0)
        new_center2_mean = np.mean(cluster2, axis=0)
        new_center3_mean = np.mean(cluster3, axis=0)
        
        #print(new_center1_mean)
        

        if ( np.array_equal(new_center1_mean, center[0]) and np.array_equal(new_center2_mean, center[1]) and np.array_equal(new_center3_mean, center[2]) ):
            flag = 0
            center[0] = new_center1_mean
            center[1] = new_center2_mean
            center[2] = new_center3_mean

        else:
            flag = 1
            center[0] = new_center1_mean
            center[1] = new_center2_mean
            center[2] = new_center3_mean

        
        '''print("First Cluster-->",center[0])
        print("Second Cluster-->",center[1])
        print("Third Cluster-->",center[2])'''
        #flag = 0    #print (cntr1_dist)


clustering()
finding_weight_of_k()
some = sum(result)
print(some/k)
#centering(k)

#print(mega_cluster)