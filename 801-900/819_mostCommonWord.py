import re, string, operator

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        string_array = re.split("[" + string.punctuation+' ' + "]", paragraph.lower())
        word_freq = {}
        for item in string_array:
            if item in word_freq:
                word_freq[item] += 1
            else:
                word_freq[item] = 1
        sorted_word_freq = sorted(word_freq.items(), key = operator.itemgetter(1), reverse = True)

        for key, value in sorted_word_freq:
            if key not in banned and key != "":
                return key



if __name__=="__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    solu = Solution()
    print(solu.mostCommonWord(paragraph, banned))


