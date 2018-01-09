'''
Count Inversions in a list using MergeSort
uses O(nlogn)
- Make changes to extract the file
'''
import urllib.request as url1
import os
import os as path
import sys, time
class Inv(object):
    def __init__(self):
        #self.count=0
        super(Inv, self).__init__()

    def gettingthefile(self, path):
        url="https://d18ky98rnyall9.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1515628800&Signature=VX2b9Uv6QVW7D6bZiByze31cafKMt7rlQ0Bratmhm63GPttKXXLzXFh83E9I4a8E4R1CgoU~863Xyl7Rx55jXfudQtAPFK2q4UIws529WwX-9mWmcbBG7qRHVmjpgPq-twdb~TfmyCqWUB~aaviPWF1pENZuRLIFCjAV5iufCjg_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response=url1.urlopen(url)
        data=response.read()
        filename=path
        file=open(filename,'w')
        doc=data.decode('utf-8')
        file.write(doc)
        file.close

    def processdata(self,path):
        fileh=open(path, "r+")
        res=[int(line.strip()) for line in fileh if str(line.strip())!=""]
        return res

    def Countinv(self, arr):
        if len(arr)<2:return arr,0
        mid = int(len(arr)/2)
        l,x=self.Countinv(arr[0:mid])
        r,y=self.Countinv(arr[mid:])
        res,z=self.mergecountinv(l,r)
        return res, (x+y+z)

    def mergecountinv(self,l,r):
        if not l or not r: return l,0 or r,0
        n1,n2,res,count=len(l),len(r),[],0
        l.append(float('inf'))
        r.append(float('inf'))
        for k in range(n1+n2):
            if l[0]<=r[0]:
                res.append(l.pop(0))
            else:
                res.append(r.pop(0))
                if l:
                    count+=(len(l)-1)
        return res,count

if __name__ == "__main__":
    filename="C:/Public/Code/CountInv/IntegerArr.txt"
    obj=Inv()
    if os.path.isfile(filename):
        res=obj.processdata(filename)
        start=time.time()
        #print(res[1:10],len(res))
        print(obj.Countinv(res))
        stop=time.time()
        print("The time taken : {}".format(stop-start))
    else:
        obj.gettingthefile(filename)
