'''
2708. Maximum Strength of a Group

You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

Return the maximum strength of a group the teacher can create.

Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.

Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9
'''

from typing import List


class Solution:
  def maxStrength(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    
    pos = []
    neg = []
    zc =0
    
    for val in nums:
      if val > 0:
        pos.append(val)
      elif val < 0:
        neg.append(val)
      else:
        zc += 1
        
    neg.sort()
    popped = 0
    
    if len(neg) % 2 == 1:
      popped = neg.pop()
      
    if not pos and not neg:
      return popped if zc == 0 else 0
    
    base = 1
    for val in pos+neg:
      base *= val
    
    return base
        