'''
3457-eat-pizzas
'''

from collections import Counter


class Solution:
  def maxWeight(self, pizzas: list[int]) -> int:
    c = Counter(pizzas)
    cand = sorted(c)
    n = len(pizzas)
    rounds = n // 4
    evens = rounds // 2
    odds = evens + (rounds%2)
    total = 0
    # print('init:', cand, c, (odds, evens))

    while odds > 0:
      val = cand[-1]
      cnt = min(odds, c[val])
      total += cnt * val
      odds -= cnt
      c[val] -= cnt
      if not c[val]:
        cand.pop()

    while evens > 0:
      v0 = cand[-1]
      c[v0] -= 1
      if not c[v0]:
        cand.pop()

      v1 = cand[-1]
      c[v1] -= 1
      total += v1
      if not c[v1]:
        cand.pop()

      evens -= 1

    return total
    