# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        cur = head
        seen = set()
        while cur not in seen and cur:
            seen.add(cur)
            cur = cur.next
        return False if not cur else True


class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class Solution:
    def hasCycle(self, head) -> bool:
        if not head: return False
        dummy = ListNode()
        dummy.next = head
        slow = dummy.next
        fast = dummy.next.next
        while slow!=fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return fast == slow