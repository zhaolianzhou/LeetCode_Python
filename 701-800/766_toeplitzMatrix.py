class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])
        for i in range(0, M):
            j = i
            k = 0
            while j < M-1 and k < N-1:
                if matrix[j][k] != matrix[j+1][k+1]:
                    return False
                j += 1
                k += 1

        for i in range(0, N):
            k = i
            j = 0
            while j < M-1 and k < N-1:
                if matrix[j][k] != matrix[j+1][k+1]:
                    return False
                j += 1
                k += 1
        return True

