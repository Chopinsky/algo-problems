'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Constraints:

1 <= nums.length <= 10^4
-10^7 <= nums[i] <= 10^7
0 <= k <= 10^7
'''


from typing import List


class Solution:
  def findPairs(self, nums: List[int], k: int) -> int:
    vals = set()
    seen = set()
    n = len(nums)
    
    for val in nums[::-1]:
      if val+k in vals:
        # print(1, val, val+k, seen, vals)
        seen.add((val, val+k))
        
      if val-k in vals:
        # print(2, val, val-k, seen, vals)
        seen.add((val-k, val))
      
      vals.add(val)
      
    return len(seen)
  