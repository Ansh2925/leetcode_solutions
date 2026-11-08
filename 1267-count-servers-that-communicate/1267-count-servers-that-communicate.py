class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        ans = 0
        
        m = len(grid)
        n = len(grid[0])

        row_count = [0]*m
        col_count = [0]*n

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]:
                    row_count[row] += 1
                    col_count[col] += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1 and (row_count[row] > 1 or col_count[col] > 1):
                    ans += 1


        return ans