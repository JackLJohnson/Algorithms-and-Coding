'''
Two Sum Problem
'''
import urllib.request as url1
import os
from os import path
import time
import re
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
obj = twosum()
filename = "C://Public//Code//Algorithms-and-Coding//prob-2sum.txt"
if os.path.isfile(filename):
    print(obj.calculate(filename))
else:
    obj.gettingthefile(filename)
