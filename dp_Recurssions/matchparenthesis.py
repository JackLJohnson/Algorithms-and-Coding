class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_={')':'(','}':'{',']':'[' }
        res,snew=[],list(s)
        if not s:return True
        if len(snew)%2!=0:return False
        while snew:
            item=snew.pop(0)
            if item in dict_.values():res.append(item)
            elif item in dict_.keys():
                if res==[] or dict_[item]!=res.pop():return False
            else:return False
        return res==[]

    def isValid2(self,s):
        string1,delta=s,len(s)
        while delta !=0 and delta%2==0:
            s=s.replace("()","")
            s=s.replace("{}","")
            s=s.replace("[]","")
            delta = len(s) if delta>len(s) else 0
        return len(s)==0


obj=Solution()
s="[([()])])"
print(obj.isValid2(s))
