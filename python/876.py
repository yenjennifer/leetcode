#pointers, fast moves 2x faster then slow, once fast or fast.next reaches the end, slow will be in the middle
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#calculate length
import math
class Solution:
    def middleNode(self, head):
        if not head: return head
        cur = head
        size = 0
        while cur:
            size+=1
            cur = cur.next
        size = math.ceil((size+1)/2)
        print(size)
        idx = 1
        while idx < size:
            head = head.next
            idx+=1
        return head
