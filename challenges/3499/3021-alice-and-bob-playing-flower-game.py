'''
3021-alice-and-bob-playing-flower-game
'''


class Solution:
  def flowerGame(self, n: int, m: int) -> int:
    no = (n+1) // 2
    ne = n - no
    mo = (m+1) // 2
    me = m - mo
    # print('init:', (no, ne), (mo, me))
    return no*me + ne*mo
        