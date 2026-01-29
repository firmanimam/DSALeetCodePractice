# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        current = head
        while current.next:
            prev_node_val = current.val
            current = current.next
            current.val = 2 * prev_node_val + current.val
        return current.val



        