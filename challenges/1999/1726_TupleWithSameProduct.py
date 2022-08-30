'''
1726. Tuple with Same Product

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^4
All elements in nums are distinct.
'''

from typing import List
from collections import defaultdict
from math import comb


class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    nums.sort()
    product = defaultdict(int)
    n = len(nums)
    
    if n < 4:
      return 0
    
    for i in range(n-1):
      for j in range(i+1, n):
        product[nums[i]*nums[j]] += 1
        
    # print(product)
    cnt = 0
    
    for val in product.values():
      if val < 2:
        continue
        
      cnt += comb(val, 2) * 8
    
    return cnt
    