class Solution:
    def restoreString(self, s, indices):
        ans = ""
        temp = [0]*len(s)
        for i in indices:
            temp[indices[i]]=s[i]
        #string.join(array)
        return ans.join(temp)

if __name__ == '__main__':
    s1 = Solution()
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    print(s1.restoreString(s, indices))