'''
3838-weighted-word-mapping
'''

from typing import List


class Solution:
  def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
    baseline = ord('a')
    
    def map_to(s: str) -> str:
      idx = 25 - (sum(weights[ord(ch) - baseline] for ch in s) % 26)
      # print('idx:', s, idx)
      return chr(baseline + idx)

    return "".join([map_to(word) for word in words])
