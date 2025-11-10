for _ in range(int(input())):
    a,b=map(int,input().split())
    def f():
        if a==0:
            return("NO")
        if (b*2)%a==0:
            return("YES")
        else:
            return("NO")
    print(f())