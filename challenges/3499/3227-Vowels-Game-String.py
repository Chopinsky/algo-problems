'''
3227. Vowels Game in a String
'''


class Solution:
  def doesAliceWin(self, s: str) -> bool:
    v = set(['a', 'e', 'i', 'o', 'u'])
    c = sum(1 if ch in v else 0 for ch in s)
    # print('init:', c)

    return c > 0
