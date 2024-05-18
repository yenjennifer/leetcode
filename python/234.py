# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Compare reversed last half with first half
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
    
    def isPalindrome(self, head) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True


#STACK T: O(N), M: O(N)
class Solution:
    def isPalindrome(self, head) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.val != stack.pop():
                return False
            cur = cur.next
        return True

#Compare string
class Solution:
    def isPalindrome(self, head) -> bool:
        old = new = ''
        cur = head
        prev = None
        while cur:
            old += str(cur.val)
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        while prev:
            new+=str(prev.val)
            prev = prev.next
        return new == old