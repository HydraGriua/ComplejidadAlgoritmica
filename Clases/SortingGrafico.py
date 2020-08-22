import random
import time
from matplotlib import pyplot as plt

# Bubble sort   
def Bubblesort(v): 
  n, intercambia, x = len(v), True, -1
  while intercambia:
    intercambia, x = False, x + 1
    for i in range(1, n-x):
      if v[i-1] > v[i]:
        v[i-1], v[i] = v[i], v[i-1]
        intercambia = True   


# Insertion sort
def Insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1] = key


# Selection sort
def Selectionsort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min],arr[i]


# Quick sort
def Quicksort(v):
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
  r = random.sample(range(1000001),1000)
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
C = A.copy() 
D = A.copy() 
E = A.copy() 
F = A.copy() 
G = A.copy() 
for i in B:
  measure_time(Mergesort, i,Merge)
for i in C:
  measure_time(Insertionsort, i,Insertion)
for i in D:
  measure_time(Bubblesort, i,Bubble)
for i in E:
  measure_time(Quicksort, i,Quick)
for i in F:
  measure_time(Selectionsort, i,Selection)
for i in G:
  measure_time(Heapsort, i,Heap)




#X: elementos en el arr
arr = [5, 10, 50, 100, 250, 500, 1000]#, 10000, 100000, 1000000]


# Lineas 
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