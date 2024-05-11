'''
3145. Find Products of Elements of Big Array

A powerful array for an integer x is the shortest sorted array of powers of two that sum up to x. For example, the powerful array for 11 is [1, 2, 8].

The array big_nums is created by concatenating the powerful arrays for every positive integer i in ascending order: 1, 2, 3, and so forth. Thus, big_nums starts as [1, 2, 1, 2, 4, 1, 4, 2, 4, 1, 2, 4, 8, ...].

You are given a 2D integer matrix queries, where for queries[i] = [fromi, toi, modi] you should calculate (big_nums[fromi] * big_nums[fromi + 1] * ... * big_nums[toi]) % modi.

Return an integer array answer such that answer[i] is the answer to the ith query.

Example 1:

Input: queries = [[1,3,7]]

Output: [4]

Explanation:

There is one query.

big_nums[1..3] = [2,1,2]. The product of them is 4. The remainder of 4 under 7 is 4.

Example 2:

Input: queries = [[2,5,3],[7,7,4]]

Output: [2,2]

Explanation:

There are two queries.

First query: big_nums[2..5] = [1,2,4,1]. The product of them is 8. The remainder of 8 under 3 is 2.

Second query: big_nums[7] = 2. The remainder of 2 under 4 is 2.

Constraints:

1 <= queries.length <= 500
queries[i].length == 3
0 <= queries[i][0] <= queries[i][1] <= 10^15
1 <= queries[i][2] <= 10^5
'''

from typing import List, Dict
from functools import lru_cache
from collections import defaultdict

class Solution:
  def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
    ans = []
    
    @lru_cache(None)
    def count_ones(shift: int):
      if shift <= 0:
        return 1 if shift == 0 else 0
      
      return (1<<shift) + 2*count_ones(shift-1)
    
    @lru_cache(None)
    def count(val: int):
      if val <= 1:
        return max(0, val)
      
      shift = len(bin(val)[2:])-1
      total, ones = 0, 0
      
      while shift >= 0:
        if val & (1<<shift) > 0:
          total += ones*(1<<shift) + count_ones(shift-1)
          ones += 1
          
        shift -= 1
        
      total += ones
      # print('count:', val, total, ones)
      
      return total
          
    @lru_cache(None)
    def find(idx: int):
      if idx <= 1:
        return [1, 1] if idx == 0 else [2, 2]
      
      l, r = 1, 10**14
      last = [r, count(r)]
      target = idx + 1
      
      while l <= r:
        mid = (l+r)//2
        c0 = count(mid)
        
        if c0 >= target:
          last[0] = mid
          last[1] = c0
        
        if c0 == target:
          break
          
        if c0 > target:
          r = mid-1
        else:
          l = mid+1
      
      return tuple(last)
      
    def make(shift: int):
      if shift == 0:
        return {}
      
      c0 = 1<<(shift-1)
      return {i:c0 for i in range(shift)}
    
    def calc(val: int):
      if val <= 2:
        return {1:1, 0:1} if val == 2 else {0:1}
        
      counter = defaultdict(int)
      base = []
      shift = len(bin(val)[2:])-1
      
      while shift >= 0:
        if val & (1<<shift) > 0:
          # update the upper parts
          c0 = 1<<shift
          for s0 in base:
            counter[s0] += c0
          
          # add the lower parts
          for s0, c0 in make(shift).items():
            counter[s0] += c0
          
          base.append(shift)
        
        shift -= 1
      
      for s0 in base:
        counter[s0] += 1
        
      return counter
      
    def pop(d: Dict, val: int, c: int):
      if not c:
        return d
      
      shift = len(bin(val)[2:])-1
      while shift >= 0 and c > 0:
        if val & (1<<shift) > 0:
          c -= 1
          d[shift] -= 1
          if not d[shift]:
            d.pop(shift, None)
        
        shift -= 1
      
      return d
    
    def get_val(d0: Dict, d1: Dict, mod: int):
      cand = [val for val in d1.keys()]
      for pos in cand:
        d1[pos] -= d0.get(pos, 0)
        if not d1[pos]:
          d1.pop(pos, None)
          
      # print('minus:', d1)
      res = 1
      for pos, cnt in d1.items():
        if pos == 0:
          continue
          
        res = (res * pow(1<<pos, cnt, mod)) % mod
        
      return res
    
    for f, t, mod in queries:
      if mod == 1:
        ans.append(0)
        continue
        
      v0, c0 = find(f)
      d0 = pop(calc(v0), v0, c0-f)
      # print('f:', f, (v0, c0), d0)
      
      v1, c1 = find(t)
      d1 = pop(calc(v1), v1, c1-t-1)
      # print('t:', t, (v1, c1), d1)
      
      ans.append(get_val(d0, d1, mod))
      
    return ans
        