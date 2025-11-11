for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ans,lower,upper=-1,min(arr),max(arr)
    while k>0:
        for i in arr:
            if lower+k==abs(upper-k):
                ans=lower+k
                break
        k-=1
    print(ans)