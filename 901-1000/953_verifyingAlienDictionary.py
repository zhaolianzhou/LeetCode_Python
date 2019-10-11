class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(0, len(words)-1):
            print(words[i])
            print(words[i+1])
            if self.compareWords(words[i], words[i+1], order) is False:
                return False
        return True

    def compareWords(self, w1, w2, order):
        for index in range(0, len(w1)):
            if index >= len(w2):
                return False
            if order.index(w1[index]) < order.index(w2[index]):
                return True
            elif order.index(w1[index]) > order.index(w2[index]):
                return False

        return True

if __name__=="__main__":
    solu = Solution()
    print(solu.isAlienSorted(["apple","app"],'abcdefghijklmnopqrstuvwxyz'))