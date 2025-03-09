'''
2523. Closest Prime Numbers in Range

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= nums1 < nums2 <= right .
nums1 and nums2 are both prime numbers.
nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

Constraints:

1 <= left <= right <= 10^6
'''

from typing import List
from bisect import bisect_left
import math


primes = []
nums = [i for i in range(10**6)]
for val in range(2, len(nums)):
  if nums[val] < val:
    continue

  primes.append(val)
  for v0 in range(val*val, len(nums), val):
    if nums[v0] == v0:
      nums[v0] = val


class Solution:
  def closestPrimes(self, left: int, right: int) -> List[int]:
    # print('init', primes)
    l = bisect_left(primes, left)
    if l >= len(primes):
      return [-1, -1]

    idx = l+1
    prev = primes[l]
    diff = math.inf
    ans = [-1, -1]

    while idx < len(primes) and primes[idx] <= right:
      curr = primes[idx] - prev
      if curr < diff:
        diff = curr
        ans = [prev, primes[idx]]

      prev = primes[idx] 
      idx += 1

    return ans
        
  def is_prime(self, num: int) -> bool:
    if num == 1:
      return False

    for divisor in range(2, math.floor(math.sqrt(num)) + 1):
      if num % divisor == 0:
        return False

    return True


  def closestPrimes(self, left: int, right: int) -> list[int]:
    primes = []
    for candidate in range(left, right + 1):
      if self.is_prime(candidate):
        if primes and candidate <= primes[-1] + 2:
          return [primes[-1], candidate]  # twin or [2, 3]
          
        primes.append(candidate)
    
    gaps = ([primes[i - 1], primes[i]] for i in range(1, len(primes)))

    return min(gaps, key=lambda gap: (gap[1] - gap[0], gap[0]), default=[-1, -1])


  def closestPrimes(self, left: int, right: int) -> List[int]:
    s = [i for i in range(right+1)]
    primes = []

    for v0 in range(2, right+1):
      # a non-prime
      if s[v0] < v0:
        continue
        
      primes.append(v0)
      for v1 in range(v0*v0, right+1, v0):
        if s[v1] > v0:
          s[v1] = v0
      
    if not primes:
      return [-1, -1]
    
    idx = bisect_left(primes, left)
    # print(primes[idx:])
    
    if idx >= len(primes)-1:
      return [-1, -1]
    
    curr = math.inf
    pair = [-1, -1]
    
    for i in range(idx, len(primes)-1):
      diff = primes[i+1]-primes[i]
      if diff < curr:
        curr = diff
        pair[0] = primes[i]
        pair[1] = primes[i+1]

    return pair
      