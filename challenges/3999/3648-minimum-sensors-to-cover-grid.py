'''
3648-minimum-sensors-to-cover-grid
'''

from math import ceil


class Solution:
  def minSensors(self, n: int, m: int, k: int) -> int:
    ln = 2*k + 1
    rc = max(1, ceil(n / ln))
    lc = max(1, ceil(m / ln))
    # print('init:', ln, lc, rc)

    return rc * lc
        