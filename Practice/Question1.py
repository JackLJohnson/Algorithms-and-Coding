from itertools import permutations
class Solution(object):
    def question1(self,s,t):
        list_=permutations(t, len(t))
        for val in list_:
            if ''.join(val) in s:return True
        return False
obj=Solution()

print(obj.question1("udacity","da"))  #True
print(obj.question1("udacity","man")) #False
print(obj.question1("udacity",""))    #True
