'''
Count Inversions in a list using MergeSort
uses O(nlogn)
'''
class Inv(object):
    def __init__(self):
        #self.count=0
        super(Inv, self).__init__()

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

obj=Inv()
print(obj.Countinv([6,5,4,3,2,1]))
