'''
This is the classic Rod Cut problem from CLRS , Chapter 15
Given a price array which state the price for each cut length and the length "n" , determine how we can maximize the revenue
'''
class Solution(object):
    def rodcut(self, p, n): #Top down recurssice approach with exponential complexity
        if n==0: return p[n]
        q=float('-inf')
        for i in range(1,n+1):
            q=max(q,p[i]+self.rodcut(p,n-i))
        return q

    def memorodcut(self, p, n):
        memo=[float('-inf')]*n
        return self.memohelper(p,n,memo)

    def memohelper(self,p,n,memo):
        if memo[n-1]>=0:return memo[n-1]
        if n==0: q=0
        else:
            q=float('-inf')
            for i in range(1,n+1):
                q=max(q, p[i]+self.memohelper(p,n-i,memo))
        memo[n-1]=q
        return q


obj=Solution()
p=[0,1,5,8,9,10,17,17,20,24,30]
n=4
print(obj.memorodcut(p,n))
