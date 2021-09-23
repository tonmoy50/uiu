gen1 = [[0,0,0,0,0],
        [0,0,1,1,1],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

print(gen1[0][4])

import matplotlib.pyplot as plt 
import numpy as np

x1 = np.linspace(1, 100)
x2 = np.linspace(1, 50)

y1 = pow(x1, 2)
y2 = pow(x2, 2)

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()
