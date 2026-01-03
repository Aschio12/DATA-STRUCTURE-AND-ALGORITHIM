n=int(input())
arr=list(map(int,input().split()))
tot=sum(arr)
if tot%3!=0 or len(arr)<3:
    print(0)
else:
    target=tot//3
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]
    tot_ways=0
    ways=0
    for i in range(n-1):
        if prefix[i]==target*2:
            tot_ways+=ways
        if prefix[i]==target:
            ways+=1
        
        
    print(tot_ways)
    