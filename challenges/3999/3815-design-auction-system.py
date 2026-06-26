'''
3815-design-auction-system
'''

from collections import defaultdict
from heapq import heappush, heappop


class AuctionSystem:
  def __init__(self):
    self.s: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    self.b: dict[tuple[int, int], int] = {}

  def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
    self.b[userId, itemId] = bidAmount
    heappush(self.s[itemId], (-bidAmount, -userId))

  def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
    self.addBid(userId, itemId, newAmount)

  def removeBid(self, userId: int, itemId: int) -> None:
    if (userId, itemId) in self.b:
      del self.b[userId, itemId]

  def getHighestBidder(self, itemId: int) -> int:
    # pop invalid values
    while self.s[itemId]:
      amount, userId = self.s[itemId][0]
      amount = -amount
      userId = -userId

      if (userId, itemId) in self.b and self.b[userId, itemId] == amount:
        break

      heappop(self.s[itemId])

    return -self.s[itemId][0][1] if self.s[itemId] else -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)