'''
An array is squareful if the sum of every pair of adjacent elements is a perfect square.

Given an integer array nums, return the number of permutations of nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: nums = [2,2,2]
Output: 1

Constraints:

1 <= nums.length <= 12
0 <= nums[i] <= 10 ** 9
'''


from typing import List
from math import isqrt
from collections import defaultdict, Counter


class Solution:
  def numSquarefulPerms(self, nums: List[int]) -> int:
    c = Counter(nums)
    cand = defaultdict(set)
    
    for i in c.keys():
      for j in c.keys():
        if i == j and c[i] <= 1:
          continue
          
        if isqrt(i+j) ** 2 == i+j:
          cand[i].add(j)
          cand[j].add(i)
          
    # print(cand)
    
    def dfs(val: int, l: int = len(nums)-1) -> int:
      c[val] -= 1
      count = 0
      
      if l == 0:
        count = 1
      else:
        for num in cand[val]:
          if c[num] <= 0:
            continue
            
          count += dfs(num, l-1)
      
      c[val] += 1
      
      return count
    
    return sum(map(dfs, c))


  def numSquarefulPerms0(self, nums: List[int]) -> int:
    def is_perfect(a: int) -> bool:
      return isqrt(a) ** 2 == a
    
    dic = defaultdict(int)
    pairs = defaultdict(set)
    n = set()
    
    for num in nums:
      dic[num] += 1
      n.add(num)
      
    n = list(n)
    cache = {}
    
    for i0 in range(len(n)):
      for i1 in range(i0, len(n)):
        if i0 == i1 and dic[n[i0]] <= 1:
          continue
          
        if is_perfect(n[i0]+n[i1]):
          pairs[n[i0]].add(n[i1])
          pairs[n[i1]].add(n[i0])
    
    # print(dic, n)
    # print(pairs)
    
    def to_key(l: int):
      base = f'{l};'
      
      for num in n:
        if not dic[num]:
          continue
          
        base += f'{num}-{dic[num]};'
        
      return base
    
    def count(l: int, lst: List[int], ln: int) -> int:
      if not lst:
        return 0
      
      key = to_key(l)
      if key in cache:
        return cache[key]
      
      base = 0
      for num in lst:
        if not dic[num]:
          continue
        
        if ln == len(nums)-1:
          # print(key, num)
          base += 1
        else:
          dic[num] -= 1
          base += count(num, list(pairs[num]), ln+1)   
          dic[num] += 1
          
      cache[key] = base
      return base
    
    return count(-1, n, 0)
  