'''
3885-design-event-manager
'''

from heapq import heappush, heappop


class EventManager:
  def __init__(self, events: list[list[int]]):
    self.stack = sorted([-p, i] for [i, p] in events)
    self.pri = {i:-p for [i, p] in events}
    # print('init:', self.stack, self.pri)

  def updatePriority(self, eventId: int, newPriority: int) -> None:
    if eventId not in self.pri:
      return

    self.pri[eventId] = -newPriority
    self._clean()

    heappush(self.stack, [-newPriority, eventId])

  def pollHighest(self) -> int:
    if not self.pri:
      return -1

    self._clean()
    if not self.stack:
      return -1

    _, id = heappop(self.stack)
    del self.pri[id]

    return id

  def _clean(self):
    while self.stack and (self.stack[0][1] not in self.pri or self.stack[0][0] != self.pri[self.stack[0][1]]):
      heappop(self.stack)


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()