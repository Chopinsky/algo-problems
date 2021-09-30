'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''


from collections import defaultdict
from typing import List


class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    ln = len(nums)
    if ln < 4:
      return []

    nums.sort()
    num_count = defaultdict(int)
    sum_pair = defaultdict(set)
    num_set = set()
    
    for n0 in nums:
      for n1 in num_set:
        if (n0, n1) not in sum_pair[n0+n1]:
          sum_pair[n0+n1].add((n0, n1))
        
      num_count[n0] += 1
      num_set.add(n0)
      
    quadruplets = set()
    
    for s, pairs in sum_pair.items():
      other = target - s
      if other not in sum_pair:
        continue
        
      for p0 in pairs:
        for p1 in sum_pair[other]:
          key = tuple(sorted([p0[0], p0[1], p1[0], p1[1]]))
          if key in quadruplets:
            continue
          
          done = True
          counter = defaultdict(int)
          counter[p0[0]] += 1
          counter[p0[1]] += 1
          counter[p1[0]] += 1
          counter[p1[1]] += 1
          
          for num, count in counter.items():
            if count > num_count[num]:
              done = False
              break
              
          if done:
            quadruplets.add(key)
      
    # print(quadruplets)
    ans = []
    for q in quadruplets:
      ans.append(list(q))
    
    return ans
      