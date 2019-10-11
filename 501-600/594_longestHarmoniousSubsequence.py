import operator
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        frequent ={}
        for item in nums:
            key = str(item)
            if key in frequent:
                frequent[key] += 1
            else:
                frequent[key] = 1
        sorted_frequent = sorted(frequent.items(), key = operator.itemgetter(0))

        max_length = 0

        for key,value in sorted_frequent:
            if str(int(key)+1) in frequent.keys():
                current_length = value + frequent[key+1]
                if current_length > max_length:
                    max_length = current_length

        return max_length

if __name__=="__main__":
    paragraph = [1,3,2,2,5,2,3,7]
    solu = Solution()
    print(solu.findLHS(paragraph))