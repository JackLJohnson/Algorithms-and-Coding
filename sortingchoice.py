'''
@author: Sandeep Anand
Code is to choose what type of sort is the best

- Given a n dimensional array
- There are a total of [n/k] number of sublists
- Each sublist is of length k
- To use both Mergesort and Insertion sort to find out which one is the best and at what point k
- Find the time it take to run each function
'''
import re
import numpy as np
import random

def returncase(*args):
    for val in args:
        return choicedict[val]

## Insertion Sort
def insertionsort(A, p, r):
    if p<r:
        length = r-p+1
        for val in range(1,length-1):
            key = A[val]
            j = val-1
            while (j>=p and A[j]>key):
                A[j+1] = A[j]
                j = j-1
            j = j+1
            A[j] = key
    else:
        retun -1

## Merge
def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q    ## go from q+1 to r

    L=[]
    R=[]

    for val in range(0,n1):
        L.append(A[p+val])

    for val in range(0,n2):
        R.append(A[q+val+1])

    i=0
    j=0
    counter_array=0

    for val in range(p,r+1):
        if (i<=n1 and j<=n2):
            if (L[i] < R[j]):
                A[val] = L[i]
                i=i+1
            else:
                A[val] = R[j]
                j=j+1
            counter_array = counter_array+1

    ## dump up the rest of array that is left to be traversed
    if (i<=n1):
        for k in range(0, n1-counter_array+1):
            A[counter_array+k] = L[i+k]

    if (j<=n2):
        for l in range(0, n2-counter_array+1):
            A[counter_array+l] = L[j+l]

def Mergesort(A, p, r):
    if(p<r):
        q = int((p+r)/2)
        Mergesort(A,p,q)
        Mergesort(A,q+1,r)

        merge(A, p, q, r)

def mixedsort(A, p, r):
    if (p == r):
        return
    elif p<r:
        if (r-p) < 20:
            insertionsort(A,p,r)
        else:
            q = int((p+r)/2)
            mixedsort(A,p,q)
            mixedsort(A,q+1,r)

            merge(A,p,q,r)  ## Merge to be done the usual way

class efficientsorting(object):
    """docstring for efficientsorting."""
    def __init__(self):
        super(efficientsorting, self).__init__()
        size = input("Please input the array of size now : \n")
        print("The size of the array is {} \n".format(size))
        array = [random.randint(1,100) for x in range(int(size))]
        #array = [int(x) for x in input().split()]
        print("Original Array used :", array)
        ch = int(input("Enter the choice for the sort you want to do: 0->insertionsort, 1->Mergesort, 2->mixedsort \n"))
        #choicedict = {0:insertionsort(array, 0, int(size)), 1:Mergesort(array, 0, int(size)), 2:mixedsort(array, 0, int(size))}
        if ch in [0,1,2]:
            if ch==0:
                insertionsort(array, 0, int(size))
            elif ch==1:
                Mergesort(array, 0, int(size))
            else:
                mixedsort(array, 0, int(size))
        else:
            return -1
        #insertionsort(array, 0, 7)
        print("The sorted array: ",array)

x = efficientsorting()
