import operator
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        result_dict = dict()
        self.calSum(root,result_dict)
        frequent = max(result_dict.values())
        result_max = [k for k,v in result_dict.items() if v==frequent]
        return result_max

    def calSum(self,root,result):
        if root is None:
            return 0
        else:
            curr_sum = self.calSum(root.left,result)+self.calSum(root.right,result)+root.val
            if curr_sum in result:
                result[curr_sum]+=1
            else:
                result[curr_sum]=1
            return curr_sum


if __name__=="__main__":
    sol=Solution()
    root = TreeNode(5)
    root.left=TreeNode(2)
    root.right=TreeNode(-3)
    # root.left.left=TreeNode(4)
    # root.right.left=TreeNode(5)
    # root.right.right=TreeNode(6)
    # root.right.left.left=TreeNode(7)
    print sol.findFrequentTreeSum(root)