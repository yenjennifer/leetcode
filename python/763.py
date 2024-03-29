s  = "ababcbacadefegdehijhklij"
##get letter positions, store as tuples
ans,l = [],[]
for i in set(s):
    left = s.index(i)
    right = len(s)-1 - s[::-1].index(i) 
    l.append((left, right))
l = sorted(l)

##sliding window
new = l[0]
for j in range(1,len(l)):
    if new[1] > l[j][0]:
        new = (min(new[0], l[j][0]), max(new[1], l[j][1])) #expand
    else:
        ans.append(new[1]-new[0]+1)
        new = l[j]
ans.append(new[1]-new[0]+1)
print(ans)


##optimze##
class Solution:
    def partitionLabels(self, s: str):
        # Step 1: Create a dictionary to store the last occurrence position of each character
        last_occurrence = {}
        for idx, char in enumerate(s):
            last_occurrence[char] = idx
        
        ans = []  # Initialize the list to store partition sizes
        start = end = 0  # Initialize variables to track the start and end of the current partition
        
        # Step 2: Iterate through the string to update the end of the current partition
        for idx, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Update end to the maximum of current end and last occurrence of current character
            # If the current index is equal to the end of the current partition, it indicates the end of the partition
            if idx == end:
                # Append the size of the current partition to the answer list
                ans.append(end - start + 1)
                # Update the start of the next partition to the next index
                start = idx + 1
                
        return ans  # Return the list of partition sizes