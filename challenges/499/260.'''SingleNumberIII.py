'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]

Constraints:

2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
'''


from typing import List


class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    double = 0
    k = 0
    
    # get the a^b where a and b only appears once
    for num in nums:
      double ^= num
        
    # get the 1st non-zero bit from the a^b, this is
    # where the first bit that a differs from b (assuming
    # a has 1 and b has 0 at this bit)
    while double & (1 << k) == 0:
      k += 1

    c = 1 << k
    elem1 = 0
    elem2 = 0
    
    # separate the nums into 2 groups: the group with 
    # 1 at the k-th bit, and the group with 0 at the
    # k-th bit, each group has only 1 number that appears
    # once, and we can cancel everything else out
    for num in nums:
      if num & c > 0:
        elem1 ^= num
      else:
        elem2 ^= num

    return [elem1, elem2]
  
  
  def singleNumber0(self, nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 2:
      return nums
    
    seen = set()
    for val in nums:
      if val not in seen:
        seen.add(val)
      else:
        seen.discard(val)
        
    return list(seen)