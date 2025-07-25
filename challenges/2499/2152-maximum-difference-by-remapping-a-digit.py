'''
2152-maximum-difference-by-remapping-a-digit
'''


class Solution:
  def minMaxDifference(self, num: int) -> int:
    base = str(num)
    cand = sorted(set(base))
    # print('init:', base, cand)

    def remap(a: int, b: int):
      va = str(a)    
      vb = str(b)
      v1 = ''.join(vb if d == va else d for d in base)
      return int(v1)

    maxv = num
    minv = num
    for d0 in cand:
      for d1 in range(10):
        if d0 == d1:
          continue

        val = remap(d0, d1)
        # print('iter:', d0, d1, val)
        maxv = max(maxv, val)
        minv = min(minv, val)

    return maxv - minv
