class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_transformations = []
        for item in words:
            item_lower = item.lower()
            item_morse = ''
            for c in item_lower:
                item_morse+=morse_map[ord(c)-ord('a')]
            if item_morse not in unique_transformations:
                unique_transformations.append(item_morse)
        return len(unique_transformations)

if __name__=="__main__":
    strs = ['abca', 'aba', 'aaab']
    solu = Solution()
    print(solu.repeatedNTimes(strs))
