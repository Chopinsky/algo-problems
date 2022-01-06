from functools import cmp_to_key
from heapq import heappop, heappush
from typing import List


class Solution:
  '''
  There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

  You will start on the 1st day and you cannot take two or more courses simultaneously.

  Return the maximum number of courses that you can take.

  Example 1:

  Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
  Output: 3
  Explanation:
  There are totally 4 courses, but you can take 3 courses at most:
  First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
  Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
  Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
  The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

  Example 2:

  Input: courses = [[1,2]]
  Output: 1

  Example 3:

  Input: courses = [[3,2],[4,3]]
  Output: 0

  Constraints:

  1 <= courses.length <= 10 ** 4
  1 <= durationi, lastDayi <= 10 ** 4
  '''

  def scheduleCourse(self, courses: List[List[int]]) -> int:
    courses.sort(key = lambda x:x[1])
    time = 0
    hq = []

    for (duration, end) in courses:
      if time + duration <= end:
        time += duration
        heappush(hq, -duration)

      else:
        if hq and -hq[0] > duration:
            time += duration + heappop(hq)
            heappush(hq, -duration)

    return len(hq)


  # idea is that stack contains all courses that can meet the requirements,
  # then for the latest course, it can either be added to the stack if
  # the added deadline meets the course deadline; otherwise, it can always
  # replace the course that has longer duraing in the stack without breaking
  # the requirements, because the replaced course met the deadline of an
  # earlier dates, hence swapping will maintain the legilibility of the
  # latest course.
  def scheduleCourse0(self, courses: List[List[int]]) -> int:
    c = []
    for (dur, dl) in courses:
      if dl >= dur:
        c.append((dur, dl))

    def sort_by(a, b):
      if a[1] == b[1]:
        return -1 if a[0] > b[0] else 1

      return -1 if a[1] < b[1] else 1

    c.sort(key=cmp_to_key(sort_by))

    total = 0
    stack = []

    for (dur, dl) in c:
      if total+dur <= dl:
        heappush(stack, -dur)
        total += dur
      elif stack and dur < -stack[0]:
        top = -heappop(stack)
        heappush(stack, -dur)
        total += (dur-top)

    return len(stack)
