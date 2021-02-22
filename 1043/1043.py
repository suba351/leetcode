class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            for j in range(0, k):
                if i-j <= 0:
                    dp[i] = max(arr[0:i + 1]) * (i + 1)
                    break
                else:
                    dp[i] = max(dp[i], dp[i - j - 1] + max(arr[i - j: i + 1]) * (j + 1))
        print(dp)
        return dp[-1]
