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
from functools import lru_cache
from bisect import bisect_right


class Solution:
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
        
    ''' 
    # alternative way to obtain expanded range:
    substr_raw = [(ch_pos[i][0], ch_pos[i][-1], i) for i in range(26) if ch_pos[i]]
    # substr_raw.sort(key=lambda x: (x[1]-x[0], x[0], x[1]))
    substr = {}
    
    for l0, r0, idx in substr_raw:
      curr = 0
      while curr < len(substr_raw):
        l1, r1, jdx = substr_raw[curr]
        curr += 1
        
        # same region, or no intersection
        if idx == jdx or r0 < l1 or r1 < l0:
          continue
        
        # expand the substr to contain all occurance
        # of string
        if l0 < l1 < r0 < r1:
          # partial intersection, expand right
          r0 = r1
          curr = 0
        elif l1 < l0 < r1 < r0:
          # partial intersection, expand left
          l0 = l1
          curr = 0
        elif l1 < l0 and r0 < r1:
          # check if there's an intersection
          k = bisect_right(ch_pos[jdx], l0)
          if k < len(ch_pos[jdx]) and ch_pos[jdx][k] < r0:
            l0, r0 = l1, r1
            curr = 0
          
      substr[idx] = (l0, r0)
    
    substr = sorted(substr.values())
    '''

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
  