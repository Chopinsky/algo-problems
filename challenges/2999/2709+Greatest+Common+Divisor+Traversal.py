'''
2709. Greatest Common Divisor Traversal

You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

from typing import List
from functools import lru_cache

class Solution:
  def canTraverseAllPairs(self, nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
      return True
    
    primes = {}
    groups = set()
    
    def get_sive(top: int):
      s = [i for i in range(top+1)]
      for v0 in range(2, top+1):
        if s[v0] != v0:
          continue
          
        for v1 in range(2*v0, top+1, v0):
          s[v1] = min(s[v1], v0)
          
      return s
    
    s = get_sive(max(nums))
    # print(s)
    
    def find(x: int) -> int:
      if x not in primes:
        primes[x] = x
      else:
        while x != primes[x]:
          x = primes[x]
          
      return x
      
    def union(x: int, y: int):
      rx, ry = find(x), find(y)
      if rx <= ry:
        primes[ry] = rx
      else:
        primes[rx] = ry
        
    def union_groups(t):
      groups.clear()
      arr = sorted(t)
      p0 = find(arr[0])
      
      for p1 in arr[1:]:
        union(p0, find(p1))
    
    @lru_cache(None)
    def get_factors(val: int):
      if val == 1:
        return (1, )

      res = set()
      while val > 1:
        f = s[val]
        res.add(f)
        val //= f
      
      return tuple(res)
    
    for val in nums:
      if val == 1:
        return False
      
      factors = get_factors(val)
      union_groups(factors)
      # print(val, factors)

    base = []
    for p in primes:
      g = find(p)
      if not base:
        base.append(g)
      elif g != base[0]:
        return False
    
    return True
        

  def canTraverseAllPairs(self, nums: List[int]) -> bool:
    if len(nums) == 1:
      return True
    
    if 1 in nums:
      return False
    
    def sive(n: int):
      s = [i for i in range(n+1)]
      for i in range(2, n+1):
        for j in range(i*i, n+1, i):
          if s[j] <= i:
            continue
            
          s[j] = i
        
      return s
    
    top = max(nums)
    s = sive(top)
    group = {}
    
    def find(x: int) -> int:
      if x not in group:
        group[x] = x
        return x
      
      while group[x] != x:
        x = group[x]
        
      return x
    
    def union(x: int, y: int):
      rx, ry = find(x), find(y)
      if rx <= ry:
        group[ry] = rx
      else:
        group[rx] = ry
        
    def primes(val: int):
      p = set()
      
      # val is a prime
      if s[val] == val:
        p.add(val)
        return [val]
      
      # add all prime coefficients
      while val > 1:
        p0 = s[val]
        p.add(p0)
        val //= p0
        
      return list(p)
    
    for num in nums:
      p = primes(num)
      if not p:
        return False
      
      # print(num, p)
      root = find(p[0])
      
      for p0 in p[1:]:
        union(root, p0)
        
    keys = list(group)
    root = find(keys[0])
    
    for p0 in keys[1:]:
      if find(p0) != root:
        return False
    
    return True
        