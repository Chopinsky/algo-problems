'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
'''


from typing import List


class Solution:
  def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    # convert numbers to strings
    a = ''.join(map(chr, nums1))
    b = ''.join(map(chr, nums2))
    la, lb = len(a), len(b)
    
    # print(a, b)
    
    # check if substring with length `size` is in both
    # string-a and string-b
    def check(size: int) -> bool:
      nonlocal la, lb
      subarr = set()
      
      for i in range(la-size+1):
        subarr.add(a[i:i+size])
        
      for i in range(lb-size+1):
        if b[i:i+size] in subarr:
          return True
        
      return False
    
    # use binary search to find the length of the substring
    # that can be found in both a and b
    lo, hi = 0, min(la, lb) + 1
    
    while lo < hi:
      mid = hi - (hi-lo) // 2
      
      if check(mid):
        lo = mid
      else:
        hi = mid-1
    
    return lo
    
    
  def findLength0(self, nums1: List[int], nums2: List[int]) -> int:
    m, n = len(nums1), len(nums2)
    longest = 0
    
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        if nums1[i] != nums2[j]:
          continue
          
        dp[i][j] = dp[i-1][j-1] + 1 if i > 0 and j > 0 else 1
        longest = max(longest, dp[i][j])
        
    # print(dp)
    
    return longest


  def findLength00(self, nums1: List[int], nums2: List[int]) -> int:
    m, n = len(nums1), len(nums2)
    dp = {}
    
    def match(i: int, j: int) -> int:
      if (i, j) in dp:
        return dp[i, j]
            
      stack = []
      while i < m and j < n and (i, j) not in dp and nums1[i] == nums2[j]:
        stack.append((i, j))
        i += 1
        j += 1
        
      if i == m or j == n or nums1[i] != nums2[j]:
        cnt = 0
      
      else:
        cnt = dp[i, j]
      
      while stack:
        i, j = stack.pop()
        cnt += 1
        dp[i, j] = cnt
      
      return cnt
      
    cand = set(nums2)
    long = 0
    
    for i in range(m):
      if nums1[i] not in cand:
        continue
        
      j = 0
      while j < n:
        if long >= n-j:
          break
        
        if nums1[i] != nums2[j]:
          j += 1
          continue
          
        ln = match(i, j)
        long = max(long, ln)
        # print(i, j, ln)
        
        if long == m or long == n:
          return long
        
        j += 1
        
      if long >= m-i:
        break
    
    return long
  