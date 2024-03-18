img = [[100,200,100],[200,50,200],[100,200,100]]
n = len(img)
m = len(img[0])
ans=[]
for r,row in enumerate(img):
    ans.append([])
    for c,col in enumerate(row):
        s=0
        count=0
        for dx in range(-1,2):
            for dy in range(-1,2):
                if 0<=r+dx<n and 0<=c+dy<m:
                    s+=img[r+dx][c+dy]
                    count+=1
        ans[-1].append(s//count)
print(ans)

# for i in range(r):
#     for j in range(c):
        # if :
        #     img[i][j] = math.floor((img[i][j] + img[i][j-1]+ img[i][j+1] + 
        #                             img[i-1][j] + img[i-1][j-1] + img[i-1][j+1] + 
        #                             img[i+1][j] + img[i+1][j-1] + img[i+1][j+1])//9)
        # if i == 0 or j == 0 or j == 0 or i == r or j == c:
        #     img[i][j] = math.floor((img[i][j] + img[i][j-1] + 
        #                             img[i-1][j] + img[i-1][j-1] + 
        #                             img[i+1][j] + img[i+1][j-1])//6)
        # if 0 < i < r-1 and 0 < j < c-1:
        #     img[i][j] = math.floor((img[i][j] + img[i][j-1]+ img[i][j+1] + 
        #                             img[i-1][j] + img[i-1][j-1] + img[i-1][j+1] + 
        #                             img[i+1][j] + img[i+1][j-1] + img[i+1][j+1])//9)
