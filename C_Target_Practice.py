for _ in range(int(input())):
    tot=0
    for row in range(10):
        s=input()
        for col in range(10):
            if s[col]=="X":
                tot+=min(row,col,9-row,9-col)+1
    print(tot)