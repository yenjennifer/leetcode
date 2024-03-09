class Solution:
    def shuffle(self, nums):
        shuffled = []
        num1 = nums[:n]
        num2 = nums[n:]
        for i in num1:
            shuffled.append(i)
            for j in num2:
                shuffled.append(j)
                num2.pop(0)
                break

        return shuffled


# ############################
# shuffle=[0]*len(nums)
# idx=0
# for i in range(len(nums)):
#     shuffle[idx]=nums[i]
#     idx+=2
#     if(idx>=len(nums)): idx=1
# print(shuffled)