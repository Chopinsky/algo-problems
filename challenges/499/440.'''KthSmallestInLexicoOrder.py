'''
Given two integers n and k, return the kth lexicographically 
smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], 
so the second smallest number is 10.

Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 10^9
'''

class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    val = 1
    k -= 1
    
    while k > 0:
      count = 0
      rng = [val, val+1]
      
      # count all numbers between e.g., [123, 124) if 
      # val == 123 and the number is smaller than or 
      # equal to n
      while rng[0] <= n:
        count += min(n+1, rng[1]) - rng[0]
        rng[0] *= 10
        rng[1] *= 10
        
      if k >= count:
        # if k is greater than or equal to the count
        # of numbers in the interval, move on to the
        # next level, aka 124
        k -= count
        val += 1
        
      else:
        # the k-th number is in the [123, 124) range, 
        # keep refining the counts in the [1230, 1231)
        # range and so on
        k -= 1
        val *= 10
      
    return val
    
        
  