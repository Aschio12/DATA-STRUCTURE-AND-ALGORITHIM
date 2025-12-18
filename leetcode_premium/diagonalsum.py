"given a sqare matrix find the sum of all diagonals"
mat=[[1,2],[5,7]]
l,r=0,len(mat)-1
tot=0
for row in range(len(mat)):
    if l!=r:
        tot+=mat[row][l]+mat[row][r]
    else:
        tot+=mat[row][l]
    l+=1
    r-=1
    
print(tot)
        