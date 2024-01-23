'''
645. Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
'''

from typing import List


class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    n = len(nums)
    base = set(i+1 for i in range(n))
    ans = [0, 0]
    
    for val in nums:
      if val not in base:
        ans[0] = val
      else:
        base.discard(val)
        
    ans[1] = base.pop()
    
    return ans
        
        
  def findErrorNums(self, nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)
    target = (n + n*n) // 2
    total = 0
    
    for val in nums:
      idx = abs(val)
      total += idx
      
      if nums[idx-1] < 0:
        ans.append(idx)
      else:
        nums[idx-1] = -nums[idx-1] 
      
    ans.append(target - (total - ans[0]))
    # print(target, total)
    
    return ans
  