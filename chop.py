import numpy as np


#print("halo")

labels = np.array( [2,2,3] )
counts = np.bincount(labels)

#print ( np.argmax(counts) )


unique, counts = np.unique(labels, return_counts=True)

save = dict ( zip (unique, counts) )

#print(counts)

holder = np.zeros( (2,2) )

holder[0][0] = 1
holder[1][0] = 2

holder[0][0] = holder[0][0] + 1

#print(np.sum(holder[0]))


x = []
print(  len(x) )