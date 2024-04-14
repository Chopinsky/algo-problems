'''
Test cases:

[383,491,329]
[363,329]
[1,4,3,3,2]
[0,3,3,2]
[2,3,5,7,7,7,5]
[0,7,5]
[1,2,3,4]
[2]
[2]
[2]
[3,1]
[3,1]
[4,8,2,9]
[0,0]
'''

from functools import lru_cache, reduce
from typing import List
from heapq import heappush, heappop
import math

class Solution:
  def minimumValueSum(self, nums: List[int], vals: List[int]) -> int:
    m, n = len(vals), len(nums)
    if nums[0]&vals[0] != vals[0]:
      return -1
    
    if m == 1:
      res = reduce(lambda x, y: x&y, nums, nums[0])
      return -1 if res != vals[0] else nums[-1]
    
    debug = False
    
    def get_last():
      curr = [math.inf] * n
      mask, target = nums[-1], vals[-1]
      idx = n-1

      while idx >= m-1:
        mask &= nums[idx]
        if mask&target != target:
          break
            
        if mask == target:
          curr[idx] = nums[-1]
          
        idx -= 1
          
      return curr
    
    @lru_cache(None)
    def ser(val: int):
      res = tuple()
      mask = 1
      idx = 0
      
      while mask <= val:
        if mask & val > 0:
          res += (idx, )
          
        mask <<= 1
        idx += 1
        
      return res
    
    curr = get_last()
    prefix = []
    digits = [0]*18
    base = [0]*18
    
    for val in nums:
      for d in ser(val):
        digits[d] += 1
        
      prefix.append(digits.copy())
    
    if debug:
      print(curr) 
      # print(prefix)
    
    def calc(i: int, j: int):
      p0 = prefix[i-1] if i > 0 else base
      p1 = prefix[j]
      ln = j-i+1
      val, mask = 0, 1
      
      for c0, c1 in zip(p0, p1):
        if c1-c0 == ln:
          val |= mask
          
        mask <<= 1
        
      return val
    
    def search(i: int, tgt: int):
      if nums[i]&tgt != tgt:
        return -1, -1
      
      l, r = i, n-1
      last = nums[i]
      
      while l <= r:
        mid = (l + r) // 2
        val = calc(i, mid)
        
        if val&tgt == tgt:
          if val == tgt:
            last = val
            r = mid-1
          else:
            last = min(last, val)
            l = mid+1
        else:
          r = mid-1
        
      return l, last
    
    for j in range(m-2, -1, -1):
      tgt = vals[j]
      nxt = [math.inf] * n
      end = -1
      stack = []
      
      for i in range(j, n):
        # not enough numbers left to form m-j+1 subarrays
        if n-i < m-j:
          break

        # for the first row, only cares about the score for curr[0]
        if j == 0 and i > 0:
          break
          
        start, val = search(i, tgt)
        if start < i or val != tgt:
          continue
          
        # print('check:', (j, i), start, val)
        
        if end < start:
          stack.clear()
          end = start
          
          while end < n-1 and tgt&nums[end] == tgt:
            if curr[end+1] < math.inf:
              heappush(stack, (nums[end]+curr[end+1], end))
            
            end += 1
            
        else:
          while stack and stack[0][1] < start:
            heappop(stack)
            
        if stack:
          nxt[i] = stack[0][0]
      
      curr = nxt
      if all([val == math.inf for val in curr]):
        return -1

      if debug:
        print('done:', j, curr)
    
    return -1 if curr[0] == math.inf else curr[0]
        