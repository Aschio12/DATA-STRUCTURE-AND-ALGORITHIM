"""Description
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.


 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
 

Constraints:

1 <= nums.length <= 2 * 105
-104 <= nums[i] <= 104
-109 <= k <= 109"""

length,current,remainder=0,0,{}
nums = [1,-1,5,-2,3]
k = 3
for r in range(len(nums)):
    current+=nums[r]
    if current-k in remainder:
        length=max(length,r-remainder[current-k])
    if current not in remainder:
        remainder[current]=r
print(length)