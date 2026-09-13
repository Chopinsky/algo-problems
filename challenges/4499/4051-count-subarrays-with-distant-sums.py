'''
4051-count-subarrays-with-distant-sums
'''

from sortedcontainers import SortedList  # pyright: ignore[reportMissingImports]


class Solution:
  def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
    n = len(nums)
    total = n*(n+1)//2
    if k == 0:
      return total

    st = SortedList([0])
    cnt = 0
    pf = 0

    for val in nums:
      pf += val
      cnt += st.bisect_right(pf - (goal+k))           # higher bound count -> to the left
      cnt += len(st) - st.bisect_left(pf - (goal-k))  # lower bound count -> to the right
      st.add(pf)                                      # add the current prefix sum to the sorted list

    return cnt
