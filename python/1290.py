class Solution:
    def getDecimalValue(self, head) -> int:
        curr = head
        size = 0
        res = 0
        while curr:
            size = size+1
            curr = curr.next
        curr = head
        size-=1
        while curr:
            res += (2**size) * curr.val
            curr = curr.next
            size-=1
        return res
    
class Solution:
    def getDecimalValue(self, head) -> int:
        curr = head
        num = ''
        while curr:
            num += str(curr.val)
            curr = curr.next
        return int(num,2)