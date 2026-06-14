'''
3876-construct-uniform-parity-array-ii
'''


class Solution:
  def uniformArray(self, nums: list[int]) -> bool:
    evens = sorted(val for val in nums if val%2 == 0)
    odds = sorted(val for val in nums if val%2 == 1)

    # already all odds or all evens
    if not evens or not odds:
      return True

    # can convert all evens to odds
    if evens[0]-odds[0] >= 1:
      return True

    return False
        