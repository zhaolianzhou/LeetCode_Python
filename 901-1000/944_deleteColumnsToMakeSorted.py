class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        if len(A) == 0:
            return 0
        else:
            max_len = len(A[0])
            for i in range(0, max_len):
                current_c = A[0][i]
                for item in A:
                    if item[i] < current_c:
                        count += 1
                        break
                    else:
                        current_c = item[i]
        return count

if __name__=="__main__":
    strs = ["cba","daf","ghi"]
    solu = Solution()
    print(solu.minDeletionSize(strs))
