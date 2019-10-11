class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        sum = 0
        valid_rounds = []

        for i in ops:
            if i == '+':
                current_round = valid_rounds[-1] + valid_rounds[-2]
                valid_rounds.append(current_round)
                sum += current_round
            if i == 'D':
                current_round = valid_rounds[-1] * 2
                valid_rounds.append(current_round)
                sum += current_round
            if i == 'C':
                last_value = valid_rounds.pop()
                sum -= last_value
            else:
                valid_rounds.append(i)
                sum += i

        return sum