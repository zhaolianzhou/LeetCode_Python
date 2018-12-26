class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        parenthese_pair = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in left:
                stack.insert(0, c)
            else:
                if len(stack):
                    if parenthese_pair[stack[0]] == c:
                        stack.pop(0)
                    else:
                        return False
                else:
                    return False
        return not len(stack)

if __name__=="__main__":
    strs = "()"
    solu = Solution()
    print(solu.isValid(strs))