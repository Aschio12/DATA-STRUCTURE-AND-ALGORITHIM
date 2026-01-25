from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=Counter(arr)
    miop=0
    while count[-1]>count[1] or count[-1]%2==1:
        count[-1]-=1
        count[1]+=1
        miop+=1
    print(miop)
    