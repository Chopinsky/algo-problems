'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''


from typing import List
from functools import lru_cache
from bisect import bisect_left


class Solution:
  def partition(self, s: str) -> List[List[str]]:
    ch_pos = [[] for _ in range(26)]
    n = len(s)
    
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      ch_pos[idx].append(i)
      
    def is_pal(i: int, j: int) -> bool:
      if j < i or i < 0 or j >= n:
        return False
      
      if i == j:
        return True
      
      while i < j:
        if s[i] != s[j]:
          return False
        
        i += 1
        j -= 1
        
      return True
    
    @lru_cache(None)
    def build_partition(i: int) -> List[List[str]]:
      if i >= n:
        return []
      
      if i == n-1:
        return [[s[i]]]
      
      idx = ord(s[i]) - ord('a')
      start = bisect_left(ch_pos[idx], i)
      ans = []
      
      for j in ch_pos[idx][start:]:
        if not is_pal(i, j):
          continue
          
        for sub_str in build_partition(j+1):
          ans.append([s[i:j+1]] + sub_str)
          
        if j == n-1:
          ans.append([s[i:j+1]])
        
      return ans
      
    return build_partition(0)
  