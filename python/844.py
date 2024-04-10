# Time O(N+M), Space O(N+M) 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(stack, string):
            stack = []
            for c in string:
                if not stack and c == '#':
                    continue
                elif c == '#':
                    stack.pop()
                else:
                    stack.append(c)
            return stack

        stack_s = []
        stack_t = []
        return backspace(stack_s, s) == backspace(stack_t, t)

# # Time O(N) Space O(1)
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def apply_backspaces(string):
#             # Pointer to keep track of the position to write the next character
#             write_index = 0
#             for char in string:
#                 if char != '#':
#                     # Write non-backspace characters to the current position
#                     string[write_index] = char
#                     write_index += 1
#                 elif write_index > 0:
#                     # Move the write index back if a backspace is encountered
#                     write_index -= 1
#             # Truncate the string at the final write index
#             return string[:write_index]

#         # Apply backspace operations to both strings
#         s = apply_backspaces(list(s))
#         t = apply_backspaces(list(t))

#         # Check if the resulting strings are equal
#         return s == t