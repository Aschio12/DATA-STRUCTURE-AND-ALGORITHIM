n=int(input())
worms=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
maxx=sum(worms)
mark=[0]*(maxx+2)
start,pile=0,1
for i in range(n):
    
    l=start+1
    r=start+worms[i]
    mark[l]+=pile
    mark[r+1]-=pile
    start+=worms[i]
    pile+=1
    
for i in range(1,maxx+1):
    mark[i]+=mark[i-1]
    
for t in q:
    print(mark[t])