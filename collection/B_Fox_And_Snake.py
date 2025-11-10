n,m=map(int,input().split())
to_right=True
ans=[]
for i in range(n):
    if i%2==0:
        ans.append("#"*m)
    else:
        if to_right:
            ans.append(("."*(m-1))+"#")
            to_right=not to_right
        else:
            ans.append("#"+(".")*(m-1))
            to_right=not to_right

for i in ans:
    print(i)