'''
Largest Square of 1's in a matrix
- DP , solving iteratively, assume the bottom right corner

Input matrix of any size

[   [1 1 0 1 0],
    [0 1 1 1 1],
    [1 1 1 1 1],
    [0 1 1 1 1],
    [0 1 1 1 1] ]

Output
3 [3x3]
'''
def largest_square(matrix):
    nrows, ncols = len(matrix), len(matrix[0])
    dp=[[0]*ncols for i in range(nrows)]
    dp[0] = matrix[0]
    max_=0
    for i in range(nrows):dp[i][0]=matrix[i][0]
    for i in range(1,nrows):
        for j in range(1,ncols):
            if matrix[i][j]==1:
                dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                max_=max(max_,dp[i][j])
    return max_

if __name__ == "__main__":
    mat = [[1,1,0,1,0],[0,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1]]
    print(largest_square(mat))
