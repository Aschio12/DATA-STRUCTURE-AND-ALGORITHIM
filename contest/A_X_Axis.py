for _ in range(int(input())):
    x=list(map(int,input().split()))
    ans=[]
    for i in range(len(x)):
        tot=0
        for j in range(len(x)):
            tot+=abs(x[i]-x[j])
        ans.append(tot)
    print(min(ans))