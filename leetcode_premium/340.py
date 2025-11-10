"""340. Longest Substring with At Most K Distinct Characters
Description
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50"""
#input
s = "eceba"
k = 2
d,l,max_length={},0,0
for r in range(len(s)):
    if s[r] not in d:
        d[s[r]]=1
    else:
        d[s[r]]+=1
    while len(d)>k:
        d[s[l]]-=1
        if d[s[l]]==0:
            del d[s[l]]
        l+=1
    max_length=max(max_length,r-l+1)
print(max_length)
        