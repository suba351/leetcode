class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        max_value = arr[0]
        for i in range(k):
            max_value = max(max_value, arr[i])
            dp[i] = max_value * (i + 1)
        for i in range(k, n):
            max_value = 0
            max_ans = 0
            for j in range(0, k):
                max_value = max(max_value, arr[i - j])
                max_ans = max(max_ans, dp[i - j - 1] + max_value * (j + 1))
            dp[i] = max_ans

        print(dp)
        return dp[-1]
    
