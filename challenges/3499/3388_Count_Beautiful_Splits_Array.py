'''
3388. Count Beautiful Splits in an Array

[1,1,0,1,0]
[3,3,3,1,3]
[1,1,0,1,3,2,2,2]
[1,1,2,1]
[1,2,3,4]
[0,0,0,0,2,2,0,1,2,1,2]
'''

from typing import List


class Solution:
  def beautifulSplits(self, nums: List[int]) -> int:
    n = len(nums)
    lcp = [[0]*n for _ in range(n)]

    # calc z-function
    for i in range(n):
      mi, mr = i, i
      arr = lcp[i]

      for j in range(i+1, n):
        if mr >= j:
          arr[j] = min(mr-j+1, arr[j-mi+i])

        while j+arr[j] < n and nums[j+arr[j]] == nums[arr[j]+i]:
          arr[j] += 1

        if j+arr[j]-1 > mr:
          mi = j
          mr = j+arr[j]-1

    # print('init:', lcp)
    count = 0

    for i in range(n):
      for j in range(i+1, n-1):
        if lcp[0][i+1] >= i+1 and j-i >= i+1:
          count += 1
          continue

        if lcp[i+1][j+1] >= j-i:
          count += 1
          continue

    return count
