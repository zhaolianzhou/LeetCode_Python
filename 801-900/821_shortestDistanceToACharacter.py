class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        C_pos = [pos for pos, char in enumerate(S) if char == C]
        result = []
        N = len(S)
        for i in range(0, N):
            if i in C_pos:
                result.append(0)
            else:
                result.append(min([abs(i-j) for j in C_pos]))
        return result