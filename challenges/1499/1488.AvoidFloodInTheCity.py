'''
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

Example 4:

Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9

Example 5:

Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.


Constraints:

1 <= rains.length <= 105
0 <= rains[i] <= 109
'''

from typing import List
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_right


class Solution:
  def avoidFlood(self, rains: List[int]) -> List[int]:
    days = defaultdict(list)
    for i, lake in enumerate(rains):
      if lake > 0:
        days[lake].append(i)

    # print('init:', days)
    full = set()
    q = []
    ans = []

    for i, lake in enumerate(rains):
      # dry the lake
      if lake == 0:
        if not q:
          ans.append(1)
        else:
          _, l = heappop(q)
          full.discard(l)
          ans.append(l)

        continue

      # flood
      if lake in full:
        return []

      # add
      j = bisect_right(days[lake], i)
      ans.append(-1)

      if j < len(days[lake]):
        diff = days[lake][j] - i
        heappush(q, (diff, lake))
        full.add(lake)

    return ans


  def avoidFlood(self, rains: List[int]) -> List[int]:
    n = len(rains)
    ans = [-1 if r > 0 else 0 for r in rains]

    dry_days = defaultdict(list)
    full = {}
    last_rain_day = -1

    for i, rain in enumerate(rains):
      # save the dry day in the day after the last rain day
      if rain == 0:
        dry_days[last_rain_day+1].append(i)
        continue

      # update the last rain day date
      last_rain_day = i

      # if we *must drain this lake* since it's already full
      if rain in full:
        canDrain = False

        # loop over all the "dry days" between 2 neighboring
        # rain days, find the one after the day the lake
        # was rained upon
        for d in dry_days:
          # we can darin the lake since this dry day
          # takes place after the rain day on this lake
          if d > full[rain]:
            day = dry_days[d].pop()
            ans[day] = rain

            # remove empty array if it's empty
            if not dry_days[d]:
              dry_days.pop(d)

            canDrain = True
            break

        # if we can't find a day to dry this lake,
        # return false
        if not canDrain:
          return []

      # set the lake as full on day-i
      full[rain] = i

    # fill the rest of the dry days with a random lake to drain
    for d in dry_days:
      for idx in dry_days[d]:
        ans[idx] = 1

    return ans



  def avoidFlood1(self, rains: List[int]) -> List[int]:
    n = len(rains)
    ans = [-1 if r > 0 else 0 for r in rains]

    rain_days = defaultdict(list)
    sunny_days = []
    last_lake = 1

    for i, lake in enumerate(rains):
      if lake == 0:
        sunny_days.append(i)
        continue

      rain_days[lake].append(i)
      last_lake = lake

    q = []
    for lake, days in rain_days.items():
      if len(days) <= 1:
        continue

      for i in range(len(days)-1):
        q.append((days[i+1], days[i], lake))

    q.sort(key=lambda x: x[1])

    # print(q, sunny_days)

    idx = 0
    hq = []
    lakes = set()

    for day in sunny_days:
      # print("sunny day:", day, q, hq)

      while idx < len(q) and q[idx][1] <= day:
        if q[idx][2] in lakes or q[idx][0] <= day:
          return []

        heappush(hq, q[idx])
        lakes.add(q[idx][2])
        idx += 1

      if len(hq) > 0:
        next = heappop(hq)
        ans[day] = next[2]
        lakes.remove(next[2])
      else:
        ans[day] = last_lake

    # print("remaining rainy day:", idx, hq)

    if idx < len(q) or len(hq) > 0:
      return []

    return ans
