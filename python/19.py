class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if not head: return None
        dummy = ListNode()
        dummy.next = head
        count = 0
        s = f = dummy
        while n!= count:
            count+=1
            f = f.next
        while f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return dummy.next

#get total length, and count to target
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head: return None
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size+=1
        if size == 1: return None
        target = size - n
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while target > 0:
            target-=1
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next