'''
3414. Maximum Score of Non-overlapping Intervals

[[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
[[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
[[19,20,9],[6,10,5],[25,25,23],[12,15,11],[3,23,32],[13,13,24]]
'''

from typing import List, Dict
from bisect import bisect_left

class Solution:
  def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
    cand = sorted([(r, l, w, i) for i, [l, r, w] in enumerate(intervals)])
    ans = [-1, [len(intervals)]]
    l1, l2, l3, l4 = {}, {}, {}, {}
    # print('init:', cand)

    def can_replace(s0: List, s1: List):
      if s1[0] < s0[0]:
        return False

      if s1[0] > s0[0]:
        return True

      a, b = s0[1], s1[1]
      i = 0
      la, lb = len(a), len(b)

      while i < la and i < lb:
        va, vb = a[i], b[i]
        if va < vb:
          return False

        if vb < va:
          return True

        i += 1

      return lb < la

    def build(src: List, i: int, w: int):
      if src is None:
        return None

      w0 = src[0] + w
      a0 = sorted(src[1] + [i])
      return [w0, a0]

    def update(src: List, store: Dict, pos: int):
      if src is None or pos < 0:
        return

      if 'idx' not in store:
        store['idx'] = []

      if pos not in store or can_replace(store[pos], src):
        if '$' not in store or can_replace(store['$'], src):
          store['$'] = src

        store[pos] = store['$']
        if not store['idx'] or pos > store['idx'][-1]:
          store['idx'].append(pos)

      if can_replace(ans, store[pos]):
        ans[0] = store[pos][0]
        ans[1] = store[pos][1]

    def process(store: Dict, nxt_store: Dict, data: List):
      r, l, w, i = data
      arr = store.get('idx', [])
      j = bisect_left(arr, l) - 1
      pos = -1 if j < 0 else arr[j] 
      src = build(store.get(pos, None), i, w)
      update(src, nxt_store, r)

    for data in cand:
      # print('iter:', (data[1], data[0]), data[3], data[2])
      process(l3, l4, data)
      process(l2, l3, data)
      process(l1, l2, data)

      # update p1
      r, _, w, i = data
      update([w, [i]], l1, r)
      # print('updated:', l1, l2, l3, l4)

    # print('done:', ans, l1, l2, l3, l4)

    return ans[1]
        