
arr = [1,25,35,42,68,70]
k = 1

class Solution:
    def getWinner(self, arr, k):
        if k >= len(arr):
            return max(arr)
        ptr = 0
        next = 1
        count = 0
        while count < k:
            if arr[ptr]>arr[next]: # 樓主贏
                arr.append(arr[next])
                next+=1
                count+=1
            elif arr[ptr]<arr[next]: #挑戰者贏
                arr.append(arr[ptr])
                ptr=next
                next+=1
                count = 1
        return arr[ptr]

# count = 0
# if k >= len(arr):
#     print(max(arr))
# while count<k:
#     if arr[0]>arr[1]:
#         count+=1
#         arr.append(arr[1])
#         arr.pop(1)
#     elif arr[0]<arr[1]:
#         arr.append(arr[0])
#         arr.pop(0)
#         count = 1
# print(arr[0])