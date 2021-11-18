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

class SummaryRanges:
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
