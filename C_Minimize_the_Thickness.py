for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    prefix,current,tot=[],0,sum(arr)
    ans=n
    for i in range(len(arr)):
        current+=arr[i]
        if tot%current==0:
            valid=True
            l,m_tot,m_max=i+1,0,i+1
            for r in range(i+1,n):
                m_tot+=arr[r]
                if m_tot==current:
                    m_max=max(m_max,r-l+1)
                    l=r+1
                    m_tot=0
                elif m_tot>current:
                    valid=False
                    break
            if valid:
                ans=min(ans,m_max)
    print(ans)
                    
                
        