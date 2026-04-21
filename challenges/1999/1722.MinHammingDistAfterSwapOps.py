'''
You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

Example 1:

Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

Example 2:

Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.

Example 3:

Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0

Constraints:

n == source.length == target.length
1 <= n <= 105
1 <= source[i], target[i] <= 10 ** 5
0 <= allowedSwaps.length <= 10 ** 5
allowedSwaps[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
'''


from typing import List
from collections import defaultdict


class Solution:
  def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    n = len(source)
    g = [i for i in range(n)]
    cnt = [1]*n

    def find(x: int) -> int:
      while g[x] != x:
        x = g[x]

      return x

    def union(x: int, y: int):
      rx = find(x)
      ry = find(y)

      if rx == ry:
        return

      if cnt[rx] < cnt[ry]:
        rx, ry = ry, rx

      g[ry] = rx
      cnt[rx] += cnt[ry]
    
    for u, v in allowedSwaps:
      union(u, v)

    group = defaultdict(list)
    for u in range(n):
      root = find(u)
      group[root].append(u)

    dist = 0
    c = defaultdict(int)

    for lst in group.values():
      c.clear()

      for idx in lst:
        c[source[idx]] += 1

      for idx in lst:
        if c[target[idx]] > 0:
          c[target[idx]] -= 1
        else:
          dist += 1

    return dist  
        
  def minimumHammingDistance0(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    ln = len(source)
    arr = [i for i in range(ln)]
    
    def find(i: int) -> int:
      while arr[i] != i:
        i = arr[i]
        
      return i
    
    def union(i: int, j: int) -> int:
      ii, ij = find(i), find(j)
      if ii == ij:
        return ii
      
      if ii < ij:
        arr[ij] = ii
        return ii
        
      arr[ii] = ij
      return ij
    
    for i, j in allowedSwaps:
      union(i, j)
      
    groups = defaultdict(list)
    for i, n in enumerate(source):
      ri = find(i)
      groups[ri].append(i)
      
    dist = 0
    for _, idx in groups.items():
      count = defaultdict(int)
      for i in idx:
        count[source[i]] += 1
        count[target[i]] -= 1
      
      # print(idx, count)
      total = 0
      
      for d in count.values():
        total += abs(d)
        
      dist += total // 2
    
    return dist
    
