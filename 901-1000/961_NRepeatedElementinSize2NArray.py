class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        unique = []
        for item in A:
            if item not in unique:
                unique.append(item)
            else:
                return item

if __name__=="__main__":
    strs = ['abca', 'aba', 'aaab']
    solu = Solution()
    print(solu.repeatedNTimes(strs))
