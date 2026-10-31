'''
3826-find-the-smallest-balanced-index
'''


class Solution:
  def smallestBalancedIndex(self, nums: list[int]) -> int:
    l = []
    n = len(nums)

    for i in range(n):
      if i == 0:
        s = 0
      else:
        s = l[-1] + nums[i-1]

      l.append(s)

    res = -1
    curr = 1

    for i in range(n-1, -1, -1):
      if i == n-1:
        curr = 1
      else:
        curr *= nums[i+1]

      if curr > l[i]:
        break

      if curr == l[i]:
        res = i

    # print('init:', l, res)
    return res        
    