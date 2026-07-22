'''
3969-valid-subarrays-with-matching-sum-digits-i
'''

class Solution:
  def countValidSubarrays(self, nums: list[int], x: int) -> int:
    def count(j: int) -> int:
      curr = 0
      c = 0
      xs = str(x)

      for k in range(j, -1, -1):
        curr += nums[k]
        s = str(curr)
        if s[0] == xs and s[-1] == xs:
          c += 1 

      return c

    return sum(count(i) for i in range(len(nums)))
