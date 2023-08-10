from typing import List
from functools import lru_cache
from collections import defaultdict
from math import isqrt, gcd

class Solution:
  def gcd(self, a: int, b: int) -> int:
    if not a or a == b:
      return b

    if not b:
      return a

    if a < b:
      a, b = b, a

    while b > 0:
      b, a = a%b, b

    return a

  def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
    nums = set(nums)
    top = max(nums) + 1
    count = 0
    
    for i in range(1, top):
      # min subseq is the number itself
      if i in nums:
        count += 1
        continue
      
      # for all j that's dividable by i and in the `nums`, check
      # if the gcd of these numbers is also i -- meaning i is the
      # gcd of all these numbers
      base = 0

      for j in range(i, top, i):
        if j not in nums:
          continue
          
        base = gcd(base, j)
        if base == i:
          count += 1
          break
      
    return count
  
    
  def countDifferentSubsequenceGCDs0(self, nums: List[int]) -> int:
    @lru_cache(None)
    def divisors(n):
      for i in range(2, isqrt(n)+1):
        if n%i == 0:
          s = divisors(n//i)
          return s | set(q*i for q in s)

      return set([1, n])

    nums = set(nums)
    q = defaultdict(list)
    
    for num in nums:
      for div in divisors(num):
        q[div].append(num)

    ans = 0
    for num in q:
      list_div = q[num]
      s = list_div[0]
      for i in range(1, len(list_div)):
        s = gcd(s, list_div[i])
        if s == num:
          break

      if s == num: 
        ans += 1

    return ans
      