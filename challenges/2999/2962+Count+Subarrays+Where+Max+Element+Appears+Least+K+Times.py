'''
2962. Count Subarrays Where Max Element Appears at Least K Times

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5

[1,3,2,3,3]
2
[1,4,2,1]
3
[28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49]
1
'''

from typing import List

class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    top = max(nums)
    n = len(nums)
    cnt = 0
    pos = [-1]
    
    for i in range(n):
      if nums[i] == top:
        pos.append(i)
    
    if len(pos)-1 < k:
      return cnt
    
    # print('init:', pos)
    for i in range(1, len(pos)):
      j = i+k-1
      if j >= len(pos):
        break
        
      left = pos[i]-pos[i-1]
      right = n-pos[j]
      cnt += left*right
      # print('update:', i, left, right)
    
    return cnt
    