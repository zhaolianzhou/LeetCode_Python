"""
You are given two strings order and s.
All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order,
then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Topics:
Hash Table, String, Sorting
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charMap = {order[i]: 0 for i in range(len(order))}
        for i in range(len(s)):
            if s[i] in charMap.keys():
                charMap[s[i]] += 1
            else:
                charMap[s[i]] = 1

        result = ''
        for k, v in charMap.items():
            result += v * k

        return result

