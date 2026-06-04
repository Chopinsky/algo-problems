'''
3751-total-waviness-of-numbers-in-range-i
'''


class Solution:
  def totalWaviness(self, num1: int, num2: int) -> int:
    cnt = 0

    def count_waves(val: int) -> int:
      if val < 100:
        return 0

      val = str(val)
      c = 0

      for i in range(1, len(val)-1):
        if val[i-1] < val[i] and val[i] > val[i+1]:
          c += 1

        if val[i-1] > val[i] and val[i] < val[i+1] :
          c += 1
      
      return c
        
    return sum(count_waves(val) for val in range(num1, num2+1))
