class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        word_list = s.split(' ')
        result = ''
        for c in word_list:
            result = result +' '+ c[::-1]
        return result[1::]

if __name__ == '__main__':
    str = "Let's take Leetcode contest"
    sulo = Solution()
    print(sulo.reverseWords(str))