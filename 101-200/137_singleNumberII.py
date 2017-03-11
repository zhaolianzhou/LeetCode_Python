class Solution(object):
    def singleNumber(self,nums):
        """

        :param nums: List[int]
        :return: int
        """
        sort_nums = sorted(nums)
        n = len(nums)
        i = 0
        while i < n:
            if i == n-1:
                return sort_nums[i]
            if sort_nums[i+1]==sort_nums[i]:
                i+=3
            else:
                return sort_nums[i]





nums = [1,2,3,2,3,4,5,3,1,2,4,1,4]
sol = Solution()
print sol.singleNumber(nums)