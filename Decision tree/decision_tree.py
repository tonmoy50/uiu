import numpy as np
import math
import random
import msvcrt as m
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from collections import Counter

class Node:
    def __init__(self, attribute=None, attribute_values=None, child_nodes=None, decision=None):
        self.attribute = attribute
        self.attribute_values = attribute_values
        self.child_nodes = child_nodes
        self.decision = decision


class DecisionTree:

    root = None

    @staticmethod
    def plurality_values(data):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        yes = np.count_nonzero(labels)
        no = labels.shape[0] - yes
        if yes < no:
            return 1
        else:
            return 0
        
        
        
        #new_label = labels.astype(int)
        #counts = np.bincount( int(new_label) )
        #return np.argmax(counts)


    @staticmethod
    def all_zero(data):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        
        count = np.count_nonzero(labels)

        if count >= 1:
            return False

        else:
            return True

    @staticmethod
    def all_one(data):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        label_size = labels.shape[0]

        count = np.count_nonzero(labels)

        if count < label_size:
            return False

        else:
            return True




    @staticmethod
    def importance(data, attributes):
        labels = data[:, data.shape[1] - 1]  # store the last column in labels
        #print(labels)
        yes = np.count_nonzero(labels)
        no = labels.shape[0] - yes
        
        prev_info_gain = -1
        best_attribute = attributes[0]


        entropy_parent = yes / (labels.shape[0])

        
        for i in range( len(attributes) ):
            sum = 0.0
            
            unique, counts = np.unique( data[ :, i ]  , return_counts=True)
            save = dict ( zip (unique, counts) )

            holder = np.zeros( ( len(unique) , 2 ) )

            for j in range( len(data[ : , data.shape[1] - 1]) ):
                if j == 0:
                    #if data[ j , : ] == unique[0]:
                    #   holder[0][0] = holder[0][0] + 1
                    for k in range( len(unique) ):
                        if data[j][data.shape[1]-1] == unique[k]:
                            holder[k][0] = holder[k][0] + 1    
                else:
                    for k in range( len(unique) ):
                        if data[j][data.shape[1]-1] == unique[k]:
                            holder[k][1] = holder[k][1] + 1
                
            
            for l in holder:
                if l[1] == 0 and l[0] != 0:
                    sum = - ( l[0] * math.log2( l[0] ) ) + sum
                elif l[0] == 0 and l[1] != 0:
                    sum = - ( l[1] * math.log2( l[1] ) ) + sum
                elif l[0] == 0 and l[1] == 0:
                    sum = sum + 0.0
                else:
                    sum = - ( l[0] * math.log2( l[0] ) ) - ( l[1] * math.log2( l[1] ) ) + sum





            info_gain = entropy_parent - sum
                
            if info_gain > prev_info_gain:
                best_attribute = attributes[i]
                prev_info_gain = info_gain
            
        return best_attribute



    def train(self, data, attributes, parent_data):
        data = np.array(data)
        parent_data = np.array(parent_data)
        attributes = list(attributes)

        if data.shape[0] == 0:  # if x is empty
            return Node(decision=self.plurality_values(parent_data))

        elif self.all_zero(data):
            return Node(decision=0)

        elif self.all_one(data):
            return Node(decision=1)

        elif len(attributes) == 0:
            return Node(decision=self.plurality_values(data))

        else:
            a = self.importance(data, attributes)
            tree = Node(attribute=a, attribute_values=np.unique(data[:, a]), child_nodes=[])
            attributes.remove(a)
            for vk in np.unique(data[:, a]):
                new_data = data[data[:, a] == vk, :]
                subtree = self.train(new_data, attributes, data)
                tree.child_nodes.append(subtree)

            return tree

    def fit(self, data):
        self.root = self.train(data, list(range(data.shape[1] - 1)), np.array([]))

    def predict(self, data):
        predictions = []
        for i in range(data.shape[0]):
            current_node = self.root
            while True:
                if current_node.decision is None:
                    current_attribute = current_node.attribute
                    current_attribute_value = data[i, current_attribute]
                    if current_attribute_value not in current_node.attribute_values:
                        predictions.append(random.randint(0, 1))
                        break
                    idx = list(current_node.attribute_values).index(current_attribute_value)

                    current_node = current_node.child_nodes[idx]
                else:
                    predictions.append(current_node.decision)
                    break

        return predictions



def scikit_learn_results(X_train, X_test, Y_train, Y_test):
    clf = DecisionTreeClassifier(criterion="entropy")

    clf = clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)

    accu = metrics.accuracy_score( Y_test, y_pred ) * 100

    #print( "Accuracy", accu, "%" )


def prediction_test(nijer_prediction, Y_test):
    #print(nijer_prediction) 
    accu = metrics.accuracy_score( Y_test, nijer_prediction )
    return accu


def main():
    #data = np.genfromtxt("data.csv", delimiter=",")
    data = np.genfromtxt("heart_c.csv", delimiter=",", skip_header=1)
    #print(data)

    features = data.shape[1] - 1
    
    X = data[:, :data.shape[1] - 1]
    Y = data[:, data.shape[1] - 1]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    N = X_train.shape[1]

    scikit_learn_results(X_train, X_test, Y_train, Y_test)

    amaar_tree = DecisionTree()
    
    #notun_data = np.stack(X_train, Y_train)
    #print( type(notun_data) )
    
    notun_data, baki_data = train_test_split(data, test_size=0.2, random_state=0)
        
    amaar_tree.fit(notun_data)
    nijer_prediction = amaar_tree.predict(baki_data)

    valo_data = prediction_test(nijer_prediction, Y_test)
    accu = ( valo_data / X_test.shape[0] ) * 100

    print ( "Local Accuracy = ", valo_data * 100, "%" )
    print("Press any key to exit.....")
    m.getch()
    



if __name__ == "__main__":
    main()