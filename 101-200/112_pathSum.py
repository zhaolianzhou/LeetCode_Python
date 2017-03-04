class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self,root,sum):
        if root is None:
            return False
        curr_sum = 0
        sums=[]
        self.calSum(root,sums,curr_sum)
        if sum in sums:
            return True
        else:
            return False

    def calSum(self,root,sums,curr_sum):
        if root:
            curr_sum+=root.val
        if root.left is None and root.right is None:
            sums.append(curr_sum)
        if root.left:
            self.calSum(root.left,sums,curr_sum)
        if root.right:
            self.calSum(root.right,sums,curr_sum)

if __name__=="__main__":
    solu=Solution()
    root = TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(5)
    print solu.hasPathSum(root,4)