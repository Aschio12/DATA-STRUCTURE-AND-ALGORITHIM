nums = [1,2,3,4,5,6,7]
k = 3
if k==0:
    print(nums)
def rotate(l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r+=1
rotate(0,len(nums)-1)
rotate(0,k-1)
rotate(k,len(nums)-1)