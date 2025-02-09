'''
3448-count-substrings-divisible-by-last-digit
'''

from collections import defaultdict


class Solution:
  def countSubstrings(self, s: str) -> int:
    curr = [defaultdict(int) for _ in range(10)]
    nxt = [defaultdict(int) for _ in range(10)]
    
    num = int(s[0])
    count = 1 if num > 0 else 0
    for i in range(1, 10):
      curr[i][num%i] = 1

    # print('init:', curr)
    for idx in range(1, len(s)):
      num = int(s[idx])
      for i in range(1, 10):
        # start a new substring ending with num
        nxt[i][num%i] += 1

        # update all previous substrings with the addition
        # of the tail `num` and the mod
        for j, cnt in curr[i].items():
          nxt[i][(j*10+num)%i] += cnt

        curr[i].clear()

      curr, nxt = nxt, curr
      count += curr[num][0]
      # print('iter:', idx, curr)

    return count
        