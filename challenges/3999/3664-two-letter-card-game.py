'''
3664-two-letter-card-game
'''

from typing import List, Tuple
from collections import Counter, defaultdict, deque
from bisect import insort


class Solution:
  def score(self, cards: List[str], x: str) -> int:
    cnt = Counter(cards)
    cnt_xx = cnt.pop(x+x, 0)
    cnt1 = [c for w, c in cnt.items() if w[0] == x]
    cnt2 = [c for w, c in cnt.items() if w[1] == x]
    
    def calc(cnt: list[int]) -> Tuple[int, int]:
      sum_cnt = sum(cnt)
      max_cnt = max(cnt, default=0)
      pairs = min(sum_cnt//2, sum_cnt-max_cnt)

      # return pairs, left-over-singles
      return pairs, sum_cnt - pairs*2

    pair1, left1 = calc(cnt1)
    pair2, left2 = calc(cnt2)
    res = pair1 + pair2

    # doubles pairing with the single leftovers
    if cnt_xx > 0:
      mn = min(cnt_xx, left1+left2)
      res += mn
      cnt_xx -= mn

    # more doubles, split the original pairs, for each split we 
    # can form 2 new pairs using doubles
    if cnt_xx > 0:
      res += min(cnt_xx//2, pair1+pair2)

    return res

  def score(self, cards: List[str], x: str) -> int:
    fc = defaultdict(int)
    sc = defaultdict(int)
    dc = 0

    for card in cards:
      if x not in card:
        continue

      if card[0] == card[1]:
        dc += 1
        continue

      if card[0] == x:
        fc[card[1]] += 1
      else:
        sc[card[0]] += 1

    f = sorted(fc.values())
    s = sorted(sc.values())
    score = 0
    print('pre:', dc, f, s)

    def count(src: list[int], val: int) -> int:
      c = 0
      if not src:
        return c

      arr = deque(src)
      if val > 0:
        insort(arr, val)

      # print('iter:', arr)
      while len(arr) > 1:
        if len(arr) == 3:
          top = max(arr)
          ss = sum(arr)
          if ss > 2*top:
            c += ss // 2
            break

        vl = arr.popleft()
        vr = arr.pop()
        diff = min(vl, vr)
        c += diff
        vl -= diff
        vr -= diff

        if vl+vr > 0:
          arr.appendleft(max(vl, vr))

      # print('iter-end:', c)
      return c
      
    score = 0
    for val in range(dc+1):
      s0 = count(f, val)
      s1 = count(s, dc-val)
      score = max(score, s0+s1)
      # print('done:', val, score, s0, s1)

    return score
