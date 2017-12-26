'''
MergeSort
- Given a unsorted list
- Merge operation that is merging two sorted halves
- Divide and conquer - > logn
'''
class MergeSort(object):
    """docstring for MergeSort."""
    def __init__(self):
        super(MergeSort, self).__init__()

    def mergeSort(self, arr):
        if (len(arr))<2:return arr
        mid = int((len(arr))/2)
        left,right =  self.mergeSort(arr[:mid]),self.mergeSort(arr[mid:])
        return self.merge(left,right)

    def merge(self,l,r):
        if not l or not r:return l or r
        n1,n2,res,i,j = len(l),len(r),[],0,0 #Length of the left subarray arr[p..mid] ,and the rigt subarray arr[mid+1..r]
        l.append(float('inf'))
        r.append(float('inf'))
        for k in range(n1+n2):
            if l[i]<=r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1
        return res

obj = MergeSort()
arr = [3,4,5,1,2,8,3,7,6]
print(obj.mergeSort(arr))
