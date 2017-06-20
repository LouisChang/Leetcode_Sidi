# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = res = ListNode(0)
        carry = 0
        while l1 or l2 or carry > 0:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            
            if l2:
                b = l2.val
                l2 = l2.next
            
            sum = a + b + carry
            carry = sum / 10
            res.next = ListNode(sum % 10)
            res = res.next
        return head.next
