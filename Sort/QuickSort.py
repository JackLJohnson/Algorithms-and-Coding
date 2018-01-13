'''
QuickSort
1. Ans: 162085
2. Ans: 164123
3. Ans: 138382

first middle final
if array is of odd length, it is the middle length
if array of length 2k use the kth element
EXAMPLE:
For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements;
since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element
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
            q=self.partitionrand(arr,l,r)
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

    def getpivot(self,arr,l,r):
        k=len(arr)
        m=0 if (r-l)==1 else int((r-l)/2)+l
        f,l,mid=arr[l],arr[r],arr[m]
        #else:f,l,mid=arr[l],arr[r],arr[int((r-l)/2)-1]
        res=[f,mid,l]
        idx=res.index(sorted(res)[1])
        return idx

    def getpivotmod(self,arr,l,r):
        m=0 if (r-l)==1 else int((r-l)/2)+l
        M,L,R=arr[m],arr[l],arr[r]
        return sorted([(L,l), (M,m), (R,r)])[1][1]

    def partition_r(self,arr,l,r):
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
        arr[l],arr[r]=arr[r],arr[l]
        i,p=l+1,arr[l]
        for j in range(l+1,r+1):
            self.comp+=1
            if arr[j]<=p:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        arr[l],arr[i-1]=arr[i-1],arr[l]
        print(self.comp)
        return i-1

    def partitionrand(self,arr,l,r):
        idx=self.getpivotmod(arr,l,r)
        p=arr[idx]
        arr[l],arr[idx]=arr[idx],arr[l]
        #print(pval,idx)
        # if idx==2:arr[l],arr[r]=arr[r],arr[l]
        # if idx==1:
        #     length=len(arr)
        #     if length%2!=0:arr[l],arr[int(length/2)]=arr[int(length/2)],arr[l]
        #     else: arr[l],arr[int(length/2)-1]=arr[int(length/2)-1],arr[l]
        i=l+1
        for j in range(l+1,r+1):
            self.comp+=1
            if arr[j]<=p:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        arr[l],arr[i-1]=arr[i-1],arr[l]
        print(self.comp)
        return i-1

if __name__=="__main__":
    filename = "C:/Public/Code/testcases/QuickSort.txt"
    obj=Quicksort()
    if os.path.isfile(filename):
        res=obj.processdata(filename)
        #res=[13,9,8,15,4,6,10,2,5,7,14,12,11,1,3]
        #print(res[0:10],len(res))
        start=time.time()
        print(obj.qsort(res,0,len(res)-1))
        stop=time.time()
        print(res)
        print("Time taken by the program : {}".format(stop-start))
    else:
        obj.gettingthefile(filename)
