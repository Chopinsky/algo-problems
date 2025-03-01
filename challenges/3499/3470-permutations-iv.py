'''
3470-permutations-iv
'''

from functools import lru_cache
from typing import List


class Solution:
  def permute(self, n: int, k: int) -> List[int]:
    @lru_cache(None)
    def calc(o: int, e: int, is_odd: bool) -> int:
      if o == 0 and e == 0:
        return 1

      if is_odd:
        # o == 0 and e > 0 for odd position is illegal hence 0
        return 0 if o == 0 else o*calc(o-1, e, False)
      
      # e == 0 and o > 0 for even position is illegal hence 0
      return 0 if e == 0 else e*calc(o, e-1, True)

    oc = (n+1) // 2
    ec = n // 2
    total = 0

    for val in range(1, n+1):
      if val%2 == 1:
        total += calc(oc-1, ec, False)
      else:
        total += calc(oc, ec-1, True)

    if k > total:
      return []

    ans = []
    nums = list(range(1, n+1))

    for _ in range(n):
      # nums is changing after using the numbers
      for j in range(len(nums)):
        val = nums[j]
        is_odd = val%2 == 1

        # illegal comb
        if ans and (val%2) == (ans[-1]%2):
          continue

        # perm count if using val at this number with all possible perm
        count = calc(oc-1, ec, False) if is_odd else calc(oc, ec-1, True)
        if k > count:
          # check the next val but remove the current perm count
          k -= count
          continue

        # use the current val
        ans.append(val)
        nums.pop(j)

        if is_odd:
          oc -= 1
        else:
          ec -= 1

        break

    return ans
