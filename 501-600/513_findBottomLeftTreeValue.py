class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self,root):
        if root is None:
            return None
        stack1=[]
        stack2=[]
        stack3=[]
        stack1.append(root)
        while len(stack1):
            stack3 = list(stack1)
            while len(stack1):
                curr_node = stack1.pop(0)
                if curr_node.left is not None:
                    stack2.append(curr_node.left)
                if curr_node.right is not None:
                    stack2.append(curr_node.right)
            stack1=list(stack2)
            stack2=[]
        return stack3[0].val


if __name__=="__main__":
    sol=Solution()
    root = TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(5)
    root.right.right=TreeNode(6)
    root.right.left.left=TreeNode(7)
    print sol.findBottomLeftValue(root)
