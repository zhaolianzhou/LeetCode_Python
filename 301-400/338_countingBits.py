import math
class Solution(object):
    def countBits(self,num):
        """

        :param num:
        :return: List[int]
        """
        if num==0:
            return [0]
        num_1s=[0]*(num+1)
        for i in range(num+1):
            binarys = bin(i)[2:]
            print binarys
            num_1 = 0
            for j in range(len(binarys)):
                if binarys[j]=='1':
                    num_1+=1
            num_1s[i]=num_1

        return num_1s


if __name__=="__main__":
    sol = Solution()
    print sol.countBits(8)