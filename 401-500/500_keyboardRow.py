
class Solution(object):
    def findWords(self,words):
        if not words:
            return []
        result =list()
        Rows1=set(['Q','W','E','R','T','Y','U','I','O','P'])
        Rows2=set(['A','S','D','F','G','H','J','K','L'])
        Rows3=set(['Z','X','C','V','B','N','M'])
        for word in words:
            chars = set(list(word.upper()))
            print chars
            if chars.issubset(Rows1):
                result.append(word)
            if chars.issubset(Rows2):
                result.append(word)
            if chars.issubset(Rows3):
                result.append(word)
        return result


if __name__ =="__main__":
    mySolu = Solution()
    mySolu.findWords(["Hello", "Alaska", "Dad", "Peace"])