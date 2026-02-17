'''
3845-maximum-subarray-xor-with-bounded-range
'''

from collections import deque


class Node:
  def __init__(self):
    self.children = {}
    self.count = 0


class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, val: int):
    curr = self.root
    for i in range(31, -1, -1):
      bit = (val>>i) & 1
      if bit not in curr.children:
        curr.children[bit] = Node()

      curr = curr.children[bit]
      curr.count += 1

  def remove(self, val: int):
    curr = self.root
    for i in range(31, -1, -1):
      bit = (val>>i) & 1
      child = curr.children[bit]
      child.count -= 1
      curr = child

  def xor(self, val: int) -> int:
    curr = self.root
    res = 0

    for i in range(31, -1, -1):
      bit = (val>>i) & 1
      flip = 1 - bit

      if (flip in curr.children) and (curr.children[flip].count > 0):
        # can go to the opposite branch and xor to 1 at bit-i
        res |= (1 << i)
        curr = curr.children[flip]
      else:
        # must follow the existing bit
        curr = curr.children[bit]

    return res


class Solution:
  def maxXor(self, nums: list[int], k: int) -> int:
    n = len(nums)

    prefix = [0]*(n+1)
    for i in range(n):
      prefix[i+1] = prefix[i] ^ nums[i]

    minq = deque()
    maxq = deque()

    t = Trie()
    t.insert(0)

    left = 0
    ans = 0

    for right in range(n):
      while minq and nums[minq[-1]] > nums[right]:
        minq.pop()

      while maxq and nums[maxq[-1]] < nums[right]:
        maxq.pop()
      
      minq.append(right)
      maxq.append(right)

      while nums[maxq[0]] - nums[minq[0]] > k:
        t.remove(prefix[left])

        if minq[0] == left:
          minq.popleft()

        if maxq[0] == left:
          maxq.popleft()

        left += 1

      ans = max(ans, t.xor(prefix[right+1]))

      # update trie with the current value
      t.insert(prefix[right+1])

    return ans

    
        