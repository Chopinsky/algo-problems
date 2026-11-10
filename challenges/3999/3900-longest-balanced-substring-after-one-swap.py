'''
3900-longest-balanced-substring-after-one-swap
'''

from collections import defaultdict


class Solution:
  def longestBalanced(self, s: str) -> int:
    zc = s.count('0')
    oc = s.count('1')
    n = len(s)

    if zc == 0 or oc == 0:
      return 0

    if zc == oc:
      return n

    ln = 0
    cz = 0
    z = []
    co = 0
    o = []
    seen = defaultdict(list)
    seen[0].append(-1)
    debug = False #True

    def u2(i: int, j: int):
      nonlocal ln
      oc_in = co - (o[j] if j >= 0 else 0)
      zc_left = z[j] if j >= 0  else 0
      zc_right = zc - z[i]

      if zc_left+zc_right > 0 and oc_in > 0:
        ln = max(ln, i-j)
        if debug:
          print('p1:', (j, i), zc_left, zc_right)

    def u1(i: int, j: int):
      nonlocal ln
      zc_in = cz - (z[j] if j >= 0 else 0)
      oc_left = o[j] if j >= 0 else 0
      oc_right = oc - o[i] 

      if oc_left+oc_right > 0 and zc_in > 0:
        ln = max(ln, i-j)
        if debug:
          print('p2:', (j, i), oc_left, oc_right)

    for i, ch in enumerate(s):
      if ch == '0':
        cz += 1
      else:
        co += 1

      z.append(cz)
      o.append(co)
      bal = co - cz
      if debug:
        print('iter:', i, bal, (co, cz))

      if bal == 0:
        ln = max(ln, i+1)
        if debug:
          print('full:', i+1)

      if bal in seen:
        ln = max(ln, i-seen[bal][0])
        if debug:
          print('p0:', i-seen[bal][0])

      if bal+2 in seen:
        u1(i, seen[bal+2][0])
        if len(seen[bal+2]) > 1:
          u1(i, seen[bal+2][1])

      if bal-2 in seen:
        u2(i, seen[bal-2][0])
        if len(seen[bal-2]) > 1:
          u2(i, seen[bal-2][1])

      seen[bal].append(i)

    return ln
        