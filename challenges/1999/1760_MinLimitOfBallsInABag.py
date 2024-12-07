'''
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

Example 1:

Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
Example 2:

Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.
Example 3:

Input: nums = [7,17], maxOperations = 2
Output: 7
 

Constraints:

1 <= nums.length <= 10^5
1 <= maxOperations, nums[i] <= 10^9
'''

from typing import List


class Solution:
  def minimumSize(self, nums: List[int], maxOps: int) -> int:
    l, r = 1, max(nums)
    last = r
    
    def check(th: int) -> bool:
      if th >= last:
        return True
      
      ops = 0
      for cnt in nums:
        if cnt <= th:
          continue
          
        extra_ops = (cnt//th) - (1 if cnt%th == 0 else 0)
        ops += extra_ops
      
      # print('check:', th, ops)
      return ops <= maxOps
      
    while l <= r:
      mid = (l + r) // 2
      if check(mid):
        last = mid
        r = mid-1
      else:
        l = mid+1
    
    return last
    
  def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    def cnt_op(d: int) -> int:
      op = 0
      for val in nums:
        if val <= d:
          continue
          
        size = val//d + (0 if val%d == 0 else 1)
        op += size-1
        
      return op
    
    l, r = 1, max(nums)+1
    last = r
    
    while l < r:
      m = (l + r) // 2
      op = cnt_op(m)
      
      if op <= maxOperations:
        last = m
        r = m - 1
      else:
        l = m + 1
        
    return min(last, l) if cnt_op(l) <= maxOperations else last
    