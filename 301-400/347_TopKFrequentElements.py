import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        count = dict()
        result = []
        for i in range(n):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]]=1

        sort_count = sorted(count.items(),key=operator.itemgetter(1),reverse=True)
        for j in range(k):
            result.append(sort_count[j][0])
        return result

sol = Solution()
nums = [1,1,2,2,3,4]
sol.topKFrequent(nums,2)
