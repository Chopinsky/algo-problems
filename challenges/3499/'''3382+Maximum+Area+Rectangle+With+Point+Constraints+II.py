'''
3382. Maximum Area Rectangle With Point Constraints II
'''

from typing import List

class SegmentTree:
  def __init__(self, data, default = float('inf'), func=min):
    self._default = default
    self._func = func
    self._len = len(data)
    self._size = _size = 1 << (self._len - 1).bit_length()
    self.data = [default] * (2 * _size)
    self.data[_size:_size + self._len] = data
    for i in reversed(range(_size)):
      self.data[i] = func(self.data[i + i], self.data[i + i + 1])

  def __delitem__(self, idx):
    self[idx] = self._default

  def __getitem__(self, idx):
    return self.data[idx + self._size]

  def __setitem__(self, idx, value):
    idx += self._size
    self.data[idx] = value
    idx >>= 1
    while idx:
      self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
      idx >>= 1

  def __len__(self):
    return self._len

  def query(self, start, stop):
    start += self._size
    stop += self._size

    res_left = res_right = self._default
    while start < stop:
      if start & 1:
        res_left = self._func(res_left, self.data[start])
        start += 1

      if stop & 1:
        stop -= 1
        res_right = self._func(self.data[stop], res_right)

      start >>= 1
      stop >>= 1

    return self._func(res_left, res_right)

class Solution:
  def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
    n = len(xCoord)
    x = set(xCoord + yCoord)
    cmp = {}
    for i, v in enumerate(sorted(x)):
      cmp[v] = i

    points = [(xCoord[i], yCoord[i], i) for i in range(n)]
    points.sort(key = lambda p: -p[1])
    height = [float('inf')] * n
    rights = [float('inf')] * n
    last = {}

    for x, y, pos in points:
      if x in last:
        height[pos] = last[x] - y

      last[x] = y

    k = len(cmp) + 1
    segtree = SegmentTree([float('inf')] * k)
    points.sort(key = lambda p: -p[0])
    i = 0

    for x, y, pos in points:
      while i < n and points[i][0] > x:
        segtree[cmp[points[i][1]]] = points[i][0]
        i += 1

      if height[pos] != float('inf'):
        rights[pos] = segtree.query(cmp[y], cmp[y + height[pos]] + 1)

    points.sort(key = lambda x: x[0])
    groups = {}
    for x, y, pos in points:
      if height[pos] == float('inf'):
        continue

      if (y, height[pos]) not in groups:
        groups[(y, height[pos])] = []

      groups[(y, height[pos])].append((x, pos))

    res = 0
    for y, h in groups:
      arr = groups[(y, h)]
      j = 0
      for i in range(len(arr)):
        while j + 1 < len(arr) and arr[j + 1][0] <= rights[arr[i][1]]:
          j += 1

        res = max(res, h * (arr[j][0] - arr[i][0]))

    return -1 if res <= 0 else res 
      