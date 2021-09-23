import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
import pickle as pkl 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense, Dropout


data = np.genfromtxt("diabetes.csv", delimiter=",")
x = data[ :, :-1 ]
y  = data[ :, -1 ]
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=1)
train_x, valid_x, train_y, valid_y = train_test_split(train_x, train_y, test_size=0.1, random_state=1)

print(valid_y.shape[0])
print(test_y.shape[0])


hyper_param1 = [12,16,24]
hyper_param2 = [30,40,50]

best1 = 12
best2 = 30
score = 0


for ele1 in hyper_param1:
    for ele2 in hyper_param2:
        model = Sequential()
        
        model.add(Dense(ele1, input_dim=x.shape[1], activation="relu" ) )
        model.add( Dropout(0.2) )
        model.add(Dense(ele2, activation="relu" ) )
        
        model.add(Dense(32, activation="relu" ) )
        
        model.add(Dense(12, activation="relu" ) )
        model.add( Dropout(0.5) )
        model.add(Dense(1, activation="sigmoid" ) )
        
        model.compile ( loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"] )
        model.fit(train_x, train_y, epochs=100, batch_size=10, verbose=0)
        print(model.evaluate(valid_x, valid_y)[1] )
        #prediction = model.predict(valid_x)
        prediction = model.predict_classes(valid_x)
        


        temp_score = accuracy_score(valid_y, prediction)
        if temp_score > score:
            score = temp_score
            best1 = ele1
            best2 = ele2

print(best1)
print(best2)
print(score)


print("Success")