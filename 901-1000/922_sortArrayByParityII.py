class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        tem_odd = {}
        tem_even = {}
        N = len(A)
        for i in range(0,N):
            if (i%2 == 0 and A[i]%2 == 0) or (i%2 == 1 and A[i]%2 == 1):
                continue
            elif i%2 == 0 and A[i]%2 != 0:
                tem_odd[i] = A[i]
            else:
                tem_even[i] = A[i]

        while len(tem_odd):
            odd_key, odd = tem_odd.popitem()
            even_key, even = tem_even.popitem()
            A[odd_key] = even
            A[even_key] = odd

        return A
