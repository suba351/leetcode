class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        ans = 0
        for word in words:
            dp[word] = 1
            for k in range(len(word)):
                w = word[:k] + word[k + 1:]
                if w in dp:
                    dp[word] = max(dp[word], dp[w] + 1)
            ans = max(ans, dp[word])
        return ans
