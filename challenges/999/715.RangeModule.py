'''
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 
Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)

Constraints:

1 <= left < right <= 10^9
At most 104 calls will be made to addRange, queryRange, and removeRange.
'''

from bisect import bisect_left, bisect_right

class RangeModule:
    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        start = bisect_left(self.track, left)
        end = bisect_right(self.track, right)
        replace = []
        
        if start % 2 == 0:
            replace.append(left)
            
        if end % 2 == 0:
            replace.append(right)
			
        self.track[start:end] = replace

    def removeRange(self, left, right):
        start = bisect_left(self.track, left)
        end = bisect_right(self.track, right)
        replace = []
        
        if start % 2 == 1:
            replace.append(left)
            
        if end % 2 == 1:
            replace.append(right)
			
        self.track[start:end] = replace
		
    def queryRange(self, left, right):
        start = bisect_right(self.track, left)
        end = bisect_left(self.track, right)
		
        return start == end and start % 2 == 1

class RangeModule:
  def __init__(self):
    self.left = []
    self.right = []

  def addRange(self, left: int, right: int) -> None:
    if not self.left:
      self.left.append(left)
      self.right.append(right)
      return
    
    # insert to the head
    if right <= self.left[0]:
      if right < self.left[0]:
        self.left = [left] + self.left
        self.right = [right] + self.right
      else:
        self.left[0] = left
        
      return
    
    # append to the tail
    if left >= self.right[-1]:
      if left > self.right[-1]:
        self.left.append(left)
        self.right.append(right)
      else:
        self.right[-1] = right
        
      return
    
    # all ranges in [ldx, rdx] will be merged
    ldx = bisect_left(self.right, left)
    rdx = bisect_right(self.left, right) - 1
    
    # no overlaps, insert into the gap
    if right < self.left[ldx]:
      self.left = self.left[:ldx] + [left] + self.left[ldx:]
      self.right = self.right[:ldx] + [right] + self.right[ldx:]
      return
    
    # no overlaps, insert into the gap
    if rdx >= 0 and left > self.right[rdx]:
      self.left = self.left[:rdx] + [left] + self.left[rdx:]
      self.right = self.right[:rdx] + [right] + self.right[rdx:]
      return
    
    # merge to the left-most range
    if ldx <= rdx:
      self.left[ldx] = min(self.left[ldx], left)
      self.right[ldx] = max(self.right[rdx], right)
      
      del self.left[ldx+1:rdx+1]
      del self.right[ldx+1:rdx+1]


  def queryRange(self, left: int, right: int) -> bool:
    if not self.left or right <= self.left[0] or left >= self.right[-1]:
      return False
    
    ldx = bisect_right(self.left, left) - 1
    if ldx < 0 or ldx >= len(self.left):
      return False
    
    return self.right[ldx] >= right


  def removeRange(self, left: int, right: int) -> None:
    # nothing to remove from
    if not self.left or right <= self.left[0] or left >= self.right[-1]:
      return
    
    ldx = bisect_left(self.right, left)
    rdx = bisect_right(self.left, right) - 1
    
    # nothing to remove from
    if rdx < ldx or right <= self.left[ldx] or left >= self.right[rdx]:
      return
    
    # breaking up a range into 2
    if ldx == rdx:
      # remove the entire range
      if left <= self.left[ldx] and right >= self.right[ldx]:
        del self.left[ldx]
        del self.right[ldx]
        return 
      
      # remove the left portion
      if left <= self.left[ldx]:
        self.left[ldx] = right
        return
        
      # remove the right portion
      if right >= self.right[ldx]:
        self.right[ldx] = left
        return
        
      # remove the middle portion, split the range into 2
      original_right = self.right[ldx]
      self.right[ldx] = left
      
      self.left = self.left[:ldx+1] + [right] + self.left[ldx+1:]
      self.right = self.right[:ldx+1] + [original_right] + self.right[ldx+1:]
      
      return

    if left <= self.left[ldx]:
      ll = []
      lr = []
    else:
      ll = [self.left[ldx]]
      lr = [left]
      
    if right >= self.right[rdx]:
      rl = []
      rr = []
    else:
      rl = [right]
      rr = [self.right[rdx]]
      
    self.left = self.left[:ldx] + ll + rl + self.left[rdx+1:]
    self.right = self.right[:ldx] + lr + rr + self.right[rdx+1:]
      

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
