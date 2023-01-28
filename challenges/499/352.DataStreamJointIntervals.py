'''
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int val) Adds the integer val to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi].
 

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

Constraints:

0 <= val <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.
 

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?
'''

from heapq import heappop, heappush
from typing import List
from bisect import bisect_left


class SummaryRanges:
  def __init__(self):
    self.arr = []
    self.stack = []
    self.seen = set()


  def addNum(self, value: int) -> None:
    if value not in self.seen:
      heappush(self.stack, value)
      self.seen.add(value)

      
  def nxt_range_to_merge(self):
    left = heappop(self.stack)
    right = left
    
    while self.stack and right+1 == self.stack[0]:
      right = heappop(self.stack)
      
    return (left, right)
      
      
  def getIntervals(self) -> List[List[int]]:
    if not self.stack:
      return self.arr
    
    nxt_arr = []
    idx, n = 0, len(self.arr)
    # print(self.stack, self.arr, n)
    
    while self.stack:
      # get the range from the next numbers batch from the data
      # stream since the last query
      l, r = self.nxt_range_to_merge()
      
      # merge this range with the last extended range if overlapping
      if nxt_arr and nxt_arr[-1][1] >= l-1:
        last_left, last_right = nxt_arr.pop()
        l = min(l, last_left)
        r = max(r, last_right)
      
      # adding all ranges to the left of the current range in action
      while idx < n and self.arr[idx][1] < l-1:
        nxt_arr.append(self.arr[idx])
        idx += 1
        
      # merging all overlapping ranges
      while idx < n and self.arr[idx][0] <= r+1:
        l = min(l, self.arr[idx][0])
        r = max(r, self.arr[idx][1])
        idx += 1
        
      nxt_arr.append((l, r))
      
    if idx < n:
      nxt_arr += self.arr[idx:]
      
    self.arr = nxt_arr
    
    return nxt_arr


class SummaryRanges0:
  def __init__(self):
    self.store = []


  def addNum(self, val: int) -> None:
    if not self.store or val > self.store[-1]:
      if not self.store or val != self.store[-1] + 1:
        self.store += [val, val]
      else:
        self.store[-1] = val
        
      return
    
    if val < self.store[0]:
      if val == self.store[0] - 1:
        self.store[0] = val
      else:
        self.store = [val, val] + self.store
        
      return
    
    idx = bisect_left(self.store, val)
    if idx >= len(self.store):
      self.store += [val, val]
      return
    
    # already included, done
    if self.store[idx] == val or idx % 2 == 1:
      return
    
    # connecting neighboring ranges
    if self.store[idx] == val + 1 and self.store[idx-1] == val - 1:
      self.store = self.store[:idx-1] + self.store[idx+1:]
      return
    
    # extending right range
    if self.store[idx] == val + 1:
      self.store[idx] = val
      return
    
    # extending left range
    if self.store[idx-1] == val - 1:
      self.store[idx-1] = val
      return
    
    # insert
    self.store = self.store[:idx] + [val, val] + self.store[idx:]


  def getIntervals(self) -> List[List[int]]:
    ans = []
    for i in range(0, len(self.store), 2):
      ans.append([self.store[i], self.store[i+1]])
    
    return ans        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
