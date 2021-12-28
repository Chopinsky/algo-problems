'''
A sequence is special if it consists of a positive number of 0s, followed by a positive number of 1s, then a positive number of 2s.

For example, [0,1,2] and [0,0,1,1,1,2] are special.
In contrast, [2,1,0], [1], and [0,1,2,0] are not special.
Given an array nums (consisting of only integers 0, 1, and 2), return the number of different subsequences that are special. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are different if the set of indices chosen are different.

Example 1:

Input: nums = [0,1,2,2]
Output: 3
Explanation: The special subsequences are bolded [0,1,2,2], [0,1,2,2], and [0,1,2,2].
Example 2:

Input: nums = [2,2,0,0]
Output: 0
Explanation: There are no special subsequences in [2,2,0,0].
Example 3:

Input: nums = [0,1,2,0,1,2]
Output: 7
Explanation: The special subsequences are bolded:
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 2
'''

from typing import List


class Solution:
  def countSpecialSubsequences(self, nums: List[int]) -> int:
    mod = 1_000_000_007
    ways = [0, 0, 0]
    
    for val in nums:
      if val == 0:
        # plus append 0 to all previous subseq only containing 0, plus
        # the sole subseq with this 0
        ways[0] = (2*ways[0] + 1) % mod
        
      elif val == 1:
        # all existing subseq, plus append this 1 to all previously 
        # valid subseq ending with 1, plus all previously possible 
        # subseq only with 0 that will now end with this 1.
        ways[1] = (2*ways[1] + ways[0]) % mod
        
      else:
        # same analysis as the case of val == 1
        ways[2] = (2*ways[2] + ways[1]) % mod
        
        
    return ways[-1]
    