
 def maxSub(st):
     left,length,current_dict=0,1,{}
     for right in range(len(st)):
        if st[right] not in current_dict:
             current_dict[st[right]]=1
        else:
            current_dict[st[right]]+=1
            
        while len(current_dict)>2:
            current_dict[st[left]]-=1
            if current_dict[st[left]]==0:
                del current_dict[st[left]]
            left+=1
        length=max(length,right-left+1)
    return length
return maxSub(s)