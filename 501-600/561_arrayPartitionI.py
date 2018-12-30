class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = int(len(nums)/2)
        result = 0
        for i in range(0, count):
            result+= nums[2*i]
        return result