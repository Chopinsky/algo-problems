'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]

Constraints:

1 <= nums.length <= 10 ** 5
-10 ** 4 <= nums[i] <= 10 ** 4
'''


from typing import List
import math


class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    n = len(nums)
    idx = [0] * (n+1)
    ans = [0] * n
    nums = sorted((val, i) for i, val in enumerate(nums))
    # print(idx, nums)
    
    last = math.inf
    stack = []
    
    def update(i: int):
      i += 1
      while i < len(idx):
        idx[i] += 1
        i += (i & -i)
        
    def query(i: int):
      cnt = 0
      i += 1
      
      while i > 0:
        cnt += idx[i]
        i -= (i & -i)
        
      return cnt
    
    total = 0
    for val, i in nums:
      if val != last:
        for j in stack:
          update(j)
          total += 1
          
        last = val
        stack.clear()
        
      ans[i] = total - query(i)
      stack.append(i)
    
    return ans


  def countSmaller(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0 for _ in range(n)]
    
    lo, hi = min(nums), max(nums)
    rng = hi-lo
    fenwick = [0 for _ in range(rng+1)]
    
    def update(idx: int):
      idx += 1
      
      while idx <= rng:
        fenwick[idx] += 1
        idx += (idx & -idx)
        
      return
    
    def query(idx: int) -> int:
      s = 0
      idx += 1
      
      while idx > 0:
        s += fenwick[idx]
        idx -= (idx & -idx)
        
      return s
    
    for i in range(n-1, -1, -1):
      if i < n-1:
        ans[i] = query(nums[i]-1-lo)
        # print(i, nums[i], fenwick)
      
      update(nums[i]-lo)
    
    return ans
    