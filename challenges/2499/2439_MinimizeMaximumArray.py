'''
2439. Minimize Maximum of Array

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

Constraints:

n == nums.length
2 <= n <= 10^5
0 <= nums[i] <= 10^9
'''

from functools import lru_cache
from typing import List


class Solution:
  def minimizeArrayValue(self, nums: List[int]) -> int:
      stack = []
      n, idx = len(nums), 0
      
      @lru_cache(None)
      def get_seg(s: int, c: int):
        avg = s // c
        return (avg, avg) if s%c == 0 else (avg, avg+1)

      while idx < n:
        sums = nums[idx]
        cnt = 1

        while idx < n-1 and nums[idx] <= nums[idx+1]:
          idx += 1
          sums += nums[idx]
          cnt += 1

        l, r = get_seg(sums, cnt)
        
        # we can merge with the previous segment
        while stack and stack[0] < r:
          _, _, s0, c0 = stack.pop()
          sums += s0
          cnt += c0
          l, r = get_seg(sums, cnt)
          
        stack.append((l, r, sums, cnt))
        idx += 1
        
      return max(state[1] for state in stack)


  def minimizeArrayValue0(self, nums: List[int]) -> int:
    def shuffle(nums):
      max_val = -1
      n = len(nums)
      idx = 0
      nxt = []
      
      while idx < n:
        sums = nums[idx]
        cnt = 1
        start = idx

        while idx < n-1 and nums[idx] <= nums[idx+1]:
          idx += 1
          sums += nums[idx]
          cnt += 1

        local_max = sums // cnt
        rem = sums % cnt
        
        if rem != 0:
          local_max += 1
          for jdx in range(start, idx+1):
            if idx-jdx < rem:
              nxt.append(local_max)
            else:
              nxt.append(local_max-1)
              
        else:
          nxt += [local_max] * (idx-start+1)
          
        max_val = max(max_val, local_max)
        idx += 1
        
      return max_val, nxt
    
    last = 0
    max_val = -1
    
    while last != max_val:
      last = max_val
      max_val, nums = shuffle(nums)
      # print(max_val, nums)
    
    return max_val
    