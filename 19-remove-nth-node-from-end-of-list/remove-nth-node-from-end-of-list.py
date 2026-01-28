# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) #initialize dummy so that if head=[1] we can return None (we deleting head)
        dummy.next = head

        slow = fast = dummy 

        for _ in range(n):
            if fast is None:
                return None
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next #delete node

        return dummy.next #return head node

        