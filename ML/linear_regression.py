import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error 
dataframe = datasets.load_diabetes(return_X_y=False)
X = dataframe.data[:,:]
Y = dataframe.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.30, random_state=42)
train_size = X_train.shape[0]
test_size  = X_test.shape[0]
features = X_train.shape[1]

#predictions = np.zeros((test_size,1))
W = np.zeros((features, 1))
print (W.shape[0], W.shape[1])
b = 0
alpha = 0.01
epochs = 100
n = features
m = X_train.shape[0]

trans_X = np.transpose(X_train)
error_list = []

#print(predictions)

def linear_regression(b):

    for i in range(epochs):
        predictions = np.dot(X_train, W) + b
        #print (predictions)
        error_grad = predictions[:, 0] - Y_train
        error_grad = error_grad.reshape(-1, 1)
        #print(error_grad.shape[0], error_grad.shape[1])
        #print (error_grad.shape[0], error_grad.shape[1])
        b = b - ( alpha * sum(error_grad) )
        
        for j in range(n):
            W[j] = W[j] - alpha * sum( (error_grad[:, 0] * X_train[:, j] ) )
        
        error = np.sum( ( error_grad )**2 )
        error_list.append(error)
        #print(error) 
        
        
        
        #print (error_grad)
        #print ("fbwjdbfjkff")

linear_regression(b)
#print(error_list)
Z = 1 / ( 1 + np.exp( - ( X_test.dot( W ) + b ) ) )         
predicted_val = np.where( Z > 0.5, 1, 0 )
print(predicted_val)

real_val = list(Y_test)
correct = 0
for i in range(len(predicted_val)):
    if real_val[i] == predicted_val[i]:
        correct = correct + 1
acc = correct / len(predicted_val)
print(acc)








