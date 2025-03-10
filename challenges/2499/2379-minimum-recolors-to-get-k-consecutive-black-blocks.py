'''
2379-minimum-recolors-to-get-k-consecutive-black-blocks
'''


class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    cnt = 0
    r = 0
    n = len(blocks)
    ops = n

    for l in range(n):
      if n-l < k:
        break
        
      while r < n and r-l+1 <= k:
        if blocks[r] == 'B':
          cnt += 1

        r += 1

      ops = min(ops, k-cnt)
      # print('iter:', (l, r), cnt)

      if blocks[l] == 'B':
        cnt -= 1

    return ops
      