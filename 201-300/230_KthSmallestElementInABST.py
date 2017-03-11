class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self,root,k):
        """

        :param root: TreeNode
        :param k: int
        :return: int
        """
        if root is None:
            return None
        nums=[]
        self.DFS(root,nums)
        return nums[k]

    def DFS(self,root,nums):
        if root.left is not None:
            self.DFS(root.left,nums)
        nums.append(root.val)
        if root.right is not None:
            self.DFS(root.right,nums)    


