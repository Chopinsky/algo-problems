'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''


from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
  '''
  The idea is to loop over all mid in the numbers from the tuple (left, mid, right),
  then we can narrow down the window -- if the tuple sum is smaller than the target,
  we move the left bound; otherwise, move the right bounds, until we reach a point the
  tuple sum is the closet to the target. 
  '''
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    ans = float('inf')

    for i in range(len(nums)-2):
      # print("iterate: ", i, ans)
      if i > 0 and nums[i-1] == nums[i]:
        continue

      minsum = nums[i] + nums[i+1] + nums[i+2]
      maxsum = nums[i] + nums[-1] + nums[-2]
      #print(f'ini minsum: {minsum} maxsum {maxsum} , nnn {nums[i], nums[-1], nums[-2]}')

      if minsum >= target:
        if abs(minsum-target) >= abs(ans-target):
          #print(f"minsum - target {abs(minsum-target)} ans {abs(ans-target):}")
          return ans

      if maxsum < target:
        if abs(maxsum-target) < abs(ans-target):
          #print(f"maxsum - target: {abs(maxsum-target)} ans: {abs(ans-target):}")
          ans = maxsum

        #print("ans", ans)
        continue

      left, right = i+1, len(nums)-1
      while left < right:
        #print(f'left: {left}  right: {right} -> {ans}')
        thsum = nums[i] + nums[left] + nums[right]

        if abs(thsum - target) < abs(ans - target):
          ans = thsum

        if thsum == target:
          return thsum

        elif thsum < target:
          left += 1
          while left < len(nums)-1 and nums[left-1] == nums[left]:
            left += 1

        else:
          right -= 1
          while right > i and nums[right+1] == nums[right]:
            right -= 1

    return ans
      
  def threeSumClosest1(self, nums: List[int], target: int) -> int:
    ans = sum(nums[:3])
    if len(nums) == 3:
      return ans
    
    count = defaultdict(int)
    for n in nums:
      count[n] += 1
    
    unique = sorted(count.keys())
    lu = len(unique)
    nums = sorted(nums)
    pairs = set()
    
    # print(unique, nums)
    
    def is_valid(vi: int, vj: int, vk: int) -> bool:
      d = defaultdict(int)
      d[vi] += 1
      d[vj] += 1
      d[vk] += 1
      
      return d[vi] <= count[vi] and d[vj] <= count[vj] and d[vk] <= count[vk]
    
    for i in range(lu):
      for j in range(i, lu):
        vi, vj = unique[i], unique[j]
        p = (vi, vj) if vi <= vj else (vj, vi)
        if p in pairs:
          continue
        
        if i == j and count[vi] < 2:
          continue
          
        val = target - vi - vj
        idx = bisect_right(nums, val)
        
        # if idx >= len(nums):
        #   continue
          
        if idx < len(nums) and is_valid(vi, vj, nums[idx]):
          if abs(target-ans) > abs(target-vi-vj-nums[idx]):
            ans = vi+vj+nums[idx]
    
        if idx > 0 and is_valid(vi, vj, nums[idx-1]):
          if abs(target-ans) > abs(target-vi-vj-nums[idx-1]):
            ans = vi+vj+nums[idx-1]
        
        pairs.add(p)
        
    return ans
  