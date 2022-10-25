'''
2446. Determine if Two Events Have Conflict

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.

Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.

Constraints:

evnet1.length == event2.length == 2.
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.
'''

from typing import List


class Solution:
  def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
    def normalize(s: str) -> int:
      src = s.split(':')
      # print(s, src)
      return 60 * int(src[0]) + int(src[1])
    
    s1, e1 = normalize(event1[0]), normalize(event1[1])
    s2, e2 = normalize(event2[0]), normalize(event2[1])
    # print('reduced:', (s1, e1), (s2, e2))
    
    if s1 >= s2:
      s1, s2 = s2, s1
      e1, e2 = e2, e1
      
    return e1 >= s2
    