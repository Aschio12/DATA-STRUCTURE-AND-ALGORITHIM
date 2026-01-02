for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    l,r=0,n-1
    point,ans=0,[]
    current=0
    while l<=r:
        need=x-(current%x)
        if arr[r]>=need:
            current+=arr[r]
            point+=arr[r]
            ans.append(str(arr[r]))
            r-=1
        else:
            current+=arr[l]
            ans.append(str(arr[l]))
            l+=1
    print(point)
    print(" ".join(ans))