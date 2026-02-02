'''
3598-longest-common-prefix-between-adjacent-strings-after-removals
'''

from typing import List


class Solution:
  def longestCommonPrefix(self, words: List[str]) -> List[int]:
    trie = {}

    def add(w: str, i: int):
      curr = trie
      for ch in w:
        if ch not in curr:
          curr[ch] = {"$":[]}

        curr = curr[ch]
        curr["$"].append(i)
        curr["$"] = curr["$"][-2:]

    def query(w: str, i: int):
      pl = 0
      p = True
      ppl = 0
      pp = True
      curr = trie

      for ch in w:
        if not p and not pp:
          break

        if ch not in curr:
          break

        curr = curr[ch]

        if p:
          if i-1 in curr["$"]:
            pl += 1
          else:
            p = False

        if pp:
          if i-2 in curr["$"]:
            ppl += 1
          else:
            pp = False
        
      return pl, ppl

    n = len(words)
    ans = [0]*n
    ln = []
    cross = [0]*n

    for i in range(n):
      if i > 0:
        pl, ppl = query(words[i], i)
        ln.append((pl, i-1))
        cross[i-1] = ppl
        # print('iter:', words[i], pl, ppl)

      add(words[i], i)
      # print('added:', trie)

    ln.sort()
    ln = ln[-3:]  # only the last 3 pairs matter
    # print('done:', ln, cross)

    for i in range(n):
      j = len(ln)-1
      while j >= 0:
        # found 
        if i-1 != ln[j][1] and i != ln[j][1]:
          ans[i] = max(ans[i], ln[j][0])
          break

        j -= 1

      # compare with cross-pair
      ans[i] = max(ans[i], cross[i])

    return ans
        