'''
Text justification
- Max length of sentence = 10 (let's say)
- How to break/split a sentence such that we will have the minimum cost that is minimum spaces between them
- Use the square of the distances to calculate the spaces that will be left after putting certain words
- words cannot be broken
- bottom up aprroach O(n2)
- Need to use memoization
The quick brown fox jumps
'''
class textjustify(object):
    """docstring for textjustify."""
    def __init__(self):
        super(textjustify, self).__init__()

    def returnlen(self,l,widthsize):
        countlen=0
        #print(l)
        for idx,x in enumerate(l):
            countlen+=len(x)
            if idx>=1:countlen+=1
        return widthsize-countlen

    def calculate(self,text,size):
        wordsl = text.split(" ")
        nwords = len(text.split(" "))
        mat = [[None]*nwords for x in range(nwords)]
        for i in range(nwords):
            for j in range(nwords):
                temp = self.returnlen(wordsl[i:j+1],size)
                if temp>=0 and temp!=size:
                    mat[i][j] = temp**2
                elif temp<0 :
                    mat[i][j] = float('inf')
        mincost, result = [None for i in range(nwords)],[None for i in range(nwords)]
        #print(mat[:][:])
        for row in range(nwords-1,-1,-1):
            mincost[row] = mat[row][nwords-1]
            result[row] = nwords
            #print(mincost, result)
            for col in range(nwords-1,row,-1):
                if mat[row][col-1] == 'inf':# this does not hit
                    print("hitting inf at", col)
                if mincost[row] > mincost[col] + mat[row][col-1]:
                    mincost[row] = mincost[col] + mat[row][col-1]
                    result[row] = col
        rep=0
        for idx,val in enumerate(result):
            if val!=rep:
                print(wordsl[idx:val])
            rep = val
        print(mincost, result)

obj = textjustify()
words = "The quick brown fox jumpsover"
pagesize = 10
obj.calculate(words, pagesize)

'''
Output:
['The', 'quick']
['brown', 'fox']
['jumpsover']
[3, 27, 2, 50, 1] [2, 2, 4, 4, 5]
[Finished in 0.236s]
'''
