'''
Given an empty set of intervals, implement a data structure that can:

Add an interval to the set of intervals.
Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:

CountIntervals() Initializes the object with an empty set of intervals.
void add(int left, int right) Adds the interval [left, right] to the set of intervals.
int count() Returns the number of integers that are present in at least one interval.
Note that an interval [left, right] denotes all the integers x where left <= x <= right.

Example 1:

Input
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
Output
[null, null, null, 6, null, 8]

Explanation
CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. 
countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count();    // return 6
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
countIntervals.count();    // return 8
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 5 and 6 are present in the interval [5, 8].
                           // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
                           // the integers 9 and 10 are present in the interval [7, 10].

Constraints:

1 <= left <= right <= 10^9
At most 10^5 calls in total will be made to add and count.
At least one call will be made to count.
'''


class Node:
  def __init__(self, l: int, r: int, is_leaf=True):
    self.is_leaf = is_leaf
    self.l = l
    self.r = r
    self.left = None
    self.right = None
    
    
  def insert(self, l: int, r: int):
    # print('insert:', (self.l, self.r), (l, r))
    # must split here
    if r < self.l-1 or l > self.r+1:
      root = Node(min(self.l, l), max(self.r, r), is_leaf=False)
      other = Node(l, r)

      if r < self.l:
        root.left = other
        root.right = self
      else:
        root.left = self
        root.right = other

      return root, r-l+1
        
    # update leaf leaf
    old_cnt = self.r - self.l + 1
    self.l = min(self.l, l)    
    self.r = max(self.r, r)
    
    if self.is_leaf:
      delta = (self.r-self.l+1) - old_cnt 
      return self, delta
    
    left = self.left
    right = self.right
    
    # not in either segment
    if l > left.r + 1 and r < right.l - 1:
      # add the range to the left/right if it's shorter
      if r-left.l >= right.r-l:
        self.right, d = right.insert(l, r)
      else:
        self.left, d = left.insert(l, r)
        
    # only intersect with the left segment
    elif r < right.l - 1:
      self.left, d = left.insert(l, r)
    
    # only intersect with the right segment
    elif l > left.r + 1:
      self.right, d = right.insert(l, r)
      
    # intersect with both segment
    else:
      m = (left.r + right.l) // 2
      self.left, d0 = left.insert(l, m)
      
      if m+1 <= r:
        self.right, d1 = right.insert(m+1, r)
      else:
        d1 = 0
        
      d = d0 + d1
      
    # if we can merge the leaves
    if left.is_leaf and right.is_leaf and left.r+1 >= right.l:
      self.is_leaf = True
      self.left = None
      self.right = None
    
    # print('added:', d)
    return self, d
  

class CountIntervals:
  def __init__(self):
    self.c = 0
    self.root = None


  def add(self, left: int, right: int) -> None:
    if not self.root:
      self.root = Node(left, right)
      self.c = right - left + 1
      return
    
    # print('start add:', left, right)
    self.root, d = self.root.insert(left, right)
    self.c += d
    

  def count(self) -> int:
    return self.c


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()