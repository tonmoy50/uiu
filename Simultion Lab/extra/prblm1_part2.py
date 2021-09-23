import numpy as np 
from matplotlib import pyplot as plt





x1=3
val_q=5
bit_of_i=[1,1,1,1,1]
n=500

for i in range(5,n):
  
  if(bit_of_i[i-x1]==bit_of_i[i-val_q]):
    bit_of_i.append(0)
  else:
    bit_of_i.append(1)






l = 4
y = 2**l
vals = []
u = []

for i in range(0,n,l):
  bit_segment = bit_of_i[i:i+l]
  
  str1 = ""
  for j in bit_segment:
    str1 = str1 + str(j)
  
  val=int(str1,2)
  
  vals.append(val)
  u.append(val / y)

print(vals)
print(u)
uni_numbers=set(u)
print(uni_numbers)


plt.figure(figsize=(15,10))
plt.bar(range(0,n,l),u,width=1)

plt.xlabel('Random Number')
plt.ylabel('Iteration')
plt.title('Tausworthe Chart')  
plt.show()