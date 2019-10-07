class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        new_num = [1]+nums+[1]
        dp = [[0]*(n+2) for _ in range(n+2)]

        for k in range(1,n+1):
            for i in range(1,n+2-k):
                for j in range(i,k+i):
                    # print(k,i,j)
                    dp[i][k+i] = max(dp[i][k+i],dp[i][j]+dp[j+1][k+i]+new_num[i-1]*new_num[j]*new_num[k+i])
                    # print(dp[i][k+i])

        return dp[1][n+1]


test = Solution()
test.maxCoins([3,1,5,8])