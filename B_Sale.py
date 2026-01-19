n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
balance=0
for price in arr:
    if  m==0:
        break
    if price<0:
        balance+=abs(price)
    m-=1
print(balance)