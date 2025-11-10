from collections import defaultdict
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[tuple(map(int,input().split())) for _ in range(k)]
    dict=defaultdict(int)
    for a,b in arr:
        dict[a]+=b
    s=list(dict.values())
    s.sort(reverse=True)
    o=min(n,len(s))
    print(sum(s[:o]))