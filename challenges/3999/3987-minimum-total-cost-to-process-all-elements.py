'''
3987-minimum-total-cost-to-process-all-elements
'''


class Solution:
  def minimumCost(self, nums: list[int], k: int) -> int:
    mod = 10**9 + 7
    curr = k
    op = 1
    cost = 0

    def calc(d: int) -> int:
      s = op
      e = op+d-1
      return ((s+e)*d) // 2

    def diff(val: int) -> int:
      if val <= curr:
        return 0

      d = val - curr
      rem = d % k
      ops = d // k
      if rem > 0:
        ops += 1

      return ops

    for val in nums:
      ops = diff(val)
      if ops > 0:
        curr += k*ops
        cost = (cost + calc(ops)) % mod
        op += ops
        # print('iter:', val, curr, ops, (cost, calc(ops)))

      curr -= val

    return cost
