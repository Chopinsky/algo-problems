'''
3091-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k
'''


class Solution:
  def minOperations(self, k: int) -> int:
    if k <= 2:
      return k-1

    def check(ops: int) -> bool:
      if ops+1 >= k:
        return True

      val = 1
      while ops > 0:
        val += 1
        ops -= 1
        if val*(ops+1) >= k:
          return True

      return False

    l, r = 1, k
    last = r

    while l <= r:
      mid = (l+r) // 2
      if check(mid):
        last = mid
        r = mid-1
      else:
        l = mid+1

    return last
        