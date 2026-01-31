# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        prev1 = dummy1
        prev2 = dummy2

        current = head

        while current:
            after = current.next
            current.next = None

            if current.val < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
            
            current = after

        prev1.next = dummy2.next
        head = dummy1.next
        dummy1.head = None

        return head
        