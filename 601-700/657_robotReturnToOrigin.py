class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U = 0
        L = 0
        for item in moves:
            if item == "U":
                U+=1
            elif item == "D":
                U-=1
            elif item == "L":
                L+=1
            else:
                L-=1
        return U==0 and L==0

