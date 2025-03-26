'''
3433-count-mentions-per-user
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def countMentions(self, nu: int, events: List[List[str]]) -> List[int]:
    users = [True]*nu
    events.sort(key=lambda x: (int(x[1]), -1 if x[0] == 'OFFLINE' else 1))
    # print('init:', events)
    ans = [0]*nu
    all_count = 0
    q = []

    for msg, ts, ids in events:
      ts = int(ts)
      while q and q[0][0] <= ts:
        _, id = heappop(q)
        users[id] = True

      # print('iter:', msg, ts, ids, users, ans, all_count)

      if msg == 'OFFLINE':
        id = int(ids)
        users[id] = False
        heappush(q, (ts+60, id))

      else:
        if ids == 'ALL':
          # all
          all_count += 1
        elif ids == 'HERE':
          # here
          for i in range(nu):
            if users[i]:
              ans[i] += 1

        else:
          # mention
          id_lst = ids.split(' ')
          for id in id_lst:
            id_num = int(id[2:])
            ans[id_num] += 1

    return [val+all_count for val in ans]
        