
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if root.children is None:
            return 1

        depth = 0
        current_list = [root]

        def BFS(current_list, depth):
            if len(current_list):
                depth += 1
                next_gen = []
                for i in current_list:
                    if i.children is not None:
                        for child in i.children:
                            next_gen.append(child)

                BFS(next_gen, depth)

        BFS(current_list, depth)

        return depth