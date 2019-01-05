class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        row = 0
        count = 0
        lower_s = S.lower()
        for c in lower_s:
            if count + widths[ord(c)-ord('a')] <= 100:
                count+=widths[ord(c)-ord('a')]
            else:
                row += 1
                count = widths[ord(c)-ord('a')]
        return [row, count]
