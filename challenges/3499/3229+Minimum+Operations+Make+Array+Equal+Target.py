'''
3229. Minimum Operations to Make Array Equal to Target

You are given two positive integer arrays nums and target, of the same length.

In a single operation, you can select any subarray of nums and increment or decrement each element within that subarray by 1.

Return the minimum number of operations required to make nums equal to the array target.

Example 1:

Input: nums = [3,5,1,2], target = [4,6,2,4]

Output: 2

Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..3] by 1, nums = [4,6,2,3].
- Increment nums[3..3] by 1, nums = [4,6,2,4].

Example 2:

Input: nums = [1,3,2], target = [2,1,4]

Output: 5

Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..0] by 1, nums = [2,3,2].
- Decrement nums[1..1] by 1, nums = [2,2,2].
- Decrement nums[1..1] by 1, nums = [2,1,2].
- Increment nums[2..2] by 1, nums = [2,1,3].
- Increment nums[2..2] by 1, nums = [2,1,4].

Constraints:

1 <= nums.length == target.length <= 10^5
1 <= nums[i], target[i] <= 10^8

Test cases:

[9,2,6,10,4,8,3,4,2,3]
[9,5,5,1,7,9,8,7,6,5]
[3,5,1,2]
[4,6,2,4]
[1,3,2,2]
[2,1,2,4]
'''

from typing import List

class Solution:
  def minimumOperations(self, nums: List[int], target: List[int]) -> int:
    if len(nums) != len(target):
      return -1
    
    ops = 0
    n = len(nums)
    
    def make_peak(idx: int, bumps: List):
      if idx >= n:
        return idx
      
      rng = []
      peak = -1
      prev = -1
      stage = 0
      
      while idx < n:
        diff = target[idx] - nums[idx]
        if diff <= 0:
          break
        
        if stage == 2 and diff > prev:
          break
          
        if stage == 1 and diff < peak:
          # start the down slop
          stage += 1
          
        if stage == 0:
          # init of the up slop
          rng.append(idx)
          rng.append(idx)
          stage += 1
        
        peak = max(peak, diff)
        prev = diff
        rng[-1] = idx
        idx += 1
      
      if rng:
        bumps.append((rng, peak))
      
      return idx
    
    def make_valley(idx: int, bumps: List):
      if idx >= n:
        return idx

      rng = []
      peak = 1
      prev = 1
      stage = 0
      
      while idx < n:
        diff = target[idx] - nums[idx]
        if diff >= 0:
          break
        
        if stage == 2 and diff < prev:
          break
          
        if stage == 1 and diff > peak:
          # start the down slop
          stage += 1
          
        if stage == 0:
          # init of the up slop
          rng.append(idx)
          rng.append(idx)
          stage += 1
        
        peak = min(peak, diff)
        prev = diff
        rng[-1] = idx
        idx += 1
      
      if rng:
        bumps.append((rng, peak))
        
      return idx
      
    def make_bumps():
      bumps = []
      idx = 0
      
      while idx < n:
        v0 = nums[idx]
        v1 = target[idx]

        if v0 == v1:
          idx += 1
          continue

        if v1 > v0:
          idx = make_peak(idx, bumps)
        else:
          idx = make_valley(idx, bumps)
          
      return bumps
      
    bumps = make_bumps()
    prev_end = -1
    prev_ht = -1
    # print(bumps)
    
    for rng, ht in bumps:
      if prev_end >= 0 and ht*prev_ht > 0 and rng[0] == prev_end+1:
        diff = target[prev_end] - nums[prev_end]
        ops += abs(ht - diff)
      else:
        ops += abs(ht)
      
      prev_end = rng[1]
      prev_ht = ht
    
    return ops
        
