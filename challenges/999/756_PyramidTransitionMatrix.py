'''
You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

Example 1:

Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "E" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
Example 2:

Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.

Constraints:

2 <= bottom.length <= 6
0 <= allowed.length <= 216
allowed[i].length == 3
The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
All the values of allowed are unique.
'''

from typing import List, Set
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        cand = defaultdict(list)
        for a in allowed:
            cand[a[:2]].append(a[2])
        # print('init:', cand)

        def gen(a: List, i: int) -> List[str]:
            if i >= len(a):
                return ['']

            res = set()
            for c in a[i]:
                for s in gen(a, i+1):
                    res.add(c+s)

            return list(res)

        @cache
        def dp(b: str) -> bool:
            if len(b) <= 1:
                return True

            if len(b) == 2:
                return b in cand

            a = []
            for i in range(len(b)-1):
                s = b[i:i+2]
                if s not in cand:
                    return False

                a.append(cand[s])

            for s in gen(a, 0):
                if dp(s):
                    return True

            return False

        return dp(bottom)

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        a = defaultdict(set)
        for s in allowed:
            a[s[:2]].add(s[2])
      
    print(a)
    stack = [bottom]
    cand = set()
    ln = len(bottom)
    
    def generate(base: str) -> Set:
      c0, c1 = set(['']), set()
      for i in range(len(base)-1):
        if base[i:i+2] not in a:
          return set()
        
        for ch in a[base[i:i+2]]:
          c1 |= {val+ch for val in c0}
        
        c0, c1 = c1, c0
        c1.clear()
        
      return c0
    
    while ln > 1 and stack:
      cand.clear()
      for base in stack:
        cand |= generate(base)
        
      stack = list(cand)
      ln -= 1
    
    # print(stack, ln)
    return ln == 1 and len(stack) > 0
  