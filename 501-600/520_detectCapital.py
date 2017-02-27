class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        char1 = word[0]
        if char1.isupper():
            upper = 0
            lower = 0
            for char in word[1:]:
                if char.isupper():
                    upper+=1
                else:
                    lower+=1
            if upper==0 or lower==0:
                return True
            else:
                return False
        else:
            for char in word[1:]:
                if char.isupper():
                    return False
            return True


if __name__ =="__main__":
    mySolu = Solution()
    print mySolu.detectCapitalUse("I")