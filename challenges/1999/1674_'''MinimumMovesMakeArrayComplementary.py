'''
1674. Minimum Moves to Make Array Complementary

You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.

Constraints:

n == nums.length
2 <= n <= 10^5
1 <= nums[i] <= limit <= 10^5
n is even.
'''

from typing import List
from collections import defaultdict


class Solution:
  '''
  the idea is to calculate how many ops the pair needs to perform for each target
  sum that's the answer for all pairs; we just update deltas that will affect the
  final operations sum, then adding them together from small to large will give
  us the operations required for number `i` if it's the target sum for all pairs.
  '''
  def minMoves(self, nums: List[int], limit: int) -> int:
    n = len(nums)
    delta = defaultdict(int)
    i, j = 0, n-1
    
    while i < j:
      a, b = nums[i], nums[j]
      
      # 2 ops for 2 <= tgt_sum < min(a, b)+1
      delta[2] += 2
      
      # 1 op for min(a, b)+1 <= tgt_sum < a+b
      delta[min(a, b)+1] -= 1
      
      # 0 op for tgt_sum == a+b
      delta[a+b] -= 1
      
      # 1 op for a+b+1 <= tgt_sum < max(a, b) + limit + 1
      delta[a+b+1] += 1
      
      # 2 ops for max(a, b)+limit+1 <= tgt_sum <= 2*limit
      delta[max(a, b)+limit+1] += 1
      
      i += 1
      j -= 1
      
    # print(counter)
    res = n
    curr = 0
    # todo
    
    for i in sorted(delta):
      curr += delta[i]
      res = min(res, curr)
    
    return res
    