class Solution(object):
    def question2(self, a):
        #Longest palindrome - use dp to solve
        dp = [[0]*len(a) for i in range(len(a))]
        arev=a[::-1]
        len_res=0
        for i in range(len(a)):
            for l in range(len(a)):
                if arev[i]==a[l]:
                    count=0
                    for j in range(l,len(a)):
                        if i+count<len(a):
                            #print(a[j], arev[i+count], j, i+count)
                            if a[j]==arev[i+count]:dp[i][j] = dp[i][j-1]+1
                            else: dp[i][j]=dp[i][j-1]
                        count+=1
            len_res = max(max(dp[i]),len_res)
            #len_res=max(max(dp[i][:]),len_res))
        return len_res

obj=Solution()
a="aa"
print(obj.question2(a))
