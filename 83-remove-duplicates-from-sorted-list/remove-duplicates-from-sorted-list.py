# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = runner = head
        while current is not None:
            
            while runner.next is not None:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
            runner = current
        return head
        