'''
Median Maitainance Problem - Coursera Algorithms course - L3
- Compute the median of running Integers as they come
- O(log i) of the step i
# Use Heaps
    - Use a Low Heap where you put all the smallest elements
    - Use a High Heap where you put all the Largest elements
    - Do rebalancing so that there are equal number of elements on both the heaps
    - The median will be the maximum of the low Heap or the minimum of the high heap
    - check which heap is even and odd
# Use BSTs
# helpers
    - https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
    - http://proserge.kh.ua/coding/index.php
'''

import urllib as url1
import os
from os import path
from collections import defaultdict
import sys, time
from collections import deque
from heapq import heappush, heappop
from heapq_max import *

class MedMain(object):
    """docstring for MedMain."""
    def __init__(self):
        super(MedMain, self).__init__()
        self.median=[]
        self.lowers = []     #max heap
        self.highers = []    #min heap
        self.number = 0

    def gettingthefile(self,path):
        url = "https://d18ky98rnyall9.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt?Expires=1510876800&Signature=YS-XBR7vByuNY18Sa~lbKrzX-h15fKd05uGpjOZVIgztiha0BJHzcZmEm5NiN6iijC32VQ5UzxqK8roflyUWYyZQG9YY2k5SDhAO9X4BswvDpf--XvcbB1Creg5FPN6Hlp4rBw3oNeda-FnaHBztGe2J~e1G-hYxcd4eYFR4M48_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response = url1.urlopen(url)
        data=response.read()
        filename = path
        file = open(filename, "w")
        doc = data.decode('utf-8')
        file.write(doc)
        file.close
    def processdata(self, path):
        fileh=open(path, "r+")
        for line in fileh:
            yield int(line.strip())

    def minheapify(self, h, n, index):
        smallest = index
        l=2*index+1
        r=2*index+1

        if l<n and h[l]<h[index]:
            smallest = l
        if r<n and h[r]<h[smallest]:
            smallest = r

        if smallest!=index:
            h[index], h[smallest] = h[smallest], h[index]
            self.minheapify(h, n, smallest)
        return h[0] #return the root ie, the minimum

    def maxheapify(self, h, n, index):
        largest = index
        l=2*index+1
        r=2*index+1

        if l<n and h[l]>h[index]:
            largest = l
        if r<n and h[r]>h[largest]:
            largest = r

        if largest!=index:
            h[index], h[largest] = h[largest], h[index]
            self.maxheapify(h, n, largest)
        return h[0] #return the root, max

    def calculate(self,filename,calls):
        if os.path.isfile(filename):
            gen = obj.processdata(filename)
            sum=0
            for i in range(calls):
                self.number = next(gen)
                if len(self.lowers)>0:
                    if self.number > -self.lowers[0]:
                        heappush(self.highers,self.number)
                    else:
                        heappush(self.lowers, -self.number)
                else:
                    heappush(self.lowers,-self.number)

                if len(self.lowers)>len(self.highers)+1:
                    heappush(self.highers, -(heappop(self.lowers)))
                elif len(self.highers) > len(self.lowers):
                    heappush(self.lowers, -(heappop(self.highers)))
                sum+= -self.lowers[0]
        return sum%10000

if __name__=="__main__":
    filename = "C:/Public/Code/MedMain/medmain.txt"
    obj = MedMain()
    calls = 10000 #10000 = number of numbers you have
    if os.path.isfile(filename):
        start = time.time()
        print(obj.calculate(filename, calls))
        stop = time.time()
        print("time taken here : {}".format(stop-start))
    else:
        obj.gettingthefile(filename)
