'''
3799-word-squares-ii
'''

import itertools
from typing import List


class Solution:
  def wordSquares(self, words: List[str]) -> List[List[str]]:
    n = len(words)
    all_cand = list(itertools.permutations(list(range(n)), 4))
    # print('init:', all_cand)
    
    def is_valid(cand: list[int]) -> bool:
      t, l, r, b = cand
      return t[0] == l[0] and t[3] == r[0] and b[0] == l[3] and b[3] == r[3]

    ans = []
    for cand in all_cand:
      w = [words[cand[0]], words[cand[1]], words[cand[2]], words[cand[3]]]
      if is_valid(w):
        ans.append(w)

    return sorted(ans)
        