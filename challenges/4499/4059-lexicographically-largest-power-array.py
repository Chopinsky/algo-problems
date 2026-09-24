'''
4059-lexicographically-largest-power-array
'''


class Solution:
  def largestPower(self, nums: list[int]) -> list[int]:
    powers = [0]*15
    done = [0]*15
    n = len(nums)

    def solve(arr: list[int], bit: int):
      if bit >= len(powers) or not arr:
        return

      if done[bit]:
        solve(arr, bit+1)
        return

      l = []
      r = []

      for val in arr:
        if val & (1<<(14-bit)):
          l.append(val)
        else:
          r.append(val)

      if l:
        powers[bit] += len(l)
        solve(l, bit+1)
      
      if r:
        done[bit] = 1
        solve(r, bit+1)

    solve(nums, 0)

    return powers
        