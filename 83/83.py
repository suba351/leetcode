# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        first, second = head, head.next
        while second.next is not None:
            if first.val == second.val:
                first.next = second.next
            else:
                first = second
            second = second.next
        if first.val == second.val:
                first.next = second.next
        return head
