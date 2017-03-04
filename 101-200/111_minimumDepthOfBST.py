class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self,root):
        if root is None:
            return 0
        depth = []
        curr_depth=0
        self.calDepth(root,curr_depth,depth)
        depth=sorted(depth)
        return depth[0]

    def calDepth(self,root,curr_depth,depth):
        if root:
            curr_depth+=1
        if root.left is None and root.right is None:
            depth.append(curr_depth)
        if root.left:
            self.calDepth(root.left,curr_depth,depth)
        if root.right:
            self.calDepth(root.right,curr_depth,depth)

if __name__=="__main__":
    solu=Solution()
    root = TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(5)
    print solu.minDepth(root)