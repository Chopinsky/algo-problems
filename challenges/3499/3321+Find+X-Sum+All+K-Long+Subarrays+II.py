'''
3321. Find X-Sum of All K-Long Subarrays II
'''

from sortedcontainers import SortedList
from collections import Counter
from typing import List
from bisect import bisect_left


class Solution:
  '''
  the idea is to maintain 2 sorted list: top and bottom, where top holds the top-x
  (count, value) pairs, and the bottom holds the rest pairs in the sliding window
  of size-k; then we slide the window, update the top vs. bottom lists, and update
  the sum of the top list;
  '''
  def findXSum(self, A: List[int], K: int, X: int) -> List[int]:
    bot = SortedList()
    top = SortedList()
    count = Counter()
    cur_sum = 0
  
    def contains(sorted_list, element):
      idx = bisect_left(sorted_list, element)
      return idx < len(sorted_list) and sorted_list[idx][0] == element[0] and sorted_list[idx][1] == element[1]

    def update(v: int, c: int):
      nonlocal cur_sum

      if count[v]:
        if contains(bot, (count[v], v)):
          bot.remove((count[v], v))
        else:
          top.remove((count[v], v))
          cur_sum -= count[v] * v

      count[v] += c
      
      # add to the bottom for now, will rebalance
      if count[v]:
        bot.add((count[v], v))

    def rebalance():
      nonlocal cur_sum
      
      while bot and len(top) < X:
        c0, v0 = bot.pop()
        cur_sum += v0 * c0
        top.add((c0, v0))

      while bot and bot[-1] > top[0]:
        c0, v0 = bot.pop()
        c1, v1 = top.pop(0)
        cur_sum += v0*c0 - v1*c1
        bot.add((c1, v1))
        top.add((c0, v0))
    
    ans = []
    for i in range(len(A)):
      update(A[i], 1)
      if i >= K:
        update(A[i-K], -1)

      rebalance()
      if i >= K - 1:
        ans.append(cur_sum)

    return ans
        