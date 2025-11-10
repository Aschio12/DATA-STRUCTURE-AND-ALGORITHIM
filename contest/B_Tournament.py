for _ in range(int(input())):
    n,j,k=map(int,input().split())
    arr=list(map(int,input().split()))
    number=arr[j-1]
    if k==1:
        if number<max(arr):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")