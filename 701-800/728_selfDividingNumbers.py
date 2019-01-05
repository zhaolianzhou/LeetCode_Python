class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []

        def isSelfDivide(num):
            num_str = str(num)
            for c in num_str:
                if c == '0':
                    return False
                if num%int(c) != 0:
                    return False

            return True

        for i in range(left, right+1):
            if isSelfDivide(i):
                result.append(i)
        return result
