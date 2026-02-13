'''
3714-longest-balanced-substring-ii
'''


class Solution:
  def longestBalanced(self, s: str) -> int:
    cnt = [0, 0, 0]
    ab = {(0, 0): -1}
    ac = {(0, 0): -1}
    bc = {(0, 0): -1}
    t = {}
    n = len(s)
    max_ln = 1
    prev_ch = ""
    single = 0

    for i in range(n):
      ch = s[i]
      idx = ord(ch) - ord('a')
      cnt[idx] += 1

      # check single:
      if ch != prev_ch:
        single = 0
        prev_ch = ch

      single += 1
      max_ln = max(max_ln, single)
      # print('===> iter:', i, ch, single)

      # check doubles
      # (a, b) pair
      pat0 = (cnt[0]-cnt[1], cnt[2])
      if pat0 in ab:
        max_ln = max(max_ln, i-ab[pat0])
        # print('double0:', i, (pat0, ab))

      ab[pat0] = min(ab.get(pat0, n), i)

      # (a, c) pair
      pat1 = (cnt[0]-cnt[2], cnt[1])
      if pat1 in ac:
        max_ln = max(max_ln, i-ac[pat1])
        # print('double1:', i, (pat1, ac))

      ac[pat1] = min(ac.get(pat1, n), i)

      # (b, c) pair
      pat2 = (cnt[1]-cnt[2], cnt[0])
      if pat2 in bc:
        max_ln = max(max_ln, i-bc[pat2])
        # print('double2:', i, (pat2, bc))

      bc[pat2] = min(bc.get(pat2, n), i)
      
      # triples
      if cnt[0] == cnt[1] and cnt[0] == cnt[2]:
        max_ln = max(max_ln, i+1)

      pat = (cnt[0]-cnt[1], cnt[0]-cnt[2])
      if pat in t:
        max_ln = max(max_ln, i-t[pat])
        # print('3u:', i, t[pat])

      # print('triple:', pat, t)
      t[pat] = min(t.get(pat, n), i)

    return max_ln
        