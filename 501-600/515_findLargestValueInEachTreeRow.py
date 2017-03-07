class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        stack1=[]
        stack2=[]
        stack1.append(root)
        while len(stack1):
            curr_largest = stack1[0].val
            while len(stack1):
                curr_node = stack1.pop()
                if curr_largest<curr_node.val:
                    curr_largest=curr_node.val
                if curr_node.left is not None:
                    stack2.append(curr_node.left)
                if curr_node.right is not None:
                    stack2.append(curr_node.right)
            result.append(curr_largest)
            stack1=list(stack2)
            stack2=[]
        return result

if __name__=="__main__":
    sol=Solution()
    root = TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.right.left=TreeNode(5)
    root.right.right=TreeNode(6)
    root.right.left.left=TreeNode(7)
    print sol.largestValues(root)