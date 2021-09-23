import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score


def get_featurewise_target(train, index_num, value, k, target_class):

    ret_list = []
    temp_data = train.copy()
    train_array = temp_data.iloc[:, index_num].to_numpy()

    #print(index_num, value)

    for i in range(k):

        min_index = np.abs(train_array - value).argmin()
        #print("Min: ", min_index)
        train_array[min_index] = sys.maxsize
        #print(train_array)
        ret_list.append( train[target_class].iloc[min_index] )
        
        #print(target_value)
    
    del temp_data
    del train_array
    #print("Ret List ", ret_list)
    
    return ret_list





    


def main():

    dataset_name = "heart.csv"
    target_col_name = "target"
    k = 10
    test_size = 0.3

    data = pd.read_csv(dataset_name)
    #print(data.head())
    print(data.columns)
    print(data.shape)
    num_of_rows = data.shape[0]
    num_of_columns = data.shape[1]
    
    train,test = train_test_split(data, test_size=test_size, random_state=0)
    #print(train[target_class].iloc[index_num])
    print(train.head)
    
    real_val = test[target_col_name]
    real_val = real_val.to_list()
    test.drop(columns=target_col_name, inplace=True)

    test = test.to_numpy()
    
    predicted_list = []

    for row in test:
        #print(row)
        row_prediction_list = []
        for i in range(row.shape[0]):
            featurewise_list = get_featurewise_target(train, i, row[i], k, target_col_name)
            #print(featurewise_list)
            row_prediction_list.append( max( set(featurewise_list), key=featurewise_list.count ) )
                    
        predicted_list.append( max( set(row_prediction_list), key=row_prediction_list.count ) )
        #print(row_prediction_list)
        
    print(predicted_list)

    acc = balanced_accuracy_score(real_val, predicted_list)
    print(acc)



if __name__ == '__main__':
    main()
