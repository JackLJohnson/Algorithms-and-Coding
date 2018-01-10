'''
Print all permutations of a Given string
- Using Backtracking/DFS -> T(N) = N* (O(1) + T(N-1) +O(1)) = O(n*n!)
- Using BFS
- Using DFS - Similar to Backtracking approach, but does not need swap so better
'''
class Solution(object):
    def permstring(self,s):
        res=set()
        self.dfs(s,0,len(s)-1,res)
        return res

    def dfs(self, s, l, r, visited):
        if l==r:visited.add(''.join(s)) # we do not have anything left to be permuted
            #print(visited)
        else:
            for i in range(l,r+1):
                s[l],s[i]=s[i],s[l]
                self.dfs(s,l+1,r,visited)
                s[l],s[i]=s[i],s[l] #moving back to the same old configuration to restore  - Backtracking
        return visited

    def permstring_bfs(self,s):
        res = [[]]
        for n in s:
            newval=[]
            for val in res:
                for i in range(len(val)+1):
                    newval.append(val[:i]+[n]+val[i:])
            res=newval
        return res

    def permstring_dfs(self, s):
        return self.dfs(s, [], [])

    def dfs(self, s, path, res):
        if not s:res.append(path)
        for i in range(len(s)):
            self.dfs(s[:i]+s[i+1:],path+[s[i]],res)
        return res



obj=Solution()
s="ABCD"
res=obj.permstring_bfs(list(s))

#for The case of permstring_bfs
print([''.join(l) for l in res])

print(obj.permstring_dfs(list(s)))
