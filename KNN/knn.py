
# Importing python libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets


# Loading a dataset named IRIS in dataframe variable
dataframe = datasets.load_iris()





# Slicing the dataset into X and Y where X holds all the features(first 2 columns)
# and Y holds the class column
# Array[Row(from:to-1),Column(from:to-1)]
X = dataframe.data[:,:2]
Y = dataframe.target



# Using train_test_split method from sklearn dividing the X and Y into 
# X_train, X_test, Y_train, Y_test where test case holds 30%(random) of whole dataset 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.80, random_state=42)

#print (Y_test)



# Getting the shapes of X_train and X_test
train_size = X_train.shape[0]
test_size  = X_test.shape[0]




K_Value = 3
# Assigning a predication variable with 0's where all the predicted data 
# will be stored using the algorithm
predictions = np.zeros((test_size,1))
temp_prediction = []

# Variable Scope
distances = [[]]
index_value = []


def get_prediction(index_value, temp_prediction):

    temp_list = []
    for elements in index_value:
        #print ( Y_train[elements] )
        
        temp_list.append( Y_train [elements] )
    
    f0 = temp_list.count(0)
    f1 = temp_list.count(1)
    f2 = temp_list.count(2)

    if f0 > f1 and f0 > f2:
        temp_prediction.append(0)
    elif f1 > f0 and f1 > f2:
        temp_prediction.append(1)
    else:
        temp_prediction.append(2)
        #print (predictions)





def find_neighbour(distances):
    sorted_array = np.argsort(distances)
    #print(sorted_array)
    index_value = []
    for i in range(K_Value):
        #minimum = min( sorted_array )
        index_of_min = np.where( sorted_array == i )
        index_value.append( int(index_of_min[1]) ) 
        #print (index_value)  
    get_prediction(index_value, temp_prediction)
    


def finding_correct_datas_in_Y_test(temp_prediction, Y_test):
    correct_data = []
    for i in range( len(Y_test) ):
        if Y_test[i] == temp_prediction[i] :
            correct_data.append ( Y_test[i] )
    return correct_data

# For loop for test case 
for i in range(test_size) :
    test_data = X_test[i,:]
    # Assigning a distance variable with 0's where all the distance from a test
    # data to all train data will be stored
    distances = np.zeros((1,train_size))
    # For loop for train case
    for j in range(train_size) :
        train_data = X_train[j,:]
        # Get euclidean distance between test_data and train_data
        distances[0,j] = np.sqrt(np.sum((test_data - train_data)**2))
    find_neighbour(distances)                                       #solution of problem1-3
    

#solution of problem4
valo_data = finding_correct_datas_in_Y_test(temp_prediction, Y_test)
print ("Correct datas after comparison: ", valo_data)


#solution of problem5
#accuracy = ( len(valo_data) / test_size ) * 100
print( ( len(valo_data) / test_size ) * 100, "%" )
#print (temp_prediction)
#print (Y_test)   
    
    
    
    
    
    
    ###### Steps #####    
    # 1. Find nearest K neighbors from distances
    # 2. Find the majority class value
    # 3. Fill the prediction array with predicted values based on majority 
    #    class data for each test data
    # 4. Find out the correctly classified data by comparing prediction array 
    #    with test data
    # 5. Find out the accuracy Formula = (number_of_test_instances_correctly_classified/test_size)*100
    




