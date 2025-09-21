'''
966-vowel-spellchecker
'''

from typing import List


class Solution:
  def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
    cand = set(wordlist)
    cap = {}
    vow = {}
    v = set(['a', 'e', 'i', 'o', 'u'])
    res = []

    for w in wordlist:
      w0 = w.lower()
      if w0 not in cap:
        cap[w0] = w

      w1 = ''.join('*' if ch in v else ch for ch in w0)
      if w1 not in vow:
        vow[w1] = w

    # print('init:', cand, cap, vow)
    for q in queries:
      if q in cand:
        res.append(q)
        continue

      q1 = q.lower()
      if q1 in cap:
        res.append(cap[q1])
        continue

      q2 = ''.join('*' if ch in v else ch for ch in q1)
      if q2 in vow:
        res.append(vow[q2])
        continue

      res.append("")

    return res
