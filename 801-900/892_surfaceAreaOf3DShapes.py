class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        surface = 0
        N = len(grid)
        for i in range(0, N):
            for j in range(0, N):
                surface += 6*grid[i][j]
                if grid[i][j] > 1:
                    surface -= 2*(grid[i][j] - 1)
                if j+1 < N:
                    surface -= 2*min(grid[i][j], grid[i][j+1])
                if i+1 < N:
                    surface -= 2*min(grid[i][j], grid[i+1][j])
        return surface

if __name__=="__main__":
    solu = Solution()
    print(solu.surfaceArea([[1,0],[0,2]]))