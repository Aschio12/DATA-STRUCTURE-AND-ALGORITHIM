s=""
last_index={}
for i in range(len(s)):
    last_index[s[i]]==i
start=0
end=0
ans=[]
for i,char in s:
    end=max(end,last_index[s[i]])
    if i==end:
        ans.append(end-start+1)
        start=i+1
print(ans)
    