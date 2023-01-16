'''
2537. Count the Number of Good Subarrays

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^9
'''

from typing import List
from collections import defaultdict


class Solution:
  def countGood(self, nums: List[int], k: int) -> int:
    i, j = 0, 0
    c = defaultdict(int)
    n = len(nums)
    count = 0
    pairs = 0
    
    while j < n:
      v0 = nums[j]
      pairs += c[v0]
      c[v0] += 1
      
      while i < j:
        v1 = nums[i] 
        p1 = c[v1] - 1
        if pairs - p1 < k:
          break
        
        pairs -= p1
        c[v1] -= 1
        i += 1
      
      if pairs >= k:
        count += (i + 1)
        
      j += 1
      
    return count
    