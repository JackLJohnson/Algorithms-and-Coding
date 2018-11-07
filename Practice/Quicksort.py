'''
Quicksort
'''
class Quicksort(object):
	"""docstring for Quicksort"""
	def __init__(self):
		super(Quicksort, self).__init__()
		#self.list_ = list_

	def quicksort(self, A, p, r):
		if p<r:
			q=self.partition(A, p, r)
			self.quicksort(A, p, q-1)
			self.quicksort(A, q+1, r)

	def partition(self,A, p, r):
		x=A[r]
		i=p-1
		for j in range(p, r):
			if A[j]<=x:
				i+=1
				A[i],A[j]=A[j],A[i]
		A[i+1],A[r]=A[r],A[i+1]
		return i+1

obj=Quicksort()
A=[5,4,9,7,1,8,3,2,6]
obj.quicksort(A, 0, len(A)-1)
print(A)
