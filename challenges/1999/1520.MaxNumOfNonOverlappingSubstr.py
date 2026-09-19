'''
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
'''


from typing import List, Tuple
from functools import lru_cache, cache
from bisect import bisect_right, bisect_left
from collections import defaultdict


class Solution:
  def maxNumOfSubstrings(self, s: str) -> list[str]:
    pos = defaultdict(list)

    def get_rng(i: int):
      if i not in pos:
        return (-1, -1)

      l = pos[i][0]
      r = pos[i][-1]
      if l == r:
        return (l, r)

      done = False
      while not done:
        done = True
        for lst in pos.values():
          if lst[0] > r or lst[-1] < l:
            continue

          if l <= lst[0] and lst[-1] <= r:
            continue

          j = bisect_left(lst, l)
          k = bisect_right(lst, r)-1
          if k < j:
            continue
        
          done = False
          l = min(l, lst[0])
          r = max(r, lst[-1])

      return (l, r)

    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      pos[idx].append(i)
        
    cand = set()
    # print('init:', pos)

    for i in range(26):
      if i not in pos:
        continue

      rng = get_rng(i)
      cand.add(rng)
      # print('add:', i, rng, s[rng[0]:rng[1]+1])

    lst = []
    cand = sorted(cand, key=lambda x: x[1])
    # print('done:', cand)

    @cache
    def dp(idx: int):
      if idx >= cand[-1][-1]:
        return ()

      curr = ()
      cnt = 0

      for l, r in cand:
        if l <= idx:
          continue

        # taking this interval
        lst = dp(r)
        nxt_ln = 1+len(lst)
        nxt_cnt = (r-l+1) + sum(len(w) for w in lst)

        if nxt_ln > len(curr) or (nxt_ln == len(curr) and nxt_cnt < cnt):
          curr = ((l, r), ) + lst
          cnt = nxt_cnt
      
      return curr

    arr = dp(-1)

    return [s[i:j+1] for i, j in arr]

  def maxNumOfSubstrings(self, s: str) -> List[str]:
    ch_pos = [None for i in range(26)]
    
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      # ch_pos[idx].append(i)
      if not ch_pos[idx]:
        ch_pos[idx] = [i, i]
      else:
        ch_pos[idx][1] = i
        
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      l0, r0 = ch_pos[idx]
      
      for j in range(26):
        if not ch_pos[j] or idx == j:
          continue
          
        l1, r1 = ch_pos[j]
        if l1 < i < r1:
          ch_pos[j][0] = min(l0, l1)
          ch_pos[j][1] = max(r0, r1)

    substr = [(ch_pos[i][0], ch_pos[i][-1]) for i in range(26) if ch_pos[i]]
    substr.sort()
    n = len(substr)
    # print(substr_raw, substr, ch_pos)

    @lru_cache(None)    
    def dp(i: int) -> Tuple:
      if i >= n:
        return [], 0
      
      if i == n-1:
        l, r = substr[i]
        return [s[l:r+1]], r-l+1
      
      # if we don't use this substr, get the next best
      # results using substr[i+1:]
      lst, cnt = dp(i+1)
      # print(i, lst, cnt)
      
      # if we use this substr, get the next best results
      # using substr[j:]
      j = bisect_right(substr, (substr[i][1], float('inf')))
      lst1, cnt1 = dp(j)
      
      # add the current substr to lst1 and cnt1
      l, r = substr[i]
      lst1 = lst1 + [s[l:r+1]]
      cnt1 += r - l + 1
      # print(i, j, dp(j))
      
      if (len(lst1) > len(lst)) or (len(lst1) == len(lst) and cnt > cnt1):
        lst = lst1
        cnt = cnt1
      
      return lst, cnt
    
    lst, _ = dp(0)
    return lst
  