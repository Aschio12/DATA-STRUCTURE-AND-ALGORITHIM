for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count,i=0,0
    while i <len(a):
        if a[i]>b[i]:
            count+=1
        i+=1
    print(count)