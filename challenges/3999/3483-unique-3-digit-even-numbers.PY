'''
3483-unique-3-digit-even-numbers
'''

from itertools import combinations


class Solution:
  def totalNumbers(self, digits: list[int]) -> int:
    vals = set()
    for a, b, c in combinations(digits, 3):
      # print('iter:', a, b, c)
      vals.add(100*a+10*b+c)
      vals.add(100*a+10*c+b)
      vals.add(100*b+10*a+c)
      vals.add(100*b+10*c+a)
      vals.add(100*c+10*a+b)
      vals.add(100*c+10*b+a)

    # print('done:', vals)
    return sum(1 if val%2 == 0 and val >= 100 else 0 for val in vals)
        