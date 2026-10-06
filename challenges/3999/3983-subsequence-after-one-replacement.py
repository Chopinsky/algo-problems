'''
3983-subsequence-after-one-replacement
'''


class Solution:
  def canMakeSubsequence(self, s: str, t: str) -> bool:
    ns = len(s)
    nt = len(t)
    if ns > nt:
      return False

    p0 = [-1]*ns
    p1 = [-1]*ns
    
    j = 0
    for i in range(nt):
      if j < ns and s[j] == t[i]:
        p0[j] = i
        j += 1

    j = ns-1
    for i in range(nt-1, -1, -1):
      if j >= 0 and s[j] == t[i]:
        p1[j] = i
        j -= 1

    # print('l->r', p0)
    # print('r->l', p1)

    if p0[-1] >= 0 or p1[0] >= 0:
      # already a subseq
      return True

    for i in range(ns):
      if i > 0 and p0[i-1] < 0:
        continue

      if i+1 < ns and p1[i+1] < 0:
        continue

      # change i-th char match
      prev = p0[i-1] if i >= 0 else -1
      nxt = p1[i+1] if i+1 < ns else nt
      # print('iter:', i, (prev, nxt))

      if prev+1 < nxt:
        return True

    return False
        