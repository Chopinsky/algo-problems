'''
1848-minimum-distance-to-the-target-element
'''


class Solution:
  def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
    n = len(nums)
    dist = n

    for i in range(n):
      if nums[i] != target:
        continue

      d0 = abs(i-start)
      if d0 > dist:
        break

      dist = d0

    return dist
        