for _ in range(int(input())):
    n=int(input())
    s=input()
    a,c="",""
    l,r,t=0,len(s)-1,1
    while t<r:
        a+=s[l]
        c+=s[r]
        if t in a or c:
            print("YES")
            break
        l+=1
        t+=1
        r-=1 
    
    print("YES" if (a+b+c==s) and c!="" else "NO")