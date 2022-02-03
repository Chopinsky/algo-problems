'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

Example 1:

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Example 2:

Input: nums = [4,14,4]
Output: 4
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^9
The answer for the given input will fit in a 32-bit integer.
'''


from typing import List
from collections import defaultdict


class Solution:
  def totalHammingDistance(self, nums: List[int]) -> int:
    d = defaultdict(int)
    n = len(nums)
    
    for val in nums:
      pos = 0
      while val > 0:
        if val & 1 > 0:
          d[pos] += 1
          
        val >>= 1
        pos += 1
        
    # print(d)
    dist = 0
    
    for cnt in d.values():
      if cnt == n:
        continue
        
      dist += cnt * (n-cnt)
    
    return dist
  