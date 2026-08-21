'''
3069-distribute-elements-into-two-arrays-i
'''

class Solution:
  def resultArray(self, nums: list[int]) -> list[int]:
    a1, a2 = [nums[0]], [nums[1]]

    for val in nums[2:]:
      if a1[-1] > a2[-1]:
        a1.append(val)
      else:
        a2.append(val)

    return a1 + a2

        