'''
2659. Make Array Empty

You are given an integer array nums containing distinct numbers, and you 
can perform the following operations until the array is empty:

- If the first element has the smallest value, remove it
- Otherwise, put the first element at the end of the array.

Return an integer denoting the number of operations it takes to make nums empty.

Example 1:

Input: nums = [3,4,-1]
Output: 5
Operation	Array
1	[4, -1, 3]
2	[-1, 3, 4]
3	[3, 4]
4	[4]
5	[]
Example 2:

Input: nums = [1,2,4,3]
Output: 5
Operation	Array
1	[2, 4, 3]
2	[4, 3]
3	[3, 4]
4	[4]
5	[]
Example 3:

Input: nums = [1,2,3]
Output: 3
Operation	Array
1	[2, 3]
2	[3]
3	[]

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
All values in nums are distinct.
'''

from typing import List

class Solution:
  def countOperationsToEmptyArray(self, nums: List[int]) -> int:
    tgt = sorted((val, i) for i, val in enumerate(nums))
    n = len(nums)
    fenwick = [0]*n
    
    def update(idx, val):
      if idx == 0:
        fenwick[idx] += val
        return
      
      while idx < n:
        fenwick[idx] += val
        idx += (idx & -idx)
        
    def query(idx):
      res = fenwick[0]
      while idx > 0:
        res += fenwick[idx]
        idx -= (idx & -idx)
      
      return res
    
    for i in range(n):
      update(i, 1)
      
    ops = 0
    last = -1
    
    for i in range(n):
      idx = tgt[i][1]
      if idx >= last:
        ops += query(idx) - (0 if last < 0 else query(last))
      else:
        right = query(n-1) - query(last)
        left = query(idx)
        ops += right + left
        
      update(idx, -1)
      last = idx
    
    return ops
        