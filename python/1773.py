class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        # Time Complexity: O(N), Space Complexity: O(N)
        dict = {}
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        elif ruleKey == "name":
            idx = 2
        for i in items:
            dict[i[idx]] = dict.get(i[idx], 0) +1
        if ruleValue not in dict:
            return 0
        return dict[ruleValue]
    
if __name__ == '__main__':
    s = Solution()
    items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
    ruleKey = "type"
    ruleValue = "laptop"
    print(s.countMatches(items, ruleKey, ruleValue))

        # dict_type = {}
        # dict_color = {}
        # dict_name = {}
        # for i in items:
        #     dict_type[i[0]] = dict_type.get(i[0], 0) +1
        #     dict_color[i[1]] = dict_color.get(i[1], 0) + 1 
        #     dict_name[i[2]] = dict_name.get(i[2], 0) + 1 
        # if ruleKey == "type" and ruleValue in dict_type:
        #     return dict_type[ruleValue]
        # elif ruleKey == "color" and ruleValue in dict_color:
        #     return dict_color[ruleValue]
        # elif ruleKey == "name" and ruleValue in dict_name:
        #     return dict_name[ruleValue]
        # else:
        #     return 0


        # count = 0
        # if ruleKey == "type":
        #     for item in items:
        #         if ruleValue == item[0]:
        #             count+=1
        # if ruleKey == "color":
        #     for item in items:
        #         if ruleValue == item[1]:
        #             count+=1
        # if ruleKey == "name":
        #     for item in items:
        #         if ruleValue == item[2]:
        #             count+=1
        # return count