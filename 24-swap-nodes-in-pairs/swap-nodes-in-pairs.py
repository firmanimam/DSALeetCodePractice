# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        first = prev.next

        while first is not None and first.next is not None:
            second = first.next

            #Swap
            first.next = second.next
            second.next = prev.next
            prev.next = second

            prev = first
            first = first.next
        
        head = dummy.next

        return head
        

        