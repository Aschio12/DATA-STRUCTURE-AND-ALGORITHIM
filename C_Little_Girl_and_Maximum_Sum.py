n,q=map(int,input().split())
arr=list(map(int,input().split()))
quer=[]
for _ in range(q):
    quer.append(list(map(int,input().split())))
mark=[0]*(n+1)
for l,r in quer:
    mark[l-1]+=1
    mark[r]-=1
    
for i in range(1,len(mark)):
    mark[i]=mark[i]+mark[i-1]
mark.sort(reverse=True)
arr.sort(reverse=True)
tot=0
for i in range(len(arr)):
    tot+=(arr[i]*mark[i])
print(tot)
    
    
