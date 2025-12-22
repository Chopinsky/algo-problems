'''
3508-implement-router
'''

from collections import defaultdict
from heapq import heappush, heappop
from typing import List
from bisect import bisect_left, bisect_right


class Router:
    def __init__(self, memoryLimit: int):
      self.size = memoryLimit
      self.cache = set()
      self.h = []
      self.idx = defaultdict(int)
      self.pck = defaultdict(list)
      self.curr = 0
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
      if (source, destination, timestamp) in self.cache:
        return False

      if len(self.cache) == self.size:
        self.forwardPacket()

      heappush(self.h, (timestamp, self.curr, source, destination))
      self.cache.add((source, destination, timestamp))
      self.pck[destination].append(timestamp)
      self.curr += 1

      return True
        

    def forwardPacket(self) -> List[int]:
      if not self.h:
        return []

      t, _, s, d = heappop(self.h)
      self.idx[d] += 1
      self.cache.discard((s, d, t))

      return [s, d, t]
        

    def getCount(self, d: int, st: int, et: int) -> int:
      if d not in self.pck or self.idx[d] >= len(self.pck[d]):
        return 0

      l0 = self.idx[d]
      l1 = bisect_left(self.pck[d], st)
      l = max(l0, l1)
      r = bisect_right(self.pck[d], et)-1
      
      if l > r:
        return 0

      return r-l+1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)