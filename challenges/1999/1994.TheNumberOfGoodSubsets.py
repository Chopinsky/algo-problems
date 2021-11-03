'''
You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:

Input: nums = [1,2,3,4]
Output: 6
Explanation: The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.

Example 2:

Input: nums = [4,2,3,15]
Output: 5
Explanation: The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 30
'''

from typing import List
from collections import Counter, defaultdict


class Solution:
  def numberOfGoodSubsets(self, nums: List[int]) -> int:
    c = Counter(nums)
    # print(c)
    
    # This can be reduced to an array since the `siv` yield the 
    # same array for all test cases.
    def siv(n: int) -> List[int]:
      s = [i for i in range(n+1)]
      for i in range(2, n+1):
        if i != s[i]:
          continue
          
        for j in range(i*i, n+1, i):
          if s[j] > i:
            s[j] = i
          
      return s
    
    s = siv(32)
    primes = defaultdict(int)
    base = sorted(c)
    nums = []
    
    # only 1 in the set, not going to work
    if base[-1] < 2:
      return 0
    
    # build the prime bases for each number
    for n in base:
      if s[n] == n:
        primes[n] |= 1 << n
        nums.append(n)
        continue
        
      done = True
      i = n
      
      while i > 1:
        if primes[n] & (1<<s[i]) > 0:
          done = False
          break
          
        primes[n] |= 1 << s[i]
        i //= s[i]
        
      if done:
        nums.append(n)
        
      else:
        primes.pop(n, None)
    
    total = 0
    size = len(nums)
    # print(nums)
    
    def dp(i: int, seen: int, count: int):
      nonlocal total
      
      # index outflow, done
      if i >= size:
        if seen > 2 and count:
          # print(format(seen, '#008b'), count)
          total = (total + count) % 1_000_000_007
          
        return
      
      # get the base number and if we skip this number
      val = nums[i]
      dp(i+1, seen, count)
      
      # a conflict prime exists, we're done
      if primes[val] & seen > 0:
        return
      
      if val == 1:
        nxt_count = (1 << c[val]) - 1
      else:
        nxt_count = (c[val] if not count else c[val]*count) % 1_000_000_007
      
      dp(i+1, seen | primes[val], nxt_count)
    
    # start the search
    dp(0, 0, 0)

    return total
  