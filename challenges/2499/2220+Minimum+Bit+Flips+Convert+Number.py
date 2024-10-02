'''
2220. Minimum Bit Flips to Convert Number
'''

class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
    val = bin(start ^ goal)[2:]
    # print(val)
    return val.count('1')
        