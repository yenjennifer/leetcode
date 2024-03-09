class Solution:
    def finalValueAfterOperations(self, operations):
        # "++X", "X++", "--X", "X--"
        value = 0
        for i in operations:
            if i == "--X" or i == "X--":
                value-=1
            else:
                value+=1
        return value
