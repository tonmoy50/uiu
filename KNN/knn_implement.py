def plot_data():
    """
        A function to plot the data
    """
    data_sets_file = open("data_set.txt", "r")

    plotted_datas = []
    nirvejal_list = []

    for lines in data_sets_file:
        new_line = lines
        temp_lst = new_line.split(' ')
        nirvejal_list = list( map( lambda x: int(x), temp_lst ) )
        plotted_datas.append(nirvejal_list)
    data_sets_file.close()
    return plotted_datas

def _knn_():
    x = int( input ("Enter Characteristic X: ") )
    y = int( input ("Enter Characteristic Y: ") )
    a = abs(x - radius)
    b = abs(y - radius)
    
    test_lst = []
    predict_list = []
    gotdata = 0

    if data_sets[x][y] != 2:
        return data_sets[x][y]
    else:
        for i in range(radius):
            try:
                #predict_list.append(data_sets[x + 10][y + 10])
                #predict_list.append( data_sets )
                predict_list.append( data_sets[x + 1][y] )
                predict_list.append( data_sets[x - 1][y] )
                predict_list.append( data_sets[x][y + 1] )
                predict_list.append( data_sets[x][y - 1] )                
            except IndexError:
                predict_list.append(-1)
        
        return predict_list







    #print (*data_sets)




data_sets = plot_data()
row = len(data_sets)
column = len(data_sets[0])


#temp_list = [ i for i in data_sets[2] ]
#print(predict_list)

radius = 2
result_set = _knn_()

print(result_set)

if type(result_set) is int:
    print ("The predicted data is: {}".format(result_set) )
else:
    male = result_set.count(1)
    female = result_set.count(0)

    if male > female:
        print ("The predicted data is 1")
    else:
         print ("The predicted data is 0")




#print(data_sets[11][12])

