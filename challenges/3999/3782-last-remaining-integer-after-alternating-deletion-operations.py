'''
3782-last-remaining-integer-after-alternating-deletion-operations
'''


class Solution:
  def lastInteger(self, n: int) -> int:
    head = 1
    step = 1
    rem = n
    op_one = True

    while rem > 1:
      # from right to left, original head is 
      # eliminated, jump to the next head
      if not op_one and rem%2 == 0:
        head += step

      rem = (rem+1) // 2
      step <<= 1  # removed half elements
      op_one = not op_one

    return head
        