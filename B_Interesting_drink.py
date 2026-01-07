n=int(input())
arr=list(map(int,input().split()))
maxx=200000
mark=[0]*(200000+1)
for price in arr:
    mark[price]+=1
for i in range(1,len(mark)):
    mark[i]=mark[i-1]+mark[i]
for _ in range(int(input())):
    m=int(input())
    if m>maxx:
        print(mark[maxx])
    else:
        print(mark[m])
        
