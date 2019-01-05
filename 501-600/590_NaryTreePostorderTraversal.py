
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root is None:
            return []


        def travel(root, result):
            for i in root.children:
                if i is not None:
                    travel(i, result)
            result.append(root.val)

        travel(root, result)
        return result