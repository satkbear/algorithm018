class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m , n = len(matrix),len(matrix[0])
        dp = [[0 if matrix[i][j]=='0' else 1 for j in range(n)] for i in range(m)]
    
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] =='1': 
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                else: 
                    dp[i][j] = 0

        ans = max([max(i) for i in dp])
        return ans ** 2