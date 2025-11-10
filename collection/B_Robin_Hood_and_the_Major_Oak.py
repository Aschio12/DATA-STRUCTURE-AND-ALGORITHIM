for _ in range(int(input())):
    n,k=map(int,input().split())
    grow,dif=[],n-k
    ans,step=0,1
    for i in range(1,n+1):
        ans+=i*i
    while n>k:
        ans-=step*step
        step+=1
        n-=1
    print("YES" if ans%2==0 else "NO")
