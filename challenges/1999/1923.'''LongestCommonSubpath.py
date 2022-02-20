'''
There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.

There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.

Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.

A subpath of a path is a contiguous sequence of cities within that path.

Example 1:

Input: n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]
Output: 2
Explanation: The longest common subpath is [2,3].
Example 2:

Input: n = 3, paths = [[0],[1],[2]]
Output: 0
Explanation: There is no common subpath shared by the three paths.
Example 3:

Input: n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]
Output: 1
Explanation: The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.

Constraints:

1 <= n <= 10^5
m == paths.length
2 <= m <= 10^5
sum(paths[i].length) <= 10^5
0 <= paths[i][j] < n
The same city is not listed multiple times consecutively in paths[i].
'''


from typing import List, Set


class Solution:
  '''
  the key is to use a good rolling hash function, and here it is rabin_karp
  '''
  def longestCommonSubpath0(self, n: int, paths: List[List[int]]) -> int:
    mod = (1 << 64) - 159
    d = 1 << 17
      
    def rabin_karp(arr: List, m: int) -> Set:
      base = 0
      top = (1 << (17*(m-1))) % mod

      for i in range(m): 
        base = (d * base + arr[i])% mod

      all_hashes = set()
      all_hashes.add(base)

      for i in range(len(arr) - m):
        base = (d * (base - arr[i]*top) + arr[i+m])% mod
        all_hashes.add(base)

      return all_hashes

    m = len(paths)
    l, r = 0, min(len(p) for p in paths) + 1

    while l + 1 < r:
      mid = (l + r)//2
      tt = set.intersection(*[rabin_karp(p, mid) for p in paths])

      if len(tt) != 0:
        l = mid
      else:
        r = mid

    return l
      
      
  def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
    paths.sort(key=lambda x: len(x))
    
    def get_shared_cities():
      cities = set(paths[0])
      for i in range(1, len(paths)):
        cities &= set(paths[i])
        if not cities:
          return cities
      
      return cities
    
    cities = get_shared_cities()
    if len(cities) <= 1:
      return len(cities)
    
    mod = (1 << 64) - 159
    d = 1 << 17
    
    '''
    p = max(cities)+1
    # print(cities, p)
    
    def gen_hash(i: int, m: int, last: Set) -> Set:
      vals = set()
      if m > len(paths[i]):
        return vals
      
      if m == 1:
        return set(paths[i])
      
      base = -1
      c = paths[i]
      idx = 0
      
      while idx+m <= len(c):
        if base < 0:
          base = 0
          for j in range(idx, idx+m):
            if c[j] not in cities:
              idx = j+1
              base = -1
              break
              
            base = (base*p + c[j]) % mod
          
          if base >= 0:
            if not last or (base, c[idx]) in last:
              vals.add((base, c[idx]))
              
            idx += 1
          
        else:
          add_idx = idx + m - 1
          if c[add_idx] not in cities:
            idx = add_idx + 1
            base = -1
            continue
            
          base = (mod + (base - c[idx-1]*pow(p, m-1, mod))) % mod
          base = (base * p + c[add_idx]) % mod
          if not last or (base, c[idx]) in last:
            vals.add((base, c[idx]))
            
          idx += 1
          
      return vals
    '''

    def rabin_karp(i: int, m: int, last: Set) -> Set:
      base = 0
      arr = paths[i]
      top = (1 << (17*(m-1))) % mod

      for i in range(m): 
        base = (d * base + arr[i])% mod

      all_hashes = set()
      if not last or (base, arr[0]) in last:
        all_hashes.add((base, arr[0]))

      for i in range(len(arr) - m):
        base = (d * (base - arr[i]*top) + arr[i+m])% mod
        if not last or (base, arr[i+1]) in last:
          all_hashes.add((base, arr[i+1]))

      return all_hashes
    
    def check(m: int) -> bool:
      hash_set = set()
      
      for i in range(len(paths)):
        # hash_set = gen_hash(i, m, None if i == 0 else hash_set) 
        hash_set = rabin_karp(i, m, hash_set)
        if not hash_set:
          break
        
      return len(hash_set) > 0
      
    l, r = 1, len(paths[0])
    last = 1
    
    while l < r:
      m = (l + r) // 2
      # print('bi:', l, m, r, check(m))
      
      if check(m):
        l = m+1
        last = m
      else:
        r = m-1
    
    return l if check(l) else last
    