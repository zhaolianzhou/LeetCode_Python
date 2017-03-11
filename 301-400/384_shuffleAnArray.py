import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled = list(self.nums)
        random.shuffle(shuffled)
        return shuffled


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print param_1
print param_2