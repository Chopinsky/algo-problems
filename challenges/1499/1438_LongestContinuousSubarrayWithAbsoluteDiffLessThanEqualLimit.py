'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def longestSubarray(self, nums: List[int], limit: int) -> int:
    l, r = 0, 0
    n = len(nums)
    high, low = [(-nums[0], 0)], [(nums[0], 0)]
    size = 1
    
    while l < n-1 and r < n-1:
      while r < n-1 and (not high or (abs(nums[r+1]+high[0][0]) <= limit and abs(nums[r+1]-low[0][0]) <= limit)):
        r += 1
        size = max(size, r-l+1)
        heappush(high, (-nums[r], r))
        heappush(low, (nums[r], r))

      l += 1
      while high and high[0][1] < l:
        heappop(high)
        
      while low and low[0][1] < l:
        heappop(low)
      
    return size
  