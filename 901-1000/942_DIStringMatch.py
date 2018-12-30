from operator import itemgetter
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        res_arr = [0]*(N+1)
        new_result = {i: 0 for i in range(0, N+1)}
        for i in range(0, N):
            if S[i] == 'I':
                new_result[i+1] = new_result[i] + 1
            else:
                new_result[i+1] = new_result[i] - 1

        result = dict(sorted(new_result.items(), key=itemgetter(1)))
        real_num = 0
        for k in result:
            res_arr[k] = real_num
            real_num += 1
        return res_arr

if __name__ == "__main__":
    strs = "DDI"
    solu = Solution()
    print(solu.diStringMatch(strs))