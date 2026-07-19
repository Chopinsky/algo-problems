'''
3999-minimum-number-of-string-groups-through-transformations
'''

from typing import List


class Solution:
  def minimumGroups(self, words: List[str]) -> int:
    def canonical(s: str) -> str:
      # booth algo
      base = s+s
      n = len(s)

      # i - curr rotation start;
      # j - next rotation start; 
      # k - matched prefix;
      i, j, k = 0, 1, 0

      while i < n and j < n and k < n:
        c0 = base[i+k]
        c1 = base[j+k]

        # matching, continue
        if c0 == c1:
          k += 1
          continue

        # better solution found
        if c0 > c1:
          i = i + k + 1
          k = 0
          if i <= j:
            i = j + 1

          continue

        # shift next start to begin new search
        j = j + k + 1
        k = 0
        if j <= i:
          j = i + 1

      start = min(i, j)
      return base[start:start+n]

    groups = set()
    for w in words:
      n = len(w)
      
      # get the hash of even subseq
      e_seq = "".join(w[i] for i in range(n) if i%2 == 0)
      e_hash = canonical(e_seq)

      # get the hash of the odd subseq
      o_seq = "".join(w[i] for i in range(n) if i%2 == 1)
      o_hash = canonical(o_seq)

      # add unique pairs
      groups.add((e_hash, o_hash))
      # print('iter:', w, (e_hash, e_seq), (o_hash, o_seq))

    return len(groups)
