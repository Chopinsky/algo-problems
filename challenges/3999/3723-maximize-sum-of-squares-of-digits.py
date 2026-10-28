'''
3723-maximize-sum-of-squares-of-digits
'''


class Solution:
  def maxSumOfSquares(self, num: int, sum: int) -> str:
    if 9*num < sum:
      return ""

    res = ""
    idx = 9

    while num > 0 and idx > 0:
      cnt = sum // idx
      sum = sum % idx
      if cnt > 0:
        res += str(idx) * cnt
        num -= cnt
      
      # print('iter:', (idx, cnt), sum)
      idx -= 1
        
    if num > 0:
      res += '0' * num

    return res
