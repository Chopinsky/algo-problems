'''
3266. Final Array State After K Multiplication Operations II

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
After the k operations, apply modulo 109 + 7 to every value in nums.

Return an integer array denoting the final state of nums after performing all k operations and then applying the modulo.

Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]
After applying modulo	[8, 4, 6, 5, 6]
Example 2:

Input: nums = [100000,2000], k = 2, multiplier = 1000000

Output: [999999307,999999993]

Explanation:

Operation	Result
After operation 1	[100000, 2000000000]
After operation 2	[100000000000, 2000000000]
After applying modulo	[999999307, 999999993]

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^9
1 <= k <= 10^9
1 <= multiplier <= 10^6
'''

from heapq import heappush, heappop
from typing import List

class Solution:
  '''
  this is a tricky math problem: one must realize that after about O(log(max(nums)))
  operations, the array will converge to a point where min(nums)*multpilier > max(nums),
  which means after that point, the operation will just apply on each item in the nums 
  sequencially, so we can skip rounghly `k // n` rounds because it will evenly apply to 
  each item in the array; so we only simulate the operations for the pre and post part
  of the `k//n` round, and we're done;
  '''
  def getFinalState(self, nums: List[int], k: int, mult: int) -> List[int]:
    n = len(nums)
    mod = 10**9 + 7
    
    if n == 1:
      return [(nums[0]*pow(mult, k, mod)) % mod]
    
    if mult == 1:
      return [val%mod for val in nums]
    
    stack = sorted((nums[i], i) for i in range(n))
    max_val = stack[-1][0]
    
    def op():
      val, i = heappop(stack)
      val *= mult
      heappush(stack, (val, i))
      return val
    
    while k > 0 and stack[0][0]*mult <= max_val:
      max_val = max(max_val, op())
      k -= 1
    
    rnd, k = divmod(k, n)
    # print('pre:', stack, max_val, k)
    # print('mid:', rnd, k)

    while k > 0:
      max_val = max(max_val, op())
      k -= 1
    
    base = pow(mult, rnd, mod)
    # print('done:', stack, base)
    
    for val, i in stack:
      nums[i] = (val * base) % mod
      
    return nums
        