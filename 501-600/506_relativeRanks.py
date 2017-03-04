import sys,operator
class Solution(object):
    def findRelativeRanks(self,nums):
        """
        Idea: find the largest three element, replace with medal
        :param nums:
        :return:
        """
        n = len(nums)
        ranks=dict()
        ranklist = [0]*n
        for i in range(n):
            ranks[i]=nums[i]
        sorted_rank = sorted(ranks.items(),key=operator.itemgetter(1),reverse=True)
        i=0
        last_num=-sys.maxsize
        for item in sorted_rank:
            curr_num = item[1]
            if not curr_num==last_num:
                i=i+1
            if i==1:
                ranklist[item[0]]="Gold Medal"
            elif i==2:
                ranklist[item[0]]="Silver Medal"
            elif i==3:
                ranklist[item[0]]="Bronze Medal"
            else:
                ranklist[item[0]] = str(i)
            last_num=curr_num
        return ranklist

if __name__ =="__main__":
    mySolu = Solution()
    nums = [10,9,2,5,5]
    print mySolu.findRelativeRanks(nums)
