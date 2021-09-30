'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 10^4
The frequency of each element is in the range [1, 4].
'''


from typing import List, Tuple
from collections import Counter


class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if k == 1:
      return True
    
    total = sum(nums)
    if total % k != 0:
      # print('out-00', k, total)
      return False
    
    if k > total:
      # print('out-01', k, total)
      return False
    
    c = Counter(nums)
    if k == total:
      # print('out-1', c)
      return (len(c) == 1) and (1 in c)
    
    avg = total // k    
    if avg in c:
      if c[avg] > k:
        # print('out-20', c, avg, k)
        return False
      
      if c[avg] == k:
        # print('out-21', c, avg, k)
        return len(c) == 1
      
      k -= c[avg]
      c.pop(avg, None)
      
    nums = sorted(c)
    # print(c, nums)
    
    if nums[-1] > avg:
      # print('out-3')
      return False
    
    def allocate(tgt: int, idx: int) -> List[Tuple[int, int]]:
      # print('top ... ', tgt, idx, nums, c)
      if tgt < 0 or idx < 0:
        return None
      
      val = nums[idx]
      if tgt < val or not c[val]:
        return allocate(tgt, idx-1)
        
      if idx == 0:
        return [(val, tgt//val)] if (tgt%val == 0 and tgt//val <= c[val]) else None
        
      upper = min(c[val], tgt // val)
      # print('iter ... ', upper)
      
      for i in range(upper, -1, -1):
        if tgt == val*i:
          return [(val, tgt//val)]
        
        arr = allocate(tgt-val*i, idx-1)
        if arr:
          arr.append((val, i))
          return arr
          
      return None
      
    for i in range(k):
      arr = allocate(avg, len(nums)-1)
      if not arr:
        # print('out-4', i, k)
        return False
      
      for val, cnt in arr:
        c[val] -= cnt
        
      while nums and not c[nums[-1]]:
        nums.pop()
    
    return True
  