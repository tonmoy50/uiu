#First Generator
z_val1= [12,7]
u_val1= []
m1=16
n= 1000

for i in range(2,n):
  new_z = ((13 * z_val1 [i-1]) + (11 * z_val1 [i-2]) + 3) % m1
  z_val1.append(new_z)
  new_u = new_z / m1
  u_val1.append(new_u)

#Second Generator

z_val2= [3,5]
u_val2= []
m2=17

for i in range(2,n):
  new_z2 = ((12 * z_val2 [i-1]**2) + (13 * z_val2 [i-2])) % m2
  z_val2.append(new_z2)
  new_u2 = new_z2 / m2
  u_val2.append(new_u2)

##Third Generator

z_val3= [2,7]
u_val3= []
m3=15

for i in range(2,n):
  new_z3 = (z_val3 [i-1]**3 + z_val3 [i-2] ** 2) % m3
  z_val3.append(new_z3)
  new_u3 = new_z3 / m3
  u_val3.append(new_u3)

#Generate Random Number

u = []

for i in range(0,n-2):
  combined_u = u_val1[i] + u_val2[i] + u_val2[i]
  new_u = combined_u - int(combined_u)
  u.append(new_u)

print(u_val1)
print(u_val2)
print(u_val3)

print(u)

#Histogram

from matplotlib import pyplot as plt

plt.figure(figsize=(15,10)) 
plt.bar(range(0,n-2),u,width=0.5)

plt.xlabel('Random Number')
plt.ylabel('Iterations')
plt.title('Congruential Chart')
plt.show()