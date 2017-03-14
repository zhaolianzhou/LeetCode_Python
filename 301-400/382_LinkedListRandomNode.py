# Definition for singly-linked list.
import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.link_ele = []
        tem = head
        while tem:
            self.link_ele.append(tem.val)
            tem = tem.next


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = len(self.link_ele)
        index = random.randint(0,n-1)
        return self.link_ele[index]