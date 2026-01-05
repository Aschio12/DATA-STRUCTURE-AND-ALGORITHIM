n=int(input())
stones=list(map(int,input().split()))
ordered=[]
unordered=[]
o,u=0,0
s=sorted(stones)
for orde,inorde in zip(s,stones):
    o+=orde
    u+=inorde
    ordered.append(o)
    unordered.append(u)
for _ in range(int(input())):
    typ,l,r=map(int,input().split())
    if typ==1:
        print(unordered[r-1] if l==1 else unordered[r-1]-unordered[l-2])
    else:
        print(ordered[r-1] if l==1 else ordered[r-1]-ordered[l-2])
    
    