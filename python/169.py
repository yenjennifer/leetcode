nums = [2,2,1,1,1,2,2]
#Boyer-Moore Majority vote#
 # boyer moore voting algorithm basically if one candidate occurs more than n/2 times
 # others collectively occur less than n/2 times so we select one candidate and if it 
 # occurs votes++ else votes -- if votes==0 then choose another as that is not the candidate
vote = 0
candidate = None
for num in nums:
    if vote == 0:
        candidate = num
    if candidate == num:
        vote+=1
    else: vote-=1
print(candidate)