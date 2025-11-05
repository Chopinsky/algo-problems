'''
3652-best-time-to-buy-and-sell-stock-using-strategy
'''

from typing import List



class Solution:
  def maxProfit(self, p: List[int], st: List[int], k: int) -> int:
    n = len(p)
    prefix = [0] * n
    pp = [val for val in p]
    
    for i in range(n):
      prefix[i] = p[i]*st[i] + (prefix[i-1] if i > 0 else 0)
      pp[i] += pp[i-1] if i > 0 else 0

    # print('init:', prefix, pp)
    result = prefix[-1] # perform no modifications
    shift = k//2

    for i in range(k-1, n):
      right = prefix[-1] - prefix[i]
      curr = pp[i] - pp[i-shift]
      left = prefix[i-k] if i >= k else 0
      result = max(result, right+curr+left)

    return result

        