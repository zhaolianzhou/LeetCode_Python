# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        root1_leaves = []
        root2_leaves = []
        def DFS(tree, leaves):
            if tree.left == tree.right == None:
                leaves.append(tree.val)
            else:
                if tree.left is not None:
                    DFS(tree.left, leaves)
                if tree.right is not None:
                    DFS(tree.right, leaves)

        DFS(root1, root1_leaves)
        DFS(root2, root2_leaves)
        return all(root1_leaves[i] == root2_leaves[i] for i in range(len(root2_leaves)))