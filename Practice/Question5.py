class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# Find the element in a singly linked list that's m elements from the end
class Solution(object):
    def question5(self, ll, m):
        res_=[]
        while ll:
            res_.append(ll.data)
            ll=ll.next
        return res_[-m]

# Test cases and Construct the linked List
ll=Node(2)
ll.next=Node(3)
ll.next.next=Node(4)
ll.next.next.next=Node(5)
ll.next.next.next.next=Node(6)

obj=Solution()

print(obj.question5(ll,3)) #4
print(obj.question5(ll,2)) #5
print(obj.question5(ll,1)) #6
