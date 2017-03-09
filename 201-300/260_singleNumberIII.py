class Solution():
    def singleNumber(self,nums):
        """
        :param nums:List[int]
        :return: List[int]
        """
        n = len(nums)
        result = []
        for i in nums:
            if i in result:
                result.remove(i)
            else:
                result.append(i)
        return result

if __name__=="__main__":
    sol = Solution()
    nums=[1,2,1,3,2,5]
    print sol.singleNumber(nums)