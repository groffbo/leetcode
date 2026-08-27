class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if int(grid[n][m]) == 1:
                    count += 1
                    self.recurse(grid, n, m)

        return count


    def recurse(self, grid, x, y):
        #mark the visited one as a 0

        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0":
            return 0

        grid[x][y] = "0"

        self.recurse(grid, x + 1, y)
        self.recurse(grid, x - 1, y)
        self.recurse(grid, x, y - 1)
        self.recurse(grid, x, y + 1)
        

