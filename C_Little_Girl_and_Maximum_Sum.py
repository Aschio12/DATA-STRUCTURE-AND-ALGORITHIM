n,q=map(int,input().split())
arr=list(map(int,input().split()))
quer=[]
for _ in range(q):
    quer.append(list(map(int,input().split())))
mark=[0]*(n+1)
for l,r in quer:
    mark[l-1]+=1
    mark[r]-=1
for i in range(1,n):
    mark[i]+=mark[i-1]
order=[]
for i in range(n):
    order.append([mark[i],i])
order.sort(key=lambda x:(-x[0],x[1]))

arr.sort(reverse=True)
required=[0]*n
for i in range(len(order)):
    required[order[i][1]]=arr[i]
prefix=[0]*n
prefix[0]=required[0]
for i in range(1,len(required)):
    prefix[i]=prefix[i-1]+required[i]
ans=0
for l,r in quer:
    if l==1:
        ans+=prefix[r-1]
    else:
        ans+=prefix[r-1]- prefix[l-2]
print(ans)
        
        
    