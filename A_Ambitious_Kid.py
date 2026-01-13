n=int(input())
arr=list(map(int,input().split()))
nearest=float("inf")
for i in range(n):
    if abs(arr[i])<nearest:
        nearest=abs(arr[i])
print(nearest)