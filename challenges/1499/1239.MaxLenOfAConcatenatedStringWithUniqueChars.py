'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''

from typing import List
from functools import lru_cache

class Solution:
  def maxLength(self, arr: List[str]) -> int:
    n = len(arr)
    
    @lru_cache(None)
    def get_mask(i: int) -> int:
      mask = 0
      
      for ch in arr[i]:
        m0 = 1 << (ord(ch) - ord('a'))
        if m0 & mask > 0:
          return -1
        
        mask |= m0
      
      return mask
    
    @lru_cache(None)
    def dp(i: int, mask: int) -> int:
      if i >= n:
        return 0
      
      m0 = get_mask(i)
      s0 = dp(i+1, mask)
      if m0 < 0 or m0&mask > 0:
        return s0
      
      s1 = len(arr[i]) + dp(i+1, mask | m0)
      
      return max(s0, s1)
    
    return dp(0, 0)
    

  def maxLength(self, arr: List[str]) -> int:
    arr = [s for s in arr if len(set(s)) == len(s)]
    if not arr:
      return 0
    
    arr.sort(reverse=True)
    masks = []
    
    for s in arr:
      mask = 0
      for ch in s:
        mask |= 1 << (ord(ch) - ord('a'))
        
      masks.append(mask)
      
    n = len(arr)
    pairs = [0] * len(arr)
    
    for i in range(n-1):
      for j in range(i+1, n):
        if masks[i] & masks[j] > 0:
          pairs[i] |= 1 << j
          pairs[j] |= 1 << i
    
    # print(arr, masks)
    # print(pairs)
    
    def dp(i: int, mask: int) -> int:
      if i >= n:
        ln = 0
        idx = 0
        
        while mask > 0:
          if mask & 1:
            ln += len(arr[idx])
          
          mask >>= 1
          idx += 1
          
        return ln
      
      if pairs[i] & mask > 0:
        return dp(i+1, mask)
      
      return max(dp(i+1, mask | (1 << i)), dp(i+1, mask))
    
    return dp(0, 0)
    

  def maxLength(self, arr: List[str]) -> int:
    n = len(arr)
    data = [[0, 0] for _ in range(n)]
    
    def build(i: int):
      oa = ord('a')
      for ch in arr[i]:
        idx = 1 << (ord(ch) - oa)
        if not idx & data[i][0]:
          data[i][0] |= idx
          data[i][1] += 1
        else:
          data[i][0] = 0
          data[i][1] = 0
          break
    
    for i in range(n):
      build(i)
    
    cache = {}
    # print(data)
    
    def check(base: int, i: int) -> int:
      nonlocal n
      
      if i >= n:
        return 0
      
      if (base, i) in cache:
        return cache[base, i]
      
      best = 0
      if not base & data[i][0]:
        best = data[i][1] + check(base|data[i][0], i+1)
      
      best = max(best, check(base, i+1))
      cache[base, i] = best
      
      return best
    
    return check(0, 0)
    
