class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        result = strs[0]
        for item in strs:
            while len(result):
                index = item.find(result)
                if index == 0:
                    break
                else:
                    result = result[0:-1]

        return result


if __name__=="__main__":
    # strs = ["flower", "flow", "flight"]
    strs = ['abca', 'aba', 'aaab']
    solu = Solution()
    print(solu.longestCommonPrefix(strs))