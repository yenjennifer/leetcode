# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#iterative
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            nxt = curr
        return prev
    

#recursive
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        def recursive(curr):
            if not curr.next:
                return curr
            new_head = recursive(curr.next)
            curr.next.next = curr
            curr.next = None
            return new_head

        return recursive(head)