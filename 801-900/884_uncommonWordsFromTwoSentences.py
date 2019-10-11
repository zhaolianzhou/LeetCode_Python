from collections import Counter

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_array = A.split()
        B_array = B.split()
        A_dict = {}
        B_dict = {}
        result = []
        for a_item in A_array:
            if a_item not in B_array:
                if a_item in A_dict:
                    A_dict[a_item] += 1
                else:
                    A_dict[a_item] = 1

        for b_item in B_array:
            if b_item not in A_array:
                if b_item in B_dict:
                    B_dict[b_item] += 1
                else:
                    B_dict[b_item] = 1

        for item in A_dict:
            if A_dict[item] == 1:
                result.append(item)
        for item in B_dict:
            if B_dict[item] == 1:
                result.append(item)

        return result

if __name__ == "__main__":
    solu = Solution()
    print(solu.uncommonFromSentences("this apple is sweet", "this apple is sour"))