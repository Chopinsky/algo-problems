'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

Constraints:

1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow up: Could you solve the problem in linear time and in O(1) space?
'''


from typing import List
from collections import Counter


class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    n = len(nums)
    c = Counter(nums)
    return [val for val in c if c[val] > n/3.0]
        
        
  def majorityElement(self, nums: List[int]) -> List[int]:
    if not nums:
      return []

    count1, count2, candidate1, candidate2 = 0, 0, 0, 1

    for n in nums:
      if n == candidate1:
        count1 += 1

      elif n == candidate2:
        count2 += 1

      elif count1 == 0:
        candidate1, count1 = n, 1

      elif count2 == 0:
        candidate2, count2 = n, 1

      else:
        count1 -= 1
        count2 -= 1

    ans = []
    if nums.count(candidate1) > len(nums)//3:
      ans.append(candidate1)

    if nums.count(candidate2) > len(nums)//3:
      ans.append(candidate2)

    return ans
    
      
  def majorityElement0(self, nums: List[int]) -> List[int]:
    c = Counter(nums)
    th = len(nums) / 3.0
    ans = []
    
    for val, cnt in c.items():
      if cnt > th:
        ans.append(val)
        
    return ans
    