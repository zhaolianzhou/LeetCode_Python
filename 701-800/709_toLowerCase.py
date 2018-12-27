class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ''
        for c in str:
            if c>='A' and c<='Z':
                result+= chr(ord(c)+ord('a')-ord('A'))
            else:
                result+=c

        return result


if __name__=="__main__":
    strs = "adfegtyhyDEGTHY14325$^&&"
    solu = Solution()
    print(solu.toLowerCase(strs))