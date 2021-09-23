import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import svm
from sklearn.metrics import accuracy_score


def main():
    data = np.genfromtxt("perceptron_data.csv", delimiter=",", skip_header=1)
    #print(data.shape[0])
    X = data[:, :-1]
    Y = data[:, -1]

    train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.1, random_state=1, stratify=Y)

    model = svm.SVC(kernel="rbf", C=100, gamma=0.1)
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)

    print("Accuracy Score: ", accuracy_score(predict_y, test_y) )
    



if __name__ == "__main__":
    main()