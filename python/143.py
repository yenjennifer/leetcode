# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def middle(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        middle = dummy
        fast = dummy
        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next
        mid = middle.next
        middle.next = None
        return mid
        
    def reorderList(self, head) -> None:
        if not head: return None
        head2 = self.reverse(self.middle(head))
        cur1, cur2 = head, head2
        while cur2:
            nxt1 = cur1.next
            cur1.next = cur2
            cur1 = nxt1
            nxt2 = cur2.next
            cur2.next = cur1
            cur2 = nxt2
        return