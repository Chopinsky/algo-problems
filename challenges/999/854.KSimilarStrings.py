'''
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2

Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.
'''


from collections import defaultdict
from functools import lru_cache


class Solution:
  def kSimilarity(self, s1: str, s2: str) -> int:
    if s1 == s2:
      return 0
    
    dic = defaultdict(list)
    for i, ch in enumerate(s2):
      dic[ch].append(i)
      
    base_mask = 0
    mis_pos = []
    n = len(s1)
    target = (1 << n) - 1
    
    for i in range(n):
      if s1[i] == s2[i]:
        base_mask |= 1 << i
      else:
        mis_pos.append(i)

    init_pos = mis_pos[0]
    stack, nxt = [(s1[init_pos], init_pos, base_mask)], []
    seen = set(stack)
    moves = 0
    # print(dic, format(base_mask, f'#020b'), init_pos)
    
    @lru_cache(None)
    def get_init_pos(mask: int) -> int:
      for i in mis_pos:
        if (1<<i) & mask > 0:
          continue
          
        return i
      
      return -1
        
    while stack:
      # print(moves, stack)
      for ch, pos, mask in stack:
        # find the next index the current char shall go to
        for p1 in dic[ch]:
          # the destination char is already correct
          if (1<<p1) & mask > 0:
            continue
          
          nxt_mask = mask | (1<<p1)
          if s2[pos] == s1[p1]:
            nxt_mask |= 1 << pos
            pos = get_init_pos(nxt_mask)
            p1 = pos
          
          if nxt_mask == target or pos < 0:
            return moves+1
          
          nxt_state = (s1[p1], pos, nxt_mask)
          if nxt_state not in seen:
            nxt.append(nxt_state)
            seen.add(nxt_state)
      
      stack, nxt = nxt, stack
      nxt.clear()
      moves += 1
    
    return moves
    