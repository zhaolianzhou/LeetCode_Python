class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = ['']
        for c in S:
            if 'A'<= c <='Z' or 'a'<= c <='z':
                result = [i+j for i in result for j in [c.upper(), c.lower()]]
            else:
                result = [i+c for i in result]
        return result





if __name__=="__main__":
    strs = "adfegtyhyDEGTHY14325$^&&"
    solu = Solution()
    result = solu.letterCasePermutation(strs)
    for item in result:
        print(item)