'''
There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

The room has a size of at least minSizej, and
abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the j-th query.

Example 1:

Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
Output: [3,-1,3]
Explanation: The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.

Example 2:

Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
Output: [2,1,3]
Explanation: The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.

Constraints:

n == rooms.length
1 <= n <= 105
k == queries.length
1 <= k <= 104
1 <= roomIdi, preferredj <= 10 ** 7
1 <= sizei, minSizej <= 10 ** 7
'''

from typing import List, Dict
import bisect
import collections

class Solution:
  def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
    # rooms with largest rooms in the front of the list
    rooms.sort(key=lambda x: -x[1])

    # queries with largest min-rooms in the front of the list
    q = [(i, query[0], query[1]) for i, query in enumerate(queries)]
    q.sort(key=lambda x: -x[2])

    # sorted array containing ids
    ids = []

    # inline search function to find the closest pid in the rooms meeting
    # the requirements
    def search(pid):
      if len(ids) == 0:
        return -1

      cands = []
      i = bisect.bisect_right(ids, pid)

      # left to the target pid
      if i > 0:
        cands.append(ids[i-1])

      # right to or on top of the target pid
      if i < len(ids):
        cands.append(ids[i])

      # get the min diff between left and right/on-top ids
      return min(cands, key=lambda x: abs(x-pid))

    n, k, i = len(rooms), len(queries), 0
    ans = [-1] * k

    for (idx, pid, ms) in q:
      # add rooms that meet the min-size requirements
      while i < n and rooms[i][1] >= ms:
        # insrot will insert element into the array in O(N) time
        bisect.insort(ids, rooms[i][0])
        i += 1

      # find the room ids that's closest to the pid
      ans[idx] = search(pid)

    return ans


  # same idea, but `merge` is too slow
  def closestRoom1(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
    rooms.sort()
    ans = [-1] * len(queries)
    sizes = collections.defaultdict(list)

    for i, [id, s] in enumerate(rooms):
      sizes[s].append(id)

    q = [(i, query[0], query[1]) for i, query in enumerate(queries)]
    q.sort(key=lambda x: -x[2])

    s = q[0][2]
    r = self.merge([], sizes, s, max(s, max(sizes))+1)

    # print("sizes:", sizes)
    # print("query:", q)
    # print("init:", r, s, max(s, max(sizes)))

    for (i, pid, ms) in q:
      if ms != s:
        r = self.merge(r, sizes, ms, s)
        s = ms

      # print(i, pid, ms, s, r)

      if len(r) == 0:
        continue

      idx = bisect.bisect(r, pid)
      if idx >= len(r):
        ans[i] = r[idx-1]
      elif idx == 0:
        ans[i] = r[idx]
      else:
        f, b = r[idx-1], r[idx]
        if abs(pid - f) <= abs(b - pid):
          ans[i] = f
        else:
          ans[i] = b

    return ans


  def merge(self, src: List[int], sizes: Dict[int, List[int]], start: int, end: int) -> List[int]:
    ans = src
    temp = []

    for s in range(start, end):
      if s not in sizes:
        continue

      rooms = sizes[s]
      if len(ans) == 0:
        ans = rooms
        temp.clear()
        continue

      i, j = 0, 0
      while i < len(ans) or j < len(rooms):
        if i >= len(ans):
          temp.append(rooms[j])
          j += 1
          continue

        if j >= len(rooms):
          temp.append(ans[i])
          i += 1
          continue

        if ans[i] < rooms[j]:
          temp.append(ans[i])
          i += 1
        else:
          temp.append(rooms[j])
          j += 1

      # print("merge for:", s, rooms, ans, temp)
      ans, temp = temp, ans
      temp.clear()

    # print("merged:", src, ans, start, end)

    return ans


  def closestRoom2(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
    max_room = max(rooms)
    tree = {}

    for room in rooms:
      self.update(tree, room[1], room[0], max_room[1])

    ans = []
    for q in queries:
      res = self.query(tree, q[1], q[0], max_room[1])
      ans.append(res)

    return ans


  def update(self, tree: Dict[int, List[int]], s: int, id: int, max_size: int):
    s = max_size - s + 1
    while s <= max_size:
      bisect.insort(tree[s], id)
      s += s & (-s)


  def query(self, tree: Dict[int, List[int]], s: int, id: int, max_size: int):
    ans = -1
    diff = -1

    while s > 0:
      if s not in tree:
        continue

      src = tree[s]
      idx = bisect.bisect_right(src, id)
      sid = -1
      d0 = -1

      if idx < len(src):
        d0 = abs(id - src[idx])
        sid = src[idx]

      if idx > 0:
        d1 = abs(id - src[idx-1])
        if d0 < 0 or d1 <= d0:
          sid = src[idx-1]
          d0 = d1

      if d0 >= 0 and ((diff < 0) or (d0 < diff) or (d0 == diff and sid < ans)):
        ans = sid
        diff = d0

    return ans
