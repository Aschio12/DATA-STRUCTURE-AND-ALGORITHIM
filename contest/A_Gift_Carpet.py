for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[input() for _ in range(n)]
    i=0
    name="vika" 
    for j in range(m):
        for k in range(n):
            if arr[k][j]==name[i]:
                i+=1
                break
        if i==len(name):
            break
    print("YES" if i==len(name) else "NO")
