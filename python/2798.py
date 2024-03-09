class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()  
    hours = [5,1,4,2,2]
    target = 6
    print(s.numberOfEmployeesWhoMetTarget(hours, target))