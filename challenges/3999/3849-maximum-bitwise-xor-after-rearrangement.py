'''
3849-maximum-bitwise-xor-after-rearrangement
'''


class Solution:
  def maximumXor(self, s: str, t: str) -> str:
    cnt = [0, 0]
    for ch in t:
      if ch == '0':
        cnt[0] += 1
      else:
        cnt[1] += 1

    # print('init:', cnt)
    res = []

    for ch in s:
      if (ch == '0' and cnt[1] > 0) or (ch == '1' and cnt[0] > 0):
        res.append('1')
        if ch == '0':
          cnt[1] -= 1
        else:
          cnt[0] -= 1
      else:
        res.append('0')
      
    return ''.join(res)
        