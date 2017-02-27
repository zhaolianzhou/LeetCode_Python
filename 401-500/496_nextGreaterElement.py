class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[-1 for x in range(len(findNums))]
        num_pos = dict()
        for num in nums:
            for wait in num_pos.keys():
                if num>wait:
                    result[num_pos[wait]]=num
                    num_pos.pop(wait)
            if num in findNums:
                num_pos[num]=findNums.index(num)
        return result


if __name__ =="__main__":
    mySolu = Solution()
    mySolu.nextGreaterElement([2,4],[1,2,3,4])