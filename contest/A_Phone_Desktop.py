for _ in range(int(input())):
    one,two=map(int,input().split())
    x,y,screen=5,3,1
    reqx=one*1+two*2
    reqy=one*1+two*2
    if reqx<=x and reqy<y:
        print(screen)
        
    
    