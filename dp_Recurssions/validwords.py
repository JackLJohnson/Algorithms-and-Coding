'''
Given a wordlist with a set of characters without any spaces
'''
class Solution(object):
    def wordbreak(self, s, worddict, res):
        n,key,snew=len(s),'',list(s)
        while snew:
            key+=snew.pop(0)
            if key in worddict:
                res.append(key)
                self.wordbreak(''.join(snew),worddict, res)
        return res

    def wordbreak2(self, s, worddict, res, flag):
        n,key,snew=len(s),'',list(s)
        while snew:
            key+=snew.pop(0)
            if key in worddict:
                res.append(key)
                flag.add(True)
                self.wordbreak2(''.join(snew),worddict, res, flag)
        return res,flag

    def wordbreak_dp(self, s, worddict):
        ok=[True]
        for i in len(range(s)+1)
            ok+= any(ok[j] and s[j:i] in worddict for j in range(i))
        return ok[-1]

obj=Solution()
s="leetcodein"
worddict=["leet","code"]
print(obj.wordbreak2(s,worddict,[],set()))
# res=list("".join(list(set(obj.wordbreak(s,worddict,[])))))
# print(res)
# list_=list(s)
# if len(res)<len(list_):print(False)
# for ch in list_:
#     if ch not in res:print(False)
