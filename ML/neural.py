import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
import pickle as pkl 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense, Dropout



def main():
    data = np.genfromtxt("diabetes.csv", delimiter=",")
    X = data[ : , : -1]
    Y = data[ :, -1]
    train_x, test_x, train_y, test_y = train_test_split(X , Y, test_size=0.2, random_state=1, stratify=Y)

    model = Sequential()
    
    model.add( Dense (10, input_dim=X.shape[1], activation="relu") )
    model.add( Dropout(0.5) )
    model.add( Dense (20,  activation="relu") )
    
    model.add( Dropout(0.5) )
    
    model.add( Dense (30, activation="relu") )
    model.add( Dense (1, activation="sigmoid") )

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"] )
    model.fit(train_x, train_y)
    predict_y = model.predict_classes(test_x)

    print(accuracy_score(predict_y, test_y) )

    




if __name__ == "__main__":
    main()