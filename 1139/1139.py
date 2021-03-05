class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        how_many_ones_left = [[0] * m for _ in range(n)]
        how_many_ones_right = [[0] * m for _ in range(n)]
        how_many_ones_up = [[0] * m for _ in range(n)]
        how_many_ones_bottom = [[0] * m for _ in range(n)]
        max_square = 0
        
        for x in range(n):
            how_many_ones_left[x][0] = grid[x][0]
            for y in range(1, m):
                how_many_ones_left[x][y] = grid[x][y] * how_many_ones_left[x][y - 1] + grid[x][y]
        
        for x in range(n):
            how_many_ones_right[x][-1] = grid[x][-1]
            for y in range(m - 2, -1, -1):
                how_many_ones_right[x][y] = grid[x][y] * how_many_ones_right[x][y + 1] + grid[x][y]
        
        for y in range(m):
            how_many_ones_up[0][y] = grid[0][y]
            for x in range(1, n):
                how_many_ones_up[x][y] = grid[x][y] * how_many_ones_up[x - 1][y] + grid[x][y]
        
        for y in range(m):
            how_many_ones_bottom[-1][y] = grid[-1][y]
            for x in range(n - 2, -1, -1):
                how_many_ones_bottom[x][y] = grid[x][y] * how_many_ones_bottom[x + 1][y] + grid[x][y]
        for x in range(n):
            for y in range(m):
                max_square = max(max_square, grid[x][y])
                diag = min(x, y)
                for length in range(diag, 0, -1):
                    if (how_many_ones_left[x][y] >= length + 1) and (how_many_ones_right[x - length][y - length] >= length + 1) and (how_many_ones_up[x][y] >= length + 1) and (how_many_ones_bottom[x - length][y - length] >= length + 1):
                        max_square = max(max_square, length + 1)
                        break
        return max_square**2
     
