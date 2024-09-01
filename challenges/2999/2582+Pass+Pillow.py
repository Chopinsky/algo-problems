'''
2582. Pass the Pillow
'''

class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    rnd, rem = divmod(time, n-1)
    if rnd % 2 == 0:
      return 1+rem
    
    return n-rem
        