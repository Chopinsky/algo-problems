'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Constraints:

n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    n = len(nums)
    nums += nums[:-1]
    # print(nums)
    
    prev_low = [(0, -1)]
    curr = 0
    max_val = nums[0]
    
    for i, val in enumerate(nums):
      while prev_low and i-prev_low[0][1] > n:
        heappop(prev_low)
        
      curr += val
      low = prev_low[0][0] if prev_low else 0
      max_val = max(max_val, curr - low)
      heappush(prev_low, (curr, i))
    
    return max_val


  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    n = len(nums)
    # suffix_high[i] == max sum of a subarray in the range of [k, n) where k >= i
    suffix_high = [0] * n  
    # suffix_susm == current running subarray sum in the range of [i, n)
    suffix_sums = 0
    
    # get correct values for suffix_high
    for i in range(n-1, -1, -1):
      suffix_sums += nums[i]
      suffix_high[i] = max(0, suffix_high[i+1] if i < n-1 else 0, suffix_sums)
      
    # low is the min sum of a subarray in the range of [0, k) where k < i @ i-th index
    prefix_low = 0
    # prefix sum for the subarray [0, i) @ i-th index
    prefix_sums = 0
    # the maximum value for the circular subarray sum
    ans = nums[0]

    for i in range(n):
      # update the running prefix sum for [0, i]
      prefix_sums += nums[i]
      # find the max-sum of the subarray that can exist to the right of index i
      right_high = suffix_high[i+1] if i < n-1 else 0
      
      # 3 possible senarios: 
      # 1) subarray [k, i], where [0, k) sums to the prefix_low;
      # 2) subarray that wrap around index 0 to the right side, where the sum
      #    equals the prefix_sums for [0, i), plus the right side array [k, n)
      #    whose sum makes the highest sum for index in [i, n); note the right
      #    side array could be empty (meaning [0, i) is all we need)
      # 3) previous answer
      ans = max(ans, prefix_sums-prefix_low, prefix_sums+right_high)
      # update the running prefix low
      prefix_low = min(prefix_low, prefix_sums)
      
    return ans