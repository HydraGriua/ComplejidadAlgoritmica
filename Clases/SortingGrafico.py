import numpy as np
import random
import time
from matplotlib import pyplot as plt

# Bubble sort   
def bubbleSort(v): 
    n = len(v)  
    for i in range(n): 
        for j in range(0, n-i-1): 
            if v[j] > v[j+1] : 
                v[j], v[j+1] = v[j+1], v[j]     


# Insertion sort
def insertionSort(v):

    for step in range(1, len(v)):
        key = v[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<v[j] to key>v[j].        
        while j >= 0 and key < v[j]:
            v[j + 1] = v[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        v[j + 1] = key


# Selection sort
def selectionSort(v):
   
    for step in range(len(v)-1):
        min_idx = step
        for i in range(step + 1, len(v)-1):
            if v[i] < v[min_idx]:
                min_idx = i
        (v[step], v[min_idx]) = (v[min_idx], v[step])


# Quick sort
def quickSort(v):
   quickSortHelper(v,0,len(v)-1)

def quickSortHelper(v,first,last):
   if first<last:

       splitpoint = partition(v,first,last)

       quickSortHelper(v,first,splitpoint-1)
       quickSortHelper(v,splitpoint+1,last)

def partition(v,first,last):
   pivotvalue = v[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and v[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while v[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = v[leftmark]
           v[leftmark] = v[rightmark]
           v[rightmark] = temp

   temp = v[first]
   v[first] = v[rightmark]
   v[rightmark] = temp
   return rightmark


# Merge sort
def Mergesort(v):
    if len(v)>1:
        piv = len(v)//2
        l = v[:piv]
        r = v[piv:]
        Mergesort(l)
        Mergesort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                v[k] = l[i]
                i+=1
            else:
                v[k] = r[j]
                j +=1
            k += 1
    
        while i < len(l):
            v[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            v[k] = r[j]
            j += 1
            k += 1


# Heap Sort            
def heapify(v, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      if l < n and v[i] < v[l]:
          largest = l
      if r < n and v[largest] < v[r]:
          largest = r
      if largest != i:
          v[i], v[largest] = v[largest], v[i]
          heapify(v, n, largest) 
def Heapsort(v):
      n = len(v)
      for i in range(n//2, -1, -1):
          heapify(v, n, i)
      for i in range(n-1, 0, -1):
          v[i], v[0] = v[0], v[i]
          heapify(v, i, 0)


#Medir el tiempo
def measure_time(sorting_alg, v,X):
  start = time.time()
  sorting_alg(v)
  end = time.time()
  t=end-start
  X.append(t)


#Generar vectores
def GenVec():
  x = random.sample(range(1000001),5)
  y = random.sample(range(1000001),10)
  z = random.sample(range(1000001),50)
  w = random.sample(range(1000001),100)
  q = random.sample(range(1000001),250)
  p = random.sample(range(1000001),500)
  r = random.sample(range(1000001),800)
  #t = random.sample(range(1000001),10000)
  #u = random.sample(range(1000001),100000)
  #c = random.sample(range(1000001),1000000)
  A = [x,y,z,w,q,p,r]#,t,u,c]
  return A

A = GenVec()

Bubble = []
Insertion = []
Selection = []
Merge = []
Quick = []
Heap = []

B = A.copy()
for i in B:
  measure_time(Mergesort, i,Merge)
B = A.copy()
for i in B:
  measure_time(insertionSort, i,Insertion)
B =A.copy()
for i in B:
  measure_time(bubbleSort, i,Bubble)
B = A.copy()
for i in B:
  measure_time(quickSort, i,Quick)
B = A.copy()
for i in B:
  measure_time(selectionSort, i,Selection)
B = A.copy()
for i in B:
  measure_time(Heapsort, i,Heap)




#X: elementos en el arr
arr = [5, 10, 50, 100, 250, 500, 800]#, 10000, 100000, 1000000]


#Lineas 
plt.plot(arr,Bubble)
plt.plot(arr,Insertion)
plt.plot(arr,Selection)
plt.plot(arr,Merge)
plt.plot(arr,Quick)
plt.plot(arr,Heap)

#Labels
plt.legend(['Bubble','Insertion','Selection','Merge','Quick','Heap'])
plt.xlabel("tiempo")
plt.ylabel("Elementos en el arr")
plt.title("Medicion de tiempos algoritmos de ordenamiento")

#ventana
plt.show()