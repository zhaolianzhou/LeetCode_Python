# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.i = 0
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s)==0:
            return None
        curr_num=""
        n = len(s)
        root = self.treeConHelp(curr_num,s,n)
        self.i = 0
        return root

    def treeConHelp(self,curr_num,s,n):
        while self.i <= n:
            if self.i==n:
                return curr_node
            if s[self.i]!='(' and s[self.i]!=')':
                curr_num+=s[self.i]
                self.i+=1
                if self.i==n or s[self.i]=='(' or s[self.i]==')':
                    val = int(curr_num)
                    curr_node = TreeNode(val)
                    curr_num = ""
            elif s[self.i]=='(':
                self.i+=1
                if curr_node.left is None:
                    curr_node.left=self.treeConHelp(curr_num,s,n)
                else:
                    curr_node.right=self.treeConHelp(curr_num,s,n)
            elif s[self.i]==')':
                self.i+=1
                return curr_node

sol = Solution()
result = sol.str2tree("4")
print result