for _ in range(int(input())):
    n,q=map(int,input().split())
    h=list(map(int,input().split()))
    qu=list(map(int,input().split()))
    qu=sorted((val,ind) for ind,val in enumerate(qu))
    prefix=0
    index=0
    ans=[0]*(q)
    for val,ind in (qu):
        while index<n and val>=h[index]:
            prefix+=h[index]
            index+=1
        ans[ind]=str(prefix)
    print(" ".join(ans))
        