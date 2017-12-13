'''
Two Sum Problem
'''
import urllib.request as url1
import os
from os import path
import time
import re
from heapq import heappop, heappush
import bisect
TLOW = -10000
THIGH= 10000
class twosum(object):
    """docstring for twosum."""
    def __init__(self):
        super(twosum, self).__init__()

    def gettingthefile(self, path):
        url = "https://d18ky98rnyall9.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt?Expires=1513123200&Signature=ZAoRKdXCHCaPbdBN5Iqqpj0IZlZPRIGUJhqgZ3TqQOP-yIiWKJK7wqusGCBG7S3MTm5nnjtrGrVyApVymWJnKgeQ~BWIjS4nF9PI1MeMZMLUmUO1ECwH0QYS0cZpjQZ9jlKZx1mAvA7LxHY~1Wb4Q5JxoT-lGo0G1kMdKniZhEc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response = url1.urlopen(url)
        data = response.read()
        f1 = open(path, 'w')
        values = data.decode('utf-8')
        f1.write(values)
        f1.close

    def calculate(self, path):
        f2  = open(path, 'r+')
        samples = set()
        count=0
        hashtable = {}
        res = set()
        for line in f2:
            samples.add(int(line))
        for x in samples:
            hashtable[x]=True
        print('Size of the hashtable', len(hashtable))

        for t in range(TLOW, THIGH+1):
            for sample in samples:
                y = t-sample
                if y in hashtable and sample != y:
                    res.add((sample,y))
                    break
        return len(res)

    def binsearch(self, arr, item, s, e):
        if e>=s:
            mid=int((s+e)/2)
            if arr[mid]==item:
                return True
            elif arr[mid]>item:
                self.binsearch(arr,item,s,mid-1)
            elif arr[mid]<item:
                self.binsearch(arr,item,mid+1,e)
        else:
            return None

    def calculatef1(self, path):
        f2 = open(path, 'r')
        h=[]
        res = set()
        for line in f2:
            heappush(h, int(line))
        samples = [heappop(h) for i in range(len(h))]
        sizeheap = len(samples)
        print('Size of samples {}'.format(len(samples)))
        for x in samples:
             lower = bisect.bisect_left(samples, TLOW-x)   # index from start of leftmost insertion
             upper = bisect.bisect_right(samples, THIGH-x) # index from start of rightmost insertion
             res |= set([x+y for y in samples[lower:upper]]) # uses the fact that samples is already sorted for lower and uppper are already present
        # for t in range(TLOW, THIGH+1):
        #     for x in samples:
        #         y=t-x
        #         if x!=y:
        #             if self.binsearch(samples,y,0,sizeheap-1):
        #                 res.add((x,y))
        #                 break
        return len(res)

obj = twosum()
filename = "C://Public//Code//Algorithms-and-Coding//prob-2sum.txt"
if os.path.isfile(filename):
    print(obj.calculatef1(filename))
else:
    obj.gettingthefile(filename)
