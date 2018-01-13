'''
QuickSort
1. Ans: 162085
2. Ans:
'''
import urllib.request as url1
import os
import os as path
import sys, time

class Quicksort(object):
    def __init__(self):
        super(Quicksort, self).__init__()
        self.comp=0

    def gettingthefile(self, path):
        url="https://d18ky98rnyall9.cloudfront.net/_32387ba40b36359a38625cbb397eee65_QuickSort.txt?Expires=1515974400&Signature=iJlMaPvLbkQCEewKFyK8w8PcIYGECcVjGp8AikK8kNuZcR3qpZ6~56aSEL7Qa2wAb6dfaM7T1Y~sDKyoc7e6fXMoqkEf0KJ65iAhYXhFgEUHMwvyPkLp6T-ad1amVDYEcpaWLic0dpX8bqUiytN3jNGRMNWFjr6RI8sPlWXuhq4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response=url1.urlopen(url)
        data=response.read()
        filename=path
        file=open(filename, 'w')
        doc=data.decode('utf-8')
        file.write(doc)
        file.close

    def processdata(self, path):
        fileh=open(path,"r+")
        res = [int(line.strip()) for line in fileh if line.strip()!='']
        return res

    def qsort(self, arr, l, r):
        if l<r:
            q=self.partition(arr,l,r)
            self.qsort(arr,l,q-1)
            self.qsort(arr,q+1,r)


    def partition(self,arr,l,r):
        #self.comp+=len(arr)-1
        #print("comp",self.comp)
        i,p=l+1,arr[l]
        for j in range(l+1,r+1):
            self.comp+=1
            if arr[j]<p:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        arr[l],arr[i-1]=arr[i-1],arr[l]
        print(self.comp)
        return i-1

    def partition_r(self,arr,l,r):
        #self.comp+=len(arr)-1
        #print("comp",self.comp)
        i,p=l-1,arr[r]
        for j in range(l,r):
            self.comp+=1
            if arr[j]<p:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[r],arr[i+1]=arr[i+1],arr[r]
        print(self.comp)
        return i+1

    def partition2(self,arr,l,r):
        #self.comp+=len(arr)-1
        #print("comp",self.comp)
        i,p=l+1,arr[l]
        for j in range(l+1,r+1):
            self.comp+=1
            if arr[j]<p:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        arr[l],arr[i-1]=arr[i-1],arr[l]
        print(self.comp)
        return i-1

if __name__=="__main__":
    filename = "C:/Public/Code/testcases/QuickSort.txt"
    obj=Quicksort()
    if os.path.isfile(filename):
        #res=obj.processdata(filename)
        res=[3,9,8,4,6,10,2,5,7,1]
        #print(res[0:10],len(res))
        start=time.time()
        print(obj.qsort(res,0,len(res)-1))
        stop=time.time()
        print(res)
        print("Time taken by the program : {}".format(stop-start))
    else:
        obj.gettingthefile(filename)
