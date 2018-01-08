'''
GG:check if a given string is a sum-string
- Iterative Solution
'''
class Solution(object):
    def mainfn(self, s):
        if len(s)<2:return False
        bsize = int(len(s)/3)
        for i in range(1, bsize+1):
            val = self.stringsum(s,bsize)
            if val:return True
        return val

    def helper1(self,l):
        s1=''
        for v in l:s1+=str(v)
        return int(s1)

    def stringsum(self, s, size):
        res = [int(x) for x in s]
        while len(res)>2*(size):
            temp=[]
            for i in range(0,size):temp.append(str(res.pop()))
            temp=int("".join(temp[::-1]))
            val1, val2=self.helper1(res[-size:]),self.helper1(res[-size-size:-size])
            #print(temp,val1,val2)
            if temp == val1+val2:continue
            else:return False
        return True

obj=Solution()
s=["12243660","1111112223","2368","123456787"]
for st in s:
    print(1) if (obj.mainfn(st)) else print(0)
