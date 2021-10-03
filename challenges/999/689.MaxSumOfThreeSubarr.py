'''
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i] < 2^16
1 <= k <= floor(nums.length / 3)
'''


from typing import List
from itertools import accumulate


class Solution:
  def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    i0, i1, i2 = 0, k, 2*k
    s0, s1, s2 = sum(nums[:i1]), sum(nums[i1:i2]), sum(nums[i2:i2+k])
    best0, best1, best2 = s0, s0+s1, s0+s1+s2
    box0, box1, box2 = [i0], [i0, i1], [i0, i1, i2]
    n = len(nums)
    
    while i0 < n-3*k:
      i0 += 1
      
      if i1 < n-2*k:
        i1 += 1
        s1 += nums[i1+k-1] - nums[i1-1]
      
      if i2 < n-k:
        i2 += 1
        s2 += nums[i2+k-1] - nums[i2-1]
        
      s0 += nums[i0+k-1] - nums[i0-1]
      if s0 > best0:
        best0 = s0
        box0[0] = i0
        
      if s1+best0 > best1:
        best1 = s1 + best0
        box1 = box0 + [i1]
      
      if s2+best1 > best2:
        best2 = s2 + best1
        box2 = box1 + [i2]
    
    return box2
    
    
  def maxSumOfThreeSubarrays0(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    presums = list(accumulate(nums))
    three_sums = [presums[i] - (presums[i-k] if i >= k else 0) for i in range(k-1, n)]
    base_one = sorted([(val, i) for i, val in enumerate(three_sums)], key=lambda x: (x[0], -x[1]))
    jump_one = []
    
    for i in range(k, n-2*k+1):
      while base_one and base_one[-1][1] < i+k:
        base_one.pop()
        
      jump_one.append((three_sums[i] + base_one[-1][0], i, base_one[-1][1]))
    
    ans = None
    ans_sum = 0
    base_two = sorted([val for val in jump_one], key=lambda x: (x[0], -x[1], -x[2]))
    # print("base one:", base_one)
    # print("jump one:", jump_one)
    # print('base two:', base_two)
    
    for i in range(n-3*k+1):
      while base_two and base_two[-1][1] < i+k:
        base_two.pop()
        
      total = three_sums[i] + base_two[-1][0]
      # print(i, total)
      
      if not ans_sum or ans_sum < total:
        ans = [i, base_two[-1][1], base_two[-1][2]]
        ans_sum = total
    
    return ans
  
