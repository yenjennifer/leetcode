class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers starting from num
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update max_length
                max_length = max(max_length, current_length)
        
        return max_length


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums: return 0
#         map ={}
#         for i in nums:
#             map[i] = 0

#         def get_MaxPath(key, map):
#             if key not in map: 
#                 return 0
#             if map[key] != 0: 
#                 return map[key]
#             map[key] = get_MaxPath(key-1, map) + 1
#             return map[key]
        
#         maxPath = 0
#         for i in map:
#             maxPath = max(maxPath, get_MaxPath(i, map))

#         return maxPath