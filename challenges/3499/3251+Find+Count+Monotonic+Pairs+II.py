'''
3251. Find the Count of Monotonic Pairs II

You are given an array of positive integers nums of length n.

We call a pair of non-negative integer arrays (arr1, arr2) monotonic if:

The lengths of both arrays are n.
arr1 is monotonically non-decreasing, in other words, arr1[0] <= arr1[1] <= ... <= arr1[n - 1].
arr2 is monotonically non-increasing, in other words, arr2[0] >= arr2[1] >= ... >= arr2[n - 1].
arr1[i] + arr2[i] == nums[i] for all 0 <= i <= n - 1.
Return the count of monotonic pairs.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: nums = [2,3,2]

Output: 4

Explanation:

The good pairs are:

([0, 1, 1], [2, 2, 1])
([0, 1, 2], [2, 2, 0])
([0, 2, 2], [2, 1, 0])
([1, 2, 2], [1, 1, 0])
Example 2:

Input: nums = [5,5,5,5]

Output: 126

Constraints:

1 <= n == nums.length <= 2000
1 <= nums[i] <= 1000

[2,3,2]
[5,5,5,5]
[16,5]
[30,1,37]
'''

from typing import List

class Solution:
  '''
  this is a very typical DP problem: at each position i, assuming the value at arr1 and arr2 are
  a1 and a2, and a1+a2 == v1, i.e., (a1, a2), then the possible suffix arrays that are allowed are:
      `count(a1, a2) = sum(count(b1, b2) for (b1+b2 == v2) and b1 >= a1 and 0 <= b2 <= a2)`
  given that if we reduce a1 from v1 to 0, the `sum` part of the equation above is essentially a
  prefix sum (with a1 reduce by 1, we will have 1 new state available to transition, aka from (b1, b2)
  to (a1, a2)), and use the prefix sum we can set the total suffix arrays that are valid for (a1, a2).
  '''
  def countOfPairs(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    n = len(nums)
    bound = max(nums)+1
    curr = [1 if i <= nums[-1] else 0 for i in range(bound)]
    # print('init:', curr)
    
    for i in range(n-2, -1, -1):
      prev = curr
      curr = [0]*bound
      
      aval = nums[i]
      bval = nums[i+1]
      prefix = 0
      
      a0, a1 = aval, 0
      b0, b1 = bval, 0
      
      while a0 >= 0:
        while b0 >= a0 and b1 <= a1:
          prefix = (prefix+prev[b0]) % mod
          b0 -= 1
          b1 += 1
        
        curr[a0] = prefix
        a0 -= 1
        a1 += 1
    
    return sum(curr) % mod
  