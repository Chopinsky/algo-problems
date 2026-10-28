'''
4091-count-magical-substring-pairs-ii
'''


class Solution:
  def countMagicalPairs(self, s: str) -> int:
    n = len(s)

    # build prefix
    l = [[0]*27 for _ in range(n)]
    pos = [-1] * 26
    for i, ch in enumerate(s):
      pos[ord(ch)-ord('a')] = i
      p = sorted(x for x in pos if x != -1)[::-1]
      
      # subarr pos count to the left when the unique char count is k+1
      for k in range(len(p)):
        l[i][k+1] = p[k] - (p[k+1] if k+1 < len(p) else -1)

    # build suffix
    r = [[0]*27 for _ in range(n)]
    pos = [n] * 26
    for i in range(n-1, -1, -1):
      ch = s[i]
      pos[ord(ch)-ord('a')] = i
      q = sorted(x for x in pos if x != n)

      # subarr pos count to the right when the unique char count is k+1
      for k in range(len(q)):
        r[i][k+1] = (q[k+1] if k+1 < len(q) else n) - q[k]

    cnt = 0
    for i in range(n-1):
      for k in range(1, 27):
        # {left pos cnt with k unique char} * {right pos cnt with k unique char}
        cnt += l[i][k] * r[i+1][k]

    return cnt