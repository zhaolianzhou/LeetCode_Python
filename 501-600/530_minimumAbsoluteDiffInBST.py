class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self,root):
        if root is None:
            return None
        else:
            result = []
            self.search(root,result)
        result = sorted(result)
        diff=[]
        for i in range(len(result)-1):
            diff.append(abs(result[i]-result[i+1]))
        return min(diff)
    def search(self,root,result):
        if root:
            result.append(root.val)
        if root.left:
            self.search(root.left,result)
        if root.right:
            self.search(root.right,result)

    # def getMiniDiff(self,root,sub,result):
    #     curr_diff = abs(root.val-sub.val)
    #     result.append(curr_diff)
    #     if sub.left is not None:
    #         self.getMiniDiff(root,sub.left,result)
    #         self.getMiniDiff(sub,sub.left,result)
    #     if sub.right is not None:
    #         self.getMiniDiff(root,sub.right,result)
    #         self.getMiniDiff(sub,sub.right,result)

if __name__=="__main__":
    solu=Solution()
    root = TreeNode(1)
    root.right=TreeNode(3)
    # root.right=TreeNode(3)
    root.right.left=TreeNode(2)
    print solu.getMinimumDifference(root)