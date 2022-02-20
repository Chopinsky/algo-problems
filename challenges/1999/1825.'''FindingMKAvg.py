'''
You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.

Example 1:

Input
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
Output
[null, null, null, -1, null, 3, null, null, null, 5]

Explanation
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // current elements are [3]
obj.addElement(1);        // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10);       // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
                          // After removing smallest and largest 1 element the container will be [3].
                          // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5);        // current elements are [3,1,10,5]
obj.addElement(5);        // current elements are [3,1,10,5,5]
obj.addElement(5);        // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
                          // After removing smallest and largest 1 element the container will be [5].
                          // The average of [5] equals 5/1 = 5, return 5
 
Constraints:

3 <= m <= 10^5
1 <= k*2 < m
1 <= num <= 10^5
At most 10^5 calls will be made to addElement and calculateMKAverage.
'''


from heapq import heappop, heapify, heappush, heappushpop
from collections import deque


class MKAverage:
  def __init__(self, m: int, k: int):
    self.m, self.k = m, k
    self.arr = [0] * m
    self.score = 0
    
    # lh1 == low, rh1 == mid+high
    self.lh1, self.rh1 = self.heap_init(m, k)
    # lh2 == low+mid, rh2 = high
    self.lh2, self.rh2 = self.heap_init(m, m - k)

    
  # initiailize the heaps
  def heap_init(self, p1, p2):
    h1 = [(0, i) for i in range(p1-p2, p1)]
    h2 = [(0, i) for i in range(p1-p2)]
    heapify(h1)
    heapify(h2)
    
    return (h1, h2)

  
  # move numbers between 2 heaps, and calculate
  # the score changes from this move
  def update(self, lh, rh, num):
    score, idx = 0, len(self.arr)
    pop_idx = idx - self.m
    
    # push the number to the right side
    if num > rh[0][0]:
      heappush(rh, (num, idx))

      if self.arr[pop_idx] <= rh[0][0]:
        if rh[0][1] >= pop_idx: 
          score += rh[0][0]
          
        score -= self.arr[pop_idx]
        heappush(lh, (-rh[0][0], rh[0][1]))
        heappop(rh)
            
    # push the number to the left side
    else:
      heappush(lh, (-num, idx))
      score += num
      
      if self.arr[pop_idx] >= rh[0][0]: 
        heappush(rh, (-lh[0][0], lh[0][1]))
        q = heappop(lh)
        score += q[0]
        
      else:
        score -= self.arr[pop_idx]

    while lh and lh[0][1] <= pop_idx: 
      heappop(lh)  # lazy-deletion
      
    while rh and rh[0][1] <= pop_idx: 
      heappop(rh)  # lazy-deletion

    return score

  
  def addElement(self, num):
    t1 = self.update(self.lh1, self.rh1, num)
    t2 = self.update(self.lh2, self.rh2, num)

    self.arr.append(num)
    self.score += (t2 - t1)

      
  def calculateMKAverage(self):
    if len(self.arr) < 2*self.m: 
      return -1

    return self.score // (self.m - 2*self.k)


# Create a node
class Node:
  def build_tree(arr):
    if not arr:
      return None
    
    idx = len(arr) // 2
    root = Node(arr[idx])
    
    root.left = Node.build_tree(arr[:idx])
    root.right = Node.build_tree(arr[idx+1:])
    
    return root
  
  
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None


  # Insert a node
  def insert(self, key):
    curr = self
    while True:
      if key[0] <= curr.key[0]:
        if not curr.left:
          curr.left = Node(key)
          break

        curr = curr.left

      else:
        if not curr.right:
          curr.right = Node(key)
          break

        curr = curr.right
  
  
  # Find the inorder successor
  def min_val(self):
    curr = self

    # Find the leftmost leaf
    while curr.left:
      curr = curr.left

    return curr.key
  
  
  def max_val(self):
    curr = self
    
    while curr.right:
      curr = curr.right
      
    return curr.key
  
  
  def del_min(self):
    curr = self
    parent = None
    
    while curr.left:
      parent = curr
      curr = curr.left
      
    if not parent:
      return self.right, self.key
    
    parent.left = curr.right
    return self, curr.key
  
  
  def del_max(self):
    curr = self
    parent = None
    
    while curr.right:
      parent = curr
      curr = curr.right
      
    if not parent:
      return self.left, self.key
    
    parent.right = curr.left
    return self, curr.key
  
  
class MKAverage0:
  def __init__(self, m: int, k: int):
    self.m, self.k = m, k
    self.q = []
    self.idx = 0
    self.range_sum = 0
    self.init = False
  
  
  def build(self):
    self.init = True
    base = sorted(self.q)
    
    self.low = [(-val[0], val[1]) for val in base[:self.k]]
    heapify(self.low)

    self.mid = base[self.k:-self.k]
    self.high = base[-self.k:]

    self.range_sum = sum(val[0] for val in self.mid)
    
  
  def addElement(self, num: int) -> None:
    self.q.append((num, self.idx))
    self.idx += 1
  
  
  def calculateMKAverage(self) -> int:
    if len(self.q) < self.m:
      return -1
    
    if len(self.q) == self.m:
      if not self.init:
        self.build()

      return self.range_sum // (self.m - 2*self.k)
      
    #todo
      
    return self.range_sum // (self.m - 2*self.k)
    
    
class MKAverage0:
  def __init__(self, m: int, k: int):
    self.m = m
    self.k = k
    self.idx = 0
    self.q = deque([])
    self.range_sum = 0
    self.low = []
    self.mid = None
    self.high = []
    
    
  def get_from(self, val: int) -> int:
    # print(val, self.low, self.mid, self.high)
    if val <= -self.low[0][0]:
      return 0
    
    if val >= self.high[0][0]:
      return 2
    
    return 1
  
  
  def refresh(self, idx: int):
    while self.low and self.low[0][1] <= idx:
      heappop(self.low)
      
    while self.high and self.high[0][1] <= idx:
      heappop(self.high)
    
    
  def addElement(self, num: int) -> None:
    curr = (num, self.idx)
    self.q.append(curr)
    self.idx += 1
    
    # not having enough numbers in queue, only insert
    if self.idx < self.m:
      return
      
    if self.idx == self.m:
      arr = sorted(self.q)
      
      self.low = [(-v[0], v[1]) for v in arr[:self.k]]
      self.high = arr[-self.k:]
      heapify(self.low)
      heapify(self.high)
      
      self.mid = Node.build_tree(arr[self.k:-self.k])
      # self.mid = arr[self.k:-self.k]
      self.range_sum = sum(v[0] for v in arr[self.k:-self.k])
      
      return
    
    # print('add ->', curr, self.low, self.mid, self.high, self.range_sum, self.q)
    val, idx = self.q.popleft()
    pop = self.get_from(val)
    push = self.get_from(num)
    # print(pop, push, (val, idx))
    
    # pop past numbers
    self.refresh(idx)
    
    if push == pop:
      if push == 0:
        heappush(self.low, (-curr[0], curr[1]))
      elif push == 2:
        heappush(self.high, curr)
      else:
        # insort(self.mid, curr)
        if not self.mid:
          self.mid = Node(curr)
        else:
          self.mid.insert(curr)
          
        self.range_sum += num - val
        
    else:
      if pop == 0:
        if push == 2:
          curr = heappushpop(self.high, curr)
          
        # insort(self.mid, curr)
        # head, self.mid = self.mid[0], self.mid[1:]
        if not self.mid:
          self.mid = Node(curr)
        else:
          self.mid.insert(curr)
          
        self.mid, head = self.mid.del_min()
        
        while self.mid and head[1] <= idx:
          self.mid, head = self.mid.del_min()
          
        self.range_sum += curr[0] - head[0]
        heappush(self.low, (-head[0], head[1]))          
        
      elif pop == 2:
        if push == 0:
          curr = heappushpop(self.low, (-curr[0], curr[1]))
          curr = (-curr[0], curr[1])
          
        # insort(self.mid, curr)
        # tail, self.mid = self.mid[-1], self.mid[:-1]
        if not self.mid:
          self.mid = Node(curr)
        else:
          self.mid.insert(curr)
          
        self.mid, tail = self.mid.del_max()
        
        while self.mid and tail[1] <= idx:
          self.mid, tail = self.mid.del_max()
        
        self.range_sum += curr[0] - tail[0]
        heappush(self.high, tail)
        
      else:
        if push == 0:
          curr = heappushpop(self.low, (-curr[0], curr[1]))
          curr = (-curr[0], curr[1])
          
          # insort(self.mid, curr)
          if not self.mid:
            self.mid = Node(curr)
          else:
            self.mid.insert(curr)
            
          self.range_sum += curr[0] - val
          
        else:
          curr = heappushpop(self.high, curr)
          
          # insort(self.mid, curr)
          if not self.mid:
            self.mid = Node(curr)
          else:
            self.mid.insert(curr)
            
          self.range_sum += curr[0] - val
          
    # print('pos:', self.low, self.mid, self.high, self.range_sum)
  
  
  def calculateMKAverage(self) -> int:
    if len(self.q) < self.m:
      return -1
    
    return self.range_sum // (self.m - 2*self.k)

  
# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()