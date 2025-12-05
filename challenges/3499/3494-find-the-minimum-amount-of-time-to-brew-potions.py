'''
3494-find-the-minimum-amount-of-time-to-brew-potions
'''

from typing import List


class Solution:
  def minTime(self, skill: List[int], mana: List[int]) -> int:
    n = len(skill)
    m = len(mana)
    if n == 1:
      return sum(skill[0]*cost for cost in mana)

    time = [0]*n

    def update(cost: int):
      now = time[0]
      shift = 0

      for i, s in enumerate(skill):
        now += s*cost
        if i+1 < n:
          shift = max(shift, time[i+1]-now)

      now = time[0]+shift
      
      for i, s in enumerate(skill):
        now += s*cost
        time[i] = now

    for cost in mana:
      update(cost)
      # print('iter:', (i, cost), time)

    return time[-1]


        