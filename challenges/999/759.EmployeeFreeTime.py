'''
We are given a list schedule of employees, which represents the working time 
for each employee. Each employee has a list of non-overlapping Intervals, and 
these intervals are in sorted order. Return the list of finite intervals
representing common, positive-length free time for all employees, also in sorted 
order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]

Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

(Even though we are representing Intervals in the form [x, y], the objects inside are 
Intervals, not lists or arrays. For example, schedule[0][0].start = 1, 
schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:
schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.
'''


from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def employee_free_time(self, schd: List[List[List[int]]]) -> List[List[int]]:
    queue = []

    for worker in schd:
      for s, e in worker:
        queue.append((s, e))

    queue.sort(key=lambda x: (x[0], -x[1]))
    last = list(queue[0])
    ans = []

    for (s, e) in queue[1:]:
      if s > last[1]:
        ans.append([last[1], s])
        last[0] = s
        last[1] = e
      else:
        last[1] = max(last[1], e)

    return ans


  def employee_free_time0(self, schd: List[List[List[int]]]) -> List[List[int]]:
    ans = []
    work_range = []

    for worker_schd in schd:
      for s, e in worker_schd:
        if not work_range:
          work_range.append(s)
          work_range.append(e)
          continue

        if s >= work_range[-1]:
          if s == work_range[-1]:
            work_range[-1] = e
          else:
            work_range.append(s)
            work_range.append(e)

          continue

        if e <= work_range[0]:
          if e == work_range[0]:
            work_range[0] = s
          else:
            work_range = [s, e] + work_range

          continue

        sdx = bisect_left(work_range, s)
        edx = bisect_right(work_range, e) - 1

        # if it's a start time of the range
        if sdx % 2 == 0:
          start = s
        else:
          sdx -= 1
          start = work_range[sdx]

        if edx % 2 == 1:
          end = e
        else:
          edx += 1
          end = work_range[edx]

        work_range = work_range[:sdx] + [start, end] + work_range[min(edx+1, len(work_range)):]

    # print(work_range)

    for i in range(1, len(work_range), 2):
      if i+1 < len(work_range):
        ans.append([work_range[i], work_range[i+1]])

    return ans


s = Solution()
t = [
  [[[[1,2], [5,6]], [[1,3], [4, 10]]], [[3, 4]]],
  [[[[1,3], [6,7]], [[2,4]], [[2,5], [9, 12]]], [[5,6], [7,9]]],
]

for schd, ans in t:
  print('\n==============\nTest case:', schd)
  print('Expected:', ans)
  print('Gotten  :', s.employee_free_time(schd))
