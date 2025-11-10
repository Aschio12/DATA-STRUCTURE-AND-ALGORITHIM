for _ in range(int(input())):
    dig="1234567890"     
    num=input()
    i,j=0,0
    count=0
    while i<len(num):
        if num[i]==0:
            count+=(9-j)+2
            j=8
            i+=1
        elif dig[j]>num[i]:
            j-=1
            count+=1
        elif dig[j]<num[i]:
            j+=1
            count+=1
        else:
            count+=1
            i+=1
    print(count)
            
        
        
        