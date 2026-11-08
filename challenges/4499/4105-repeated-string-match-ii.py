'''
4105-repeated-string-match-ii
'''


class Solution:
  def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
    '''
    Fine and Wilf's Theorem states that if two periodic strings with periods
    n and m match on a prefix of length n + m - gcd(n, m), they match everywhere.

    So the solution is to generate the min-length of the multiplied a and b and
    check if b-repeat is the substring of a-repeat.
    '''

    la = len(a)
    lb = len(b)
    src = b * min(y, la//lb + 2)
    end = min(la-1, la*x - lb*y) + len(src)

    if end < len(src):
      return False

    base = a * ((end+la-1) // la)
    tgt = base[:end]

    return src in tgt
