class Solution:
    def decode(self, encoded, first):
        ans = [first]
        for num in encoded:
            ans.append(ans[-1] ^ num)
        return ans

        # ans = [first]
        # a = encoded[0] ^ first
        # ans.append(a)
        # for x in encoded[1:]:
        #     a = x ^ a
        #     ans.append(a)
        # return ans

if __name__ == '__main__':
    s = Solution()
    encoded = [6,2,7,3]
    first = 4
    print(s.decode(encoded, first))