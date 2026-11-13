'''
1385-find-the-distance-value-between-two-arrays
'''


class Solution:
  def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
    cnt = 0
    for v1 in arr1:
      if all(abs(v1-v2) > d for v2 in arr2):
        cnt += 1

    return cnt
        