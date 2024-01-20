'''
3013. Divide an Array Into Subarrays With Minimum Cost II

You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.
 
Example 1:

Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
Output: 5
Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
Example 2:

Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
Output: 15
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
Example 3:

Input: nums = [10,8,18,9], k = 3, dist = 1
Output: 36
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.

Constraints:

3 <= n <= 10^5
1 <= nums[i] <= 10^9
3 <= k <= n
k - 2 <= dist <= n - 2
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  '''
  the problem essentially ask for the smallest sum of the smallest k-1 numbers in 
  any subarray of nums[i:i+dist+1], for i in range [1, n] and i+dist < n

  use a moving window to store the smallest k-1 numbers in the window:
  - `added` stores the index of the smallest k-1 numebrs
  - `stack` stores the numbers and the values in the `added` (plus those not yet popped)
  - `pool` stores the numebrs and values that's in the subarray, but not yet pulled into
    the `added` list

  we need to maintain the three helper structures:
  1. when moving the left index of i, pop any index that's in added but is smaller than i;
  2. add number that moves into the window to the `pool`;
  3. move numbers from `pool` to `stack`, if `added` has less than k-1 numbers;
  4. swap `pool` and `stack` top of the stack numbers to maintain k-1 smallest numbers in `stack`;
  '''
  def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
    n = len(nums)
    if k == n:
      return sum(nums)
    
    low, curr = float('inf'), 0
    stack = []
    pool = []
    added = set()
    i, j, l = 1, 1, 1
    
    def clean(i):
      # pop any stale states from the stack
      while stack and stack[0][1] < i:
        heappop(stack)

      # pop any stale states from pool
      while pool and pool[0][1] < i:
        heappop(pool)
     
    def add(idx, left):
      while pool and pool[0][1] < left:
        heappop(pool)
        
      heappush(pool, (nums[idx], idx))
      
    for i in range(1, n):
      # not enough numbers left to form k subarrays
      if n-i+1 < k:
        break
        
      # pop any numbers from the added array
      while l < i:
        if l in added:
          curr -= nums[l]
          added.discard(l)
          
        l += 1
        
      # add numbers that can form the head node of the 
      # i_2 to i_k subarrays
      while j < n and j-i <= dist:
        add(j, i)
        j += 1
        
      # clean up any stale states from the pool and stack
      clean(i)
        
      # move smallest pool elements into the added list 
      while pool and len(added) < k-1:
        clean(i)
        if not pool:
          break
          
        # swap element from pool to stack
        val, idx = heappop(pool)
        heappush(stack, (-val, idx))
        
        # update states
        curr += val
        added.add(idx)
        
      # swap heads between pool and stack
      if len(added) < k-1:
        continue
        
      while pool and stack:
        # nothing to swap with
        if -stack[0][0] <= pool[0][0]:
          break
          
        # pop the heads
        v0, i0 = heappop(stack)
        v1, i1 = heappop(pool)
        v0 = -v0

        # push the heads (aka swap)
        heappush(pool, (v0, i0))
        heappush(stack, (-v1, i1))
        
        # update states
        curr += v1 - v0
        added.discard(i0)
        added.add(i1)
      
      # print('iter ===>', (i, j, l, nums[i]), added, curr)
      # print(a)
      # print(b[:k-1])
      
      low = min(low, curr)
    
    return low + nums[0]
        