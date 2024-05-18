#Function 1: Using a Set
#T:O(N+M) M:O(N)
class Solution:
    def getIntersectionNode1(self, headA, headB) :
        seen = set()
        cur1 = headA
        cur2 = headB
        while cur1:
            seen.add(cur1)
            cur1 = cur1.next
        while cur2:
            if cur2 in seen:
                return cur2
            cur2 = cur2.next
        return None

#Function 2: Using Node Value Negation
#T O(N+M), M O(1) 
class Solution:
    def getIntersectionNode2(self, headA, headB):
        intersect = None
        curA = headA
        curB = headB
        while curA:
            curA.val = -(curA.val)
            curA = curA.next

        while curB:
            if curB.val < 0:
                intersect = curB
                break
            curB = curB.next

        curA = headA
        while curA:
            curA.val = -(curA.val)
            curA = curA.next
        return intersect

#Function 3: Two-Pointer Technique
#T O(N+M) M O(1)
class Solution:
    def getIntersectionNode3(self, headA, headB):
        curA = headA
        curB = headB

        while curA != curB:
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next

        return curA