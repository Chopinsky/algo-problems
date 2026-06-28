'''
1846-maximum-element-after-decreasing-and-rearranging
'''

from typing import List


class Solution:
  def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    arr.sort()
    arr[0] = 1

    for i in range(1, len(arr)):
      if arr[i] <= arr[i-1]:
        continue

      arr[i] = arr[i-1]+1

    # print('done:', arr)
    return arr[-1]
        