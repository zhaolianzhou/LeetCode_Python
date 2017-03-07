
class Solution():
    def findDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        order=[False]*n
        result=[]
        for i in range(n):
            if order[nums[i]-1]:
                result.append(nums[i])
            else:
                order[nums[i]-1]=True
        return result

if __name__=="__main__":
    sol=Solution()
    nums=[4,3,2,7,8,2,3,1]
    print sol.findDuplicates(nums)
