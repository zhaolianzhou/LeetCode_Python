class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        front = 0
        side = 0
        N = len(grid)
        top = N * N
        for i in grid:
            front += max(i)
            top -= i.count(0)

        for j in range(0, N):
            side += max([grid[t][j] for t in range(0, N)])

        return top + front + side