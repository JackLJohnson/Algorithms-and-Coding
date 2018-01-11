'''
HeapSort - Max Heap only [sorting in increasing order] [parent node is greater than the values in its two children nodes.]
Definitions :
- perfect/complete binary tree - A binary tree with all leaf nodes at the same depth. All internal nodes have degree 2.
- Note: A perfect binary tree has 2^(n+1)-1 nodes, where n is the height. It can be efficiently implemented as an array, where a node at index i has children at indexes 2i and 2i+1 and a parent at index i/2.
- https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees
- http://www.geeksforgeeks.org/heap-sort/
- Complexity - O(nlogn)
'''

class Heapsort(object):
    """docstring for Heapsort."""
    def __init__(self):
        super(Heapsort, self).__init__()

    def heapify(self, arr, n, indx):
        #arr is a stack
        #Using Binary heap
        res = []
        largest = indx
        leftchild = 2*indx + 1
        rightchild = 2*indx + 2

        #Check if left child exist
        if leftchild<n and arr[indx]<arr[leftchild]:
            largest = leftchild

        if rightchild<n and arr[largest]<arr[rightchild]:
            largest = rightchild

        #chage the root
        if largest!=indx:
            arr[indx], arr[largest] = arr[largest], arr[indx] #swap

            # heapify The root
            self.heapify(arr, n, largest)
        return arr

    def heapsort(self, arr):
        n = len(arr)

        #build a maxheap
        for i in range(0,n+1):
            self.heapify(arr, n, i)


        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] #swap
            # Can use a pop mechanism here
            self.heapify(arr, i, 0)

        return arr

obj = Heapsort()
arr = [4,10,3,5,1]
arr1 = [4,10,3]
print(obj.heapsort(arr))
