'''
3522-calculate-score-after-performing-instructions
'''

from typing import List


class Solution:
  def calculateScore(self, instructions: List[str], values: List[int]) -> int:
    n = len(instructions)
    score = 0
    seen = set()
    idx = 0

    while 0 <= idx < n and idx not in seen:
      seen.add(idx)
      if instructions[idx] == "add":
        score += values[idx]
        idx += 1
      else:
        idx += values[idx]

    return score
        