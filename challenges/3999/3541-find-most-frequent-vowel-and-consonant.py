'''
3541-find-most-frequent-vowel-and-consonant
'''

from collections import defaultdict


class Solution:
  def maxFreqSum(self, s: str) -> int:
    vc = defaultdict(int)
    cc = defaultdict(int)
    v = set(['a', 'e', 'i', 'o', 'u'])

    for ch in s:
      if ch in v:
        vc[ch] += 1
      else:
        cc[ch] += 1

    mv = max(vc.values()) if vc else 0
    mc = max(cc.values()) if cc else 0

    return mv+mc
