class Solution(object):
    def productExceptSelf(self,nums):
        """

        :param nums: List[int]
        :return: List[int]
        """
        n = len(nums)
        output=[1]*n
        output1=[0]*n
        output2=[0]*n
        product1 = 1
        product2 = 1
        for i in range(n):
            output1[i]=product1
            product1=product1*nums[i]
            output2[n-i-1]=product2
            product2=product2*nums[n-i-1]
        for j in range(n):
            output[j]=output1[j]*output2[j]

        return output


nums=[1,2,3,4]
sol = Solution()
print sol.productExceptSelf(nums)

