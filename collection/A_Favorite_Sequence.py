for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    i,j=0,n-1
    if n>1:
        while i<j:
            ans.append(a[i])
            ans.append(a[j])
            i+=1
            j-=1
    print(*ans if n>1 else str(a[0]))
        