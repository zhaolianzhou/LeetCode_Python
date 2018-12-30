class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = len(A)
        for i in range(0, count):
            if A[i+1] > A[i]:
                continue
            else:
                return i
            