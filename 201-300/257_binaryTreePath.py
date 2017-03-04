class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self,root):
        result = []
        if root is None:
            return result
        path = []
        self.binaryTreeSearch(root,result,path)
        resultStr=[]
        for tem in result:
            temStr = ""
            for i in tem:
                temStr+="->"+str(i)
            temStr=temStr[2:]
            resultStr.append(temStr)
        return resultStr

    def binaryTreeSearch(self,root,result, path):
        if root.left is None and root.right is None:
            path.append(root.val)
            result.append(list(path))
        else:
            path.append(root.val)
            if root.left is not None:
                self.binaryTreeSearch(root.left,result,path)
            if root.right is not None:
                self.binaryTreeSearch(root.right,result,path)
        path.pop()

if __name__=="__main__":
    solu=Solution()
    root = TreeNode()
    # root.left=TreeNode(2)
    # root.right=TreeNode(3)
    # root.left.right=TreeNode(5)
    print solu.binaryTreePaths(root)