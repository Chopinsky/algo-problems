'''
2442. Count Number of Distinct Integers After Reverse Operations

You are given an array nums consisting of positive integers.

You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array.

Example 1:

Input: nums = [1,13,10,12,31]
Output: 6
Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).
Example 2:

Input: nums = [2,2,2]
Output: 1
Explanation: After including the reverse of each number, the resulting array is [2,2,2,2,2,2].
The number of distinct integers in this array is 1 (The number 2).

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''

from typing import List
from functools import lru_cache


class Solution:
  def countDistinctIntegers(self, nums: List[int]) -> int:
    base = set(nums)
    
    @lru_cache(None)
    def rev(val: int) -> int:
      return int(str(val)[::-1])
    
    for val in list(base):
      rval = rev(val)
      # print(val, rval)
      base.add(rval)
      
    return len(base)
    