for _ in range(int(input())):
    m,n=map(int,input().split())
    a,b=input(),input()
    ia,ib=0,0
    
    while ia<m and ib<n:
        if a[ia]==b[ib]:
            ia+=1       
        ib+=1
           
    print(ia)
        