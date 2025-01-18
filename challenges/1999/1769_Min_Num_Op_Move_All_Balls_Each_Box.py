'''
1769. Minimum Number of Operations to Move All Balls to Each Box
'''

from typing import List


class Solution:
  def minOperations(self, boxes: str) -> List[int]:
    n = len(boxes)
    curr_ops = sum(i for i in range(n) if boxes[i] == '1')
    ans = [curr_ops]
    lc = boxes[:1].count('1')
    rc = boxes[1:].count('1')

    for i in range(1, n):
      curr_ops += lc - rc
      lc += 1 if boxes[i] == '1' else 0
      rc -= 1 if boxes[i] == '1' else 0
      ans.append(curr_ops)

    return ans
        