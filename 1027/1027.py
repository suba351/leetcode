class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        memory = {}
        for i in range(n):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                if (i, d) in memory:
                    memory[(j, d)] = memory[(i, d)] + 1
                else:
                    memory[(j, d)] = 2
        return max(memory.values())
