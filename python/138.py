
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None: None}
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        

# class Solution:
#     def copyRandomList(self, head):
#         dummy = Node(-1)
#         p1, p2 = head, dummy
#         arr1, arr2 = [], []
#         order = []
#         count = 0
#         while p1:
#             p2.next = Node(p1.val)
#             arr2.append(p2)
#             p2 = p2.next
#             arr1.append(p1)
#             p1 = p1.next
#             count+=1

#         p1 = head
#         while p1:
#             idx = arr1.index(p1)
#             order.append(idx)
#             p1 = p1.next
#         p2 = dummy.next
#         m = 0

#         while p2:
#             print(p2)
#             p2.random = arr2[order[m]]
#             p2 = p2.next
#             m+=1
#         return dummy.next