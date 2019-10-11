class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fib_num = [0, 1]
        if N < 2:
            return fib_num[N]
        else:
            for i in range(2, N+1):
                fib_num.append(fib_num[i-1] + fib_num[i-2])

        return fib_num[N]
