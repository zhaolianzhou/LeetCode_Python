# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.left is None:
            return root

        def DFS(tree):
            if tree.left is None:
                result = TreeNode(tree.val)
                if tree.right is not None:
                    result.right = DFS(tree.right)
                return result
            if tree.left is not None:
                left_tree = DFS(tree.left)
                current_node = left_tree
                while current_node.right is not None:
                    current_node = current_node.right
                current_node.right = TreeNode(tree.val)
                if tree.right is not None:
                    current_node.right.right = DFS(tree.right)
                return left_tree


        return  DFS(root)