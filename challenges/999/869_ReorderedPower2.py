'''
869. Reordered Power of 2

You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
'''

from collections import Counter, defaultdict


class Solution:
  def reorderedPowerOf2(self, n: int) -> bool:
    cand = defaultdict(list)
    curr = 1
    ln = len(str(curr))

    while ln < 10:
      cand[ln].append(Counter(str(curr)))
      curr <<= 1
      ln = len(str(curr))
      # print('iter:', curr, Counter(str(curr)))

    # print('init:', len(cand), curr)
    base = Counter(str(n))
    ln = len(str(n))
    # print('run:', base, cand[ln])

    for c in cand[ln]:
      found = True
      for num, cnt in c.items():
        if num not in base or base[num] != cnt:
          found = False
          break

      if found:
        return True

    return False

  def reorderedPowerOf2(self, n: int) -> bool:
    base = 1
    upper = 1 << 30
    digits = Counter(str(n))
    # print(digits)
    
    while base < upper:
      d = Counter(str(base))
      if len(d) == len(digits):
        is_match = True
        for ch, cnt in d.items():
          if ch not in digits or cnt != digits[ch]:
            is_match = False
            break
        
        if is_match:
          return True
      
      base <<= 1
    
    return False
    