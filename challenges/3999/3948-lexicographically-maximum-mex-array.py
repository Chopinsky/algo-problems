'''
3948-lexicographically-maximum-mex-array
'''

from typing import List
from sortedcontainers import SortedSet  # pyright: ignore[reportMissingImports]


class Solution:
  def maximumMEX(self, nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)
    suffix = [0]*n

    # find the MEX for the suffix array: [i, n-1]
    s = SortedSet(range(n+1))
    for i in range(n-1, -1, -1):
      s.discard(nums[i])
      suffix[i] = s[0]
      # print('iter:', s)

    # largest possible MEX value is suffix[0]
    st = SortedSet(range(suffix[0]+1))
    v = suffix[0]
    # print('init:', suffix, st)

    for i in range(n):
      st.discard(nums[i])
      p = st[0] if st else v

      # only append if the current MEX is
      # the largest than the rest possible
      # choices, then reset and update
      if p >= v:
        ans.append(p)
        st.clear()

        if i < n-1:
          v = suffix[i+1]
          st.update(range(v+1))

    return ans
        