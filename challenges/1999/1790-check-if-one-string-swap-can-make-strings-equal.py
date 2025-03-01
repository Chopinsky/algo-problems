'''
1790-check-if-one-string-swap-can-make-strings-equal
'''

class Solution:
  def areAlmostEqual(self, s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 != n2:
      return False

    cand = list(s2)
    i, j = 0, n2-1
    while i < j and s1[i] == s2[i]:
      i += 1

    while i < j and s1[j] == s2[j]:
      j -= 1

    if i > j:
      return True

    if i != j:
      cand[i], cand[j] = cand[j], cand[i]

    # print('swap:', (i, j), cand, s1)

    return ''.join(cand) == s1

        