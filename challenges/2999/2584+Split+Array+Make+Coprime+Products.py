'''
2584. Split the Array to Make Coprime Products

You are given a 0-indexed integer array nums of length n.

A split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.

For example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.
Return the smallest index i at which the array can be split validly or -1 if there is no such split.

Two values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.

Example 1:

Input: nums = [4,7,8,15,3,5]
Output: 2
Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
The only valid split is at index 2.
Example 2:


Input: nums = [4,7,15,8,3,5]
Output: -1
Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
There is no valid split.

Constraints:

n == nums.length
1 <= n <= 10^4
1 <= nums[i] <= 10^6
'''

from typing import List


class Solution:
  def findValidSplit(self, nums: List[int]) -> int:
    def sive(top: int) -> List[int]:
      s = [i for i in range(top+1)]
      
      for v0 in range(2, top+1):
        if s[v0] < v0:
          continue
          
        for v1 in range(v0*v0, top+1, v0):
          if s[v1] > v0:
            s[v1] = v0
            
      return s
      
    def factors(val: int):
      f = set()
      while val > 1:
        p = s[val]
        f.add(p)
        val //= p
      
      return f
      
    top = max(nums)
    s = sive(top)
    n = len(nums)
    l, r = factors(nums[0]), set()
    index = -1
    
    for i in range(1, n):
      val = nums[i]
      r |= factors(val)
      # print(l, r)
      
      # there are intersections with factors
      if len(r & l) > 0:
        l |= r
        r.clear()
        index = -1
        
      elif index < 0:
        index = i-1
      
    # print(r)
    return index
  