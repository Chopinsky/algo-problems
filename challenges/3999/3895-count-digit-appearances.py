'''
3895-count-digit-appearances
'''


class Solution:
  def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
    d = str(digit)
    return sum(str(val).count(d) for val in nums)
        