'''
3871-count-commas-in-range-ii
'''

class Solution:
  def countCommas(self, n: int) -> int:
    if n < 1000:
      return 0

    curr = 1
    commas = 0
    cnt = 0

    while curr <= n:
      nxt = 1000*curr
      # print('iter:', curr, nxt, commas)

      if n < nxt:
        cnt += commas * (n+1-curr)
      else:
        cnt += commas * (nxt-curr)

      curr = nxt
      commas += 1

    return cnt