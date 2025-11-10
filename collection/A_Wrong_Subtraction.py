for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    unvisted,count=[],0
    for i in range(len(s)-1):
        if s[i]=="A":
            s[i],s[i+1]=s[i+1],s[i]
            count+=1
        else:
            unvisted.append(i)
    for i in unvisted:
        if s[i]=="A":
            count+=1
            s[i],s[i+1]=s[i+1],s[i]
    print(count)
            
        