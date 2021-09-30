'''
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.

Constraints:

1  <= nums.length <= 1000
-2 ** 31 <= nums[i] <= 2 ** 31 - 1
'''


from collections import defaultdict
from typing import List


class Solution:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    ln = len(nums)
    init_chains = [defaultdict(int) for _ in range(ln)]
    chains = [defaultdict(int) for _ in range(ln)]
    pos = defaultdict(list)
    total = 0
    
    # idea is to save the number of chains ending at position i under 
    # arithmetic diff as the key; then we loop over previous positions
    # and update the number of chains under `diff`; also need to build
    # up chains with 2 elements for future iterations.
    for i, n0 in enumerate(nums):
      # add up all possible chains from a previous position
      for j in range(i):
        n1 = nums[j]

        # n0 == n1 will be evaluated at the end
        if n0 == n1:
          continue
          
        diff = n0 - n1

        # appending n0 to all the chains with the diff and 
        # ending previously at position j
        if diff in chains[j]:
          chains[i][diff] += chains[j][diff]
          total += chains[j][diff]
          
        # adding all the new chains with 3 elements
        if diff in init_chains[j]:
          chains[i][diff] += init_chains[j][diff]
          total += init_chains[j][diff]
      
      # update init chains for n0 (i.e. chain with 2 elements)
      for n1, p in pos.items():
        if n0 == n1:
          continue
          
        diff = n0 - n1
        init_chains[i][diff] += len(p)
      
      pos[n0].append(i)
        
    # print(pos, init_chains, chains)
    
    # adding all the 0-diff chains
    for p in pos.values():
      cnt = len(p)
      if cnt > 2:
        total += (1 << cnt) - 1 - cnt - cnt*(cnt-1)//2
        
    return total
    