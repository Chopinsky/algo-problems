'''
731. My Calendar II
'''

from bisect import insort


class MyCalendarTwo:
  def __init__(self):
    self.stack = []
    self.cnt = 0

  def book(self, start: int, end: int) -> bool:
    cnt = 0
    # self.cnt += 1
    # print(self.cnt, 'book:', (start, end), self.stack)
    
    stack = self.stack.copy()
    insort(stack, (start, 1))
    insort(stack, (end, -1))
    
    for t0, tp in stack:
      if tp == -1:
        cnt -= 1
      else:
        cnt += 1
      
      # print('iter:', t0, cnt)
      if cnt > 2:
        return False
    
    self.stack = stack
    
    return True
  
  
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)