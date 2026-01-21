'''
3680-generate-schedule
'''

from typing import List


class Solution:
  def generateSchedule(self, n: int) -> List[List[int]]:
      res = []
      if n < 5:
        return res

      if n%2:
        # Adjacent pairs
        for i in range(0, 2*n, 2):
          res.append([i%n, (i + 1)%n])

        for i in range(0, 2*n, 2):
          res.append([(i + 1)%n, i%n])

      else:
        # Adjacent pairs
        for i in range(0, n, 2):
          res.append([i, i + 1])

        for i in range(0, n, 2):
          res.append([i + 1, i])

        for i in range(1, n, 2):
          res.append([i, (i + 1)%n])

        for i in range(1, n, 2):
          res.append([(i + 1)%n, i])

      for diff in range(2, (n + 1)//2):
        # find pairs that are diff apart
        start = res[-1][0] + 1
        for i in range(start, start + n):
          res.append([i%n, (i + diff)%n])
        
        start = res[-1][-1] - 1
        for i in range(start, start + n):
          res.append([(i + diff)%n, i%n])
          
      if n%2 == 0:
        # find pairs that are n/2 apart
        start = res[-1][0] - 1
        for i in range(start, start + n):
          res.append([i%n, (i + n//2)%n])

      return res

  def generateSchedule(self, n: int) -> List[List[int]]:
    if n <= 3:
      return []

    res = []
    cand = []
    for i in range(n-1):
      for j in range(i+1, n):
        cand.append((i, j))
        cand.append((j, i))

    team = [2*(n-1)]*n
    played = set()

    def iter() -> bool:
      if len(res) == n*(n-1):
        return True

      lst = sorted(cand, key=lambda x: team[x[0]]+team[x[1]])

      while lst:
        i, j = lst.pop()
        if res and (i in res[-1] or j in res[-1]):
          continue

        if (i, j) in played:
          continue

        played.add((i, j))
        res.append((i, j))
        team[i] -= 1
        team[j] -= 1
        # print('iter:', (i, j), res)

        if iter():
          return True

        team[i] += 1
        team[j] += 1
        res.pop()
        played.discard((i, j))

      return False

    if not iter():
      return []

    return res
        