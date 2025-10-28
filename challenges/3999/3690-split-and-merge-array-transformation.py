'''
3690-split-and-merge-array-transformation
'''

from typing import List


class Solution:
  def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    step = 0
    curr, nxt = [tuple(nums1)], []
    seen = set(curr)
    tgt = tuple(nums2)
    # print('init:', seen)

    def bfs(sub: List, rem: List) -> List:
      res = []

      for i in range(len(rem)):
        arr = tuple(rem[:i] + sub + rem[i:])
        res.append(arr)

      return res

    while tgt not in seen:
      step += 1

      for cand in curr:
        for ln in range(1, n):
          for j in range(n):
            if n-j < ln:
              break

            sub = list(cand[j:j+ln])
            rem = list(cand[:j]) + list(cand[j+ln:])

            for res in bfs(sub, rem):
              t = tuple(res)
              if t in seen:
                continue

              seen.add(t)
              nxt.append(t)

      curr, nxt = nxt, curr
      nxt.clear()

    return step
      
        