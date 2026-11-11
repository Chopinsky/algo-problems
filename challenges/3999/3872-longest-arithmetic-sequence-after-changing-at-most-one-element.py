'''
3872-longest-arithmetic-sequence-after-changing-at-most-one-element
'''


class Solution:
  def longestArithmetic(self, nums: list[int]) -> int:
    n = len(nums)
    if all(val == nums[0] for val in nums):
      return n

    INF = float('inf')
    l = [[INF, 0], [nums[1]-nums[0], 2]]
    r = [[INF, 0], [nums[-1]-nums[-2], 2]]
    res = 2
    debug = False

    for i in range(2, n):
      d = nums[i] - nums[i-1]
      d0, l0 = l[-1]
      l.append([d, l0+1 if d == d0 else 2])
      res = max(res, l[-1][1])

    for i in range(n-2, 0, -1):
      d = nums[i] - nums[i-1]
      d0, l0 = r[-1]
      r.append([d, l0+1 if d == d0 else 2])
      res = max(res, r[-1][1])

    r = r[::-1]
    if debug:
      print('init:', l, r)

    for i in range(n):
      # matching left
      if i > 1:
        d0, ln0 = l[i-1]
        val = nums[i-1]+d0
        if val != nums[i]:
          res = max(res, ln0+1)

          if i+1 < n:
            d1 = nums[i+1]-val

            # can merge i+1
            if d1 == d0:
              res = max(res, ln0+2)

              if i+2 < n:
                d2, ln2 = r[i+1]

                # can merge rest of the right subarr
                if d2 == d0:
                  res = max(res, ln0+2+(ln2-1))
      
      # matching right
      if i+2 < n:
        d0, ln0 = r[i+1]
        val = nums[i+1]-d0
        # print('r0:', (i, nums[i]), val, (d0, ln0), res)

        if val != nums[i]:
          res = max(res, ln0+1)
          # print('r1:', i, val, (d0, ln0), res)

          # check i-1
          if i > 0:
            d1 = val-nums[i-1]

            # can merge i-1
            if d1 == d0:
              res = max(res, ln0+2)

              if i > 1:
                d2, ln2 = l[i-1]

                # can merge rest of the left subarr
                if d2 == d0:
                  res = max(res, ln0+2+(ln2-1))

      if debug:
        print('iter:', i, nums[i], res)

    return res
