'''
2976. Minimum Cost to Convert String I

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

Constraints:

1 <= source.length == target.length <= 10^5
source, target consist of lowercase English letters.
1 <= cost.length == original.length == changed.length <= 2000
original[i], changed[i] are lowercase English letters.
1 <= cost[i] <= 10^6
original[i] != changed[i]
'''

from typing import List

from heapq import heappop, heappush
from functools import lru_cache
from collections import defaultdict

class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    if len(source) != len(target):
      return -1
    
    m = {}
    for s, t, c in zip(original, changed, cost):
      if s == t:
        continue
      
      m[s, t] = min(m.get((s, t), float('inf')), c)
      
    e = defaultdict(list)
    for k, c in m.items():
      e[k[0]].append((k[1], c))
    
    @lru_cache(None)
    def search(ch0: str, ch1: str):
      heap = [(0, ch0)]
      seen = {ch0:0}
      small = float('inf')
      
      while heap:
        c0, ch = heappop(heap)
        # if ch0 == 'd':
        #   print('iter:', ch, c0)
        
        if c0 > seen[ch]:
          continue
        
        for ch2, c1 in e[ch]:
          c2 = c0+c1
          if ch2 == ch1:
            small = min(small, c2)
            continue
            
          if ch2 in seen and c2 >= seen[ch2]:
            continue
            
          seen[ch2] = c2
          heappush(heap, (c2, ch2))
        
      return -1 if small == float('inf') else small
      
    # print(e)
    total = 0
    
    for ch0, ch1 in zip(source, target):
      if ch0 == ch1:
        continue
        
      c0 = search(ch0, ch1)
      if c0 < 0:
        return -1
      
      # print(ch0, ch1, c0)
      total += c0
    
    return total
        
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    inf = float('inf')
    mat = [[inf if i != j else 0 for j in range(26)] for i in range(26)]
    
    for i in range(len(original)):
      odx = ord(original[i]) - ord('a')
      cdx = ord(changed[i]) - ord('a')
      mat[odx][cdx] = min(mat[odx][cdx], cost[i])
      
    for k in range(26):
      for i in range(26):
        if i == k or mat[i][k] == inf:
          continue
          
        for j in range(26):
          if i == j or k == j or mat[k][j] == inf:
            continue
            
          mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])
          
    # print(mat)
    n = len(source)
    dp = 0
    
    for i in range(n):
      odx = ord(source[i]) - ord('a')
      cdx = ord(target[i]) - ord('a')
      if mat[odx][cdx] == inf:
        return -1
      
      dp += mat[odx][cdx]
    
    return dp
        