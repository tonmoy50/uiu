from sklearn import tree
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron



def ann(X, x_train, x_test, y_train, y_test):
    base_model = Sequential()

    base_model.add( Dense(50, input_dim = X.shape[1], activation='tanh' ) )
    
    base_model.add( Dense(40, activation='tanh') )
    #base_model.add( Dropout(0.5) )
    base_model.add( Dense(30, activation='tanh') )
    #base_model.add( Dropout(0.5) )
    base_model.add( Dense(20, activation='tanh') )
    base_model.add( Dense(10, activation='tanh') )

    base_model.add( Dense(1, activation='sigmoid') )

    base_model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

    base_model.fit(x_train, y_train)

    predicts = base_model.predict_classes(x_test)

    #print("ANN - ",  accuracy_score(predicts, y_test) )
    return predicts

def Decision_Tree(x_train, x_test, y_train, y_test):
    tree_obj = tree.DecisionTreeClassifier()
    tree_obj.fit(x_train, y_train)
    y_predict = tree_obj.predict(x_test)

    #print('DTree - ', accuracy_score(y_predict, y_test))
    return y_predict

def Svm_classifier(x_train, x_test, y_train, y_test):
    svm_obj = svm.SVC()
    svm_obj.fit(x_train, y_train)
    prediction = svm_obj.predict(x_test)

    #print('SVM - ', accuracy_score(prediction, y_test))
    return prediction

def nv_bayes(x_train, x_test, y_train, y_test):

    nv = GaussianNB()
    nv.fit(x_train, y_train)
    prediction = nv.predict(x_test)

    #print('NV - ', accuracy_score(prediction, y_test))
    return prediction

def percept(x_train, x_test, y_train, y_test):
    nv = Perceptron()
    nv.fit(x_train, y_train)
    prediction = nv.predict(x_test)

    #print('NV - ', accuracy_score(prediction, y_test))
    return prediction

def voting(a, b, c):

    ensemble_pred = []
    for i in range(a.shape[0]):
        temp = []
        temp.append(a[i])
        temp.append(b[i])
        temp.append(c[i])
        #temp.append(d[i])

        if(temp.count(1) >= temp.count(0)):
            ensemble_pred.append(1)
        else:
            ensemble_pred.append(0)
    
    #print(ensemble_pred)
    return ensemble_pred
        



def main():
    #data = np.genfromtxt("heart.csv", skip_header=1, delimiter=',')
    data = pd.read_csv('heart_c.csv')
    #print(data)
    data = np.array(data)
    X = data[:, :-1]
    Y = data[:, -1]
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, stratify = Y, random_state=1)

    #ann(X, x_train, x_test, y_train, y_test)
    print( "Decision Tree: ",accuracy_score(Decision_Tree(x_train, x_test, y_train, y_test), y_test ) )
    #Svm_classifier(x_train, x_test, y_train, y_test)
    print("Naive Bayes: ", accuracy_score( nv_bayes(x_train, x_test, y_train, y_test) , y_test))
    
    print("Perceptron: ", accuracy_score(percept(x_train, x_test, y_train, y_test), y_test ) )

    #predicted_value = voting( ann(X, x_train, x_test, y_train, y_test), Decision_Tree(x_train, x_test, y_train, y_test), Svm_classifier(x_train, x_test, y_train, y_test), nv_bayes(x_train, x_test, y_train, y_test) )
    predicted_value = voting( Decision_Tree(x_train, x_test, y_train, y_test), Svm_classifier(x_train, x_test, y_train, y_test), nv_bayes(x_train, x_test, y_train, y_test) )

    print( "Ensemble: ",accuracy_score(predicted_value, y_test) )

if __name__ == "__main__":
    main()