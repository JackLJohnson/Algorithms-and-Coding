from itertools import permutations
class Solution(object):
    def question1(self,s,t):
        list_=permutations(t, len(t))
        for val in list_:
            if ''.join(val) in s:return True
        return False
obj=Solution()
s="udacity"
t="man"
print(obj.question1(s,t))
