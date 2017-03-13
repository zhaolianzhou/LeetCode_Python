# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        result_rev = []
        tem1 = l1
        tem2 = l2
        while tem1:
            list1.append(tem1.val)
            tem1=tem1.next
        while tem2:
            list2.append(tem2.val)
            tem2 = tem2.next
        rev1 = list1[::-1]
        rev2 = list2[::-1]
        n1 = len(rev1)
        n2 = len(rev2)
        former = 0
        # rev1 is always the longest one
        if n1 < n2:
            tem = list(rev1)
            rev1 = list(rev2)
            rev2 = list(tem)
            temn = n1
            n1 = n2
            n2 = temn
        for i in range(n2):
            curr_res = rev1[i]+rev2[i]+former
            if curr_res >= 10:
                former = curr_res/10
            else:
                former = 0
            curr_res = curr_res %10
            result_rev.append(curr_res)
        for j in range(n1-n2):
            curr_res = rev1[j+n2]+former
            if curr_res >= 10:
                former = curr_res/10
            else:
                former = 0
            curr_res = curr_res %10
            result_rev.append(curr_res)
        if former>0:
            result_rev.append(former)
        result = result_rev[::-1]
        return result

l1 = ListNode(5)
# l1.next = ListNode(3)
# l1.next.next = ListNode(4)
# l1.next.next.next = ListNode(3)
l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

sol = Solution()
print sol.addTwoNumbers(l2,l1)