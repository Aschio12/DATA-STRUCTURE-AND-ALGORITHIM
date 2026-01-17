n,k,q=map(int,input().split())
m=200000
mark=[0]*(m+2)
minn=float("inf")
maxx=float("-inf")
for _ in range(n):
    left,right=map(int,input().split())
    mark[left]+=1
    mark[right+1]-=1
    minn=min(minn,left)
    maxx=max(maxx,right)
    
prefix=[0]*(m+1)
current=0
for i in range(1,m+1):
    current+=mark[i]
    if current>=k:
        prefix[i]=prefix[i-1]+1
    else:
        prefix[i]=prefix[i-1]

for i in range(q):
    a,b=map(int,input().split())
    print(prefix[b]-prefix[a-1])

    
    
    