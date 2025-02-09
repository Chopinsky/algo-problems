'''
1408. String Matching in an Array
'''

from typing import List


class Solution:
  def stringMatching(self, words: List[str]) -> List[str]:
    words.sort(key=lambda x: len(x))
    ans = []
    n = len(words)

    for i in range(n):
      w0 = words[i]
      l0 = len(w0)
      for j in range(i+1, n):
        w1 = words[j]
        if len(w1) == l0 or w0 not in w1:
          continue

        ans.append(w0)
        break

    return ans
        