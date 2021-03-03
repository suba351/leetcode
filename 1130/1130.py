class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        min_sum = [[float('inf')] * n for _ in range(n)]
        max_val = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_val[i][i] = arr[i]
            min_sum[i][i] = 0
        
        length = 2
        while length <= n:
            left = 0
            right = length - 1
            while right < n:
                max_val[left][right] = max(max_val[left][right - 1], arr[right])
                for k in range(left, right):
                    print(k)
                    min_sum[left][right] = min(min_sum[left][right], min_sum[left][k] + min_sum[k + 1][right] + max_val[left][k] * max_val[k + 1][right])
                left += 1
                right = left + length - 1
            length += 1
        return min_sum[0][-1]
    
