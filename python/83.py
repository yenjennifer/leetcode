# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head: return head
        cur = head
        while cur and cur.next:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head