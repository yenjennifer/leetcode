nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()  # Sorting the input list
        result = set()  # Using a set to store unique triplets

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            target = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in result]


# def twoSum(numbers, target):
#     l = 0
#     r = len(numbers)-1
#     list = []
#     while r > l:
#         if numbers[r] + numbers[l] == target:
#             list.append([numbers[l], numbers[r], -target])
#         if numbers[r] + numbers[l] > target:
#             r-=1
#         else:
#             l+=1
#     return list


# nums_sort  = sorted(nums) 

# seen = set()
# for i in nums_sort:
#     temp_list = nums_sort.copy()
#     temp_list.remove(i)

#     if twoSum(temp_list, -i)!= []:
#         temp = twoSum(temp_list, -i)

#         for sub in temp:
#             sub.sort()      
#             seen.add(tuple(sub))

# ans = []
# for item in seen:
#     ans.append(list(item))
# print(ans)