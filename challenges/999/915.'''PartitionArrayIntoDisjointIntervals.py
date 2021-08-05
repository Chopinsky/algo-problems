'''
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

Note:

2 <= nums.length <= 30000
0 <= nums[i] <= 10 ** 6
It is guaranteed there is at least one way to partition nums as described.
'''


from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
  def partitionDisjoint(self, nums: List[int]) -> int:
    left_max = nums[0]
    running_max = nums[0]
    count = 1
    
    for i in range(1, len(nums)):
      if nums[i] < left_max:
        # the number is smaller than the max in the current left
        # segment, it (and all its left numbers not in left) must
        # be added, and update the left segment max to the current
        # running max
        count = i+1
        left_max = running_max
      elif nums[i] > running_max:
        # otherwise, we only update the running max, leaving the 
        # left segment as [0, count)
        running_max = nums[i]
    
    return count
    
  def partitionDisjoint0(self, nums: List[int]) -> int:
    q = []
    for n in nums:
      heappush(q, n)
      
    # print(q)
    count = defaultdict(int)
    total = 0
    
    for i, n in enumerate(nums):
      if n > q[0]:
        count[n] += 1
        total += 1
        continue
        
      if n == q[0]:
        heappop(q)
        
        while count[q[0]] > 0:
          val = heappop(q)
          count[val] -= 1
          total -= 1
          
        if total == 0:
          return i+1
    
    return 0
    