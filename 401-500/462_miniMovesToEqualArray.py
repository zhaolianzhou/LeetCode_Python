class Solution(object):
    def minMoves2(self,nums):
        """
        :param nums: List[int]
        :return: int
        """
        n=len(nums)
        nums_sort = sorted(nums)
        sum = 0
        for num in nums:
            sum+=abs(num-nums_sort[n/2])
        return sum