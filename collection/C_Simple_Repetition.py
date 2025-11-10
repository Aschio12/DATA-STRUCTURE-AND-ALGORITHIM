for _ in range(int(input())):
    x,k=map(int,input().split())
    new_p=int(str(x)*k)
    if new_p<2:
        print("NO")
    else:
        for i in range(2,int((new_p**0.5))-1):
            if new_p%i==0:
                print("NO")
                break
        else:
            print("YES")
    
    