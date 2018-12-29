class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in A:
            i = i[::-1]
            result.append([0 if x==1 else 1 for x in i])

        return result

if __name__=="__main__":
    strs = [[1,1,0],[1,0,1],[0,0,0]]
    solu = Solution()
    print(solu.flipAndInvertImage(strs))
