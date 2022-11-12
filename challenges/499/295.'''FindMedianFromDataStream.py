from heapq import heappush, heappushpop

class MedianFinder:
  def __init__(self):
    self.small = []
    self.big = []
    

  def addNum(self, num: int) -> None:    
    if len(self.small) < len(self.big):
      if num <= self.big[0]:
        heappush(self.small, -num)
        
      else:
        heappush(self.small, -heappushpop(self.big, num))
        # heappush(self.small, -heappop(self.big))
      
    else:
      heappush(self.big, -heappushpop(self.small, -num))
      
    # print(num, self.small, self.big)
    

  def findMedian(self) -> float:
    if len(self.small) < len(self.big):
      return self.big[0]
    
    # print('find:', self.small, self.big)
    return (self.big[0] - self.small[0]) / 2.0


  '''
  The idea is to create 2 halves: smaller ones and larger ones.
  When adding a number, either the largest in the smaller half
  spill into the larger half, or vice versa. When maintain the balance
  between the smaller and larger half when adding new numbers.
  '''
  def __init__(self):
    """
    initialize your data structure here.
    """
    # self.nums = []
    
    self.small = [] # max heap
    self.large = [] # min heap
    

  def addNum(self, num: int) -> None:
    # bisect.insort(self.nums, num)
    
    if len(self.small) == len(self.large):
      val = -heappushpop(self.small, -num)
      heappush(self.large, val)
    else:
      val = -heappushpop(self.large, num)
      heappush(self.small, val)
    

  def findMedian(self) -> float:
    if len(self.small) == len(self.large):
      return (self.large[0] - self.small[0]) / 2
    
    return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
