# -*- coding: utf-8 -*-
"""Do code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ARiHMC7LroXk9NDwAgy81-CcHO09jk3b
"""

import math

def mean(arr , n):
  print( arr )
  sum=0
  for i in arr:
    sum += i
    
  res = round(sum/n,1)
  print("means:" , res)

def median(arr , n):
  arr.sort()
  #print(arr)
  if (n%2 != 0):
    a = math.floor(n/2)
    mid = round(arr[a],1)
    print(mid)
    
  else:
    high = math.ceil(n/2)
    low = high-1
    
    mid = round((arr[high]+arr[low])/2,1)
    
    print(mid)

def mode(arr , n ):
  arr.sort()
  print("sorted",arr)
  maxnum = 0
  count =0
  l = len(arr)
  
  for i in range(l):
    flag = 0
    j=i
    while (j <= i-l-1):
      if (arr[i] == arr[j]):
        flag += 1
      j +=1
    if flag > count:
      count = flag
      maxnum = arr[i]
    
  if (count == 0):
    print(arr[0])
  else:
    print(maxnum)

def main():
  
  arr = list()
  n = int( input() )
  
  for i in range(int(n)):
    arr.append( input() )
  #n = 10
  #arr = [64630 ,11735 ,14216 ,99233 ,14470 ,4978 ,73429 ,38120 ,51135 ,67060]
  
  print( arr )
  


  #mean(arr , n)
  
  #median(arr , n)
  
  #mode(arr , n)

if __name__ == '__main__':
  main()
