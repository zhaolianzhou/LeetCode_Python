class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        current_sum = 0
        result = []
        for i in A:
            if i%2 ==0:
                current_sum += i

        for item in queries:
            index = item[1]
            val = item[0]
            if A[index] % 2 == 0:
                current_sum = current_sum - A[index]

            A[index] = A[index] + val

            if A[index] % 2 == 0:
                current_sum = current_sum + A[index]

            result.append(current_sum)

        return result

if __name__=="__main__":
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3,1], [-4, 0], [2, 3]]

    solu = Solution()
    print(solu.sumEvenAfterQueries(A, queries))