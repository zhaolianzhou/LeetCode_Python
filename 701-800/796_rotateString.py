import self


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_len = len(s)
        goal_len = len(goal)
        temp = s[:]
        if s_len != goal_len:
            return False
        else:
            for i in range(0, s_len):
                print(i)
                print("S: " + temp)
                print("G: " + goal)
                if temp == goal:
                    return True
                else:
                    temp = s[i+1:] + s[:i+1]
            return False



x = Solution()
print(x.rotateString("gcmbf", "fgcmb"))