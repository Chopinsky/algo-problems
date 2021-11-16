'''
Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2

Constraints:

1 <= arr.length <= 2 * 10^4
1 <= arr[i] <= 2 * 10^4
0 <= left <= right < arr.length
threshold <= right - left + 1
2 * threshold > right - left + 1
At most 104 calls will be made to query.
'''


from typing import List
from collections import defaultdict
from random import randint
from bisect import bisect_left, bisect_right
from math import isqrt


class MajorityChecker0:
  def __init__(self, arr: List[int]):
    self.idx = defaultdict(list)
    for i, val in enumerate(arr):
      self.idx[val].append(i)

    n = len(arr)
    self.size = isqrt(n)
    self.bucket = []
    
    def update(i: int) -> int:
      l = self.size * i
      if l >= n:
        return

      r = min(n, l + self.size)
      curr = 0
      count = 0

      for val in arr[l:r]:
        if val == curr:
          count += 1
        else:
          count -= 1
          if count <= 0:
            curr = val
            count = 1

      self.bucket.append(curr)
      return r

    idx = 0
    while idx < n:
      idx = update(idx)


  # idea is that the majority number must be the majority number
  # in at least 1 of the buckets that cover the [left, right] range
  def query(self, left: int, right: int, th: int) -> int:
    ldx = left // self.size
    rdx = min(len(self.bucket) - 1, right // self.size) + 1

    for i in range(ldx, rdx):
      num = self.bucket[i]
      l = bisect_left(self.idx[num], left)
      r = bisect_right(self.idx[num], right)
      
      if r-l >= th:
        return num
      
    return -1


class MajorityChecker:
  def __init__(self, arr: List[int]):
    self.idx = defaultdict(list)
    self.src = arr
    
    for i, val in enumerate(arr):
      self.idx[val].append(i)


  # the idea is that by randomly selecting a number in the
  # range, we should be able to hit the majority item at 
  # least once
  def query(self, left: int, right: int, th: int) -> int:
    for _ in range(32):
      num = self.src[randint(left, right)]
      l = bisect_left(self.idx[num], left)
      r = bisect_right(self.idx[num], right)
      
      if r-l >= th:
        return num
      
    return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)